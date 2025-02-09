import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

import user.user as userdata
import products.products as productdata

import stats.bot as bot_visitdata
import stats.product as product_visitdata

import importlib
import langpacks.english
import langpacks.polish

# JSON CONFIG LOAD
with open(r'd34d-shop\config.json', 'r') as file:
    config = json.load(file)

TOKEN = config['bot_token']
BOT_NAME = config['bot_name']
CHANNEL_LINK = config['channel_link']
OPERATOR_IDS = config['operator_ids']
OPERATOR_USERNAME = config['operator_username']

# MAIN FUNCTION - INITIALIZATION
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling(drop_pending_updates=True)

# CHECK FOR USER IN OPERATOR ID'S CONFIG LINE
def admin_check(user):
    if get_user_info(user, "user_id") in OPERATOR_IDS:
        return True
    else:
        return False

# GETTER FOR USER INFO (LOADS PERSISTENT USER DATA)
def get_user_info(user, info):
    user_id = user.id
    username = user.first_name if user.first_name else user.username
    match info:
        case "user_id":
            return user_id
        case "username":
            return username
        case "balance":
            return 0
        case "lang":
            return importlib.import_module(userdata.get_user_language(user_id))

# GETTER FOR PRODUCT INFO
def get_product_info(product_id, info):
    product = productdata.get_product_by_id(product_id)
    match info:
        case "name":
            return product['name']
        case "price":
            return product['price']
        case "description":
            return product['description']
        case "stock":
            return product['in_stock']

# GETTER AND SETTER FOR BOT NAME STRING
def set_get_bot_name(context=None):
    if context is not None:
        set_get_bot_name.bot_name = context.bot.name

    return getattr(set_get_bot_name, "bot_name", BOT_NAME)

# START COMMAND
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    
    # DONE: SAVES BOT NAME
    set_get_bot_name(context)
    
    bot_visitdata.add_user(get_user_info(user,"user_id"))
    
    message = get_user_info(user, "lang").get_main_menu_text(
        get_user_info(user, "user_id"),
        get_user_info(user, "username"),
        set_get_bot_name(),
        get_user_info(user, "balance"))
    await update.message.reply_text(message, reply_markup=get_main_menu(user))
    
# MAIN BUTTON HANDLER
# TODO: CREATE PAGE FOR PRODUCT CALLBACK
async def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user = query.from_user
    await query.answer()
    
    match query.data:
        case "products_callback":
            message = get_user_info(user, "lang").get_products_menu_text(set_get_bot_name())
            
            await query.message.edit_text(message, reply_markup=get_products_menu(user))
        
        case "topup_callback":
            message = get_user_info(user, "lang").get_topup_menu_text(set_get_bot_name())
            
            await query.message.edit_text(message, reply_markup=get_topup_menu(user))

        case "language_callback":
            message = get_user_info(user, "lang").get_language_menu_text(set_get_bot_name())
            
            await query.message.edit_text(message, reply_markup=get_language_menu(user))
            
        case _ if query.data.startswith("set_language_"):
            lang = "langpacks." + query.data.replace("set_language_", "").replace("_", " ").lower()
            userdata.set_user_language(get_user_info(user, "user_id"), lang)
            
            message = get_user_info(user, "lang").get_main_menu_text(
                get_user_info(user, "user_id"),
                get_user_info(user, "username"),
                set_get_bot_name(),
                get_user_info(user, "balance"))
            
            await query.message.edit_text(message, reply_markup=get_main_menu(user))
            
        case _ if query.data.startswith("product_"):
            product_id = query.data.replace("product_","")
            product_visitdata.increment_visits(product_id)
            
            if get_product_info(product_id, "stock") == 0:
                in_stock = get_user_info(user, "lang").get_product_state("soldout")
            else:
                in_stock = get_user_info(user, "lang").get_product_state("instock")
            
            message = get_user_info(user, "lang").get_product_menu_text(
                set_get_bot_name(),
                get_product_info(product_id, "name"),
                get_product_info(product_id, "price"),
                get_product_info(product_id, "description"),
                in_stock,
                get_product_info(product_id, "stock")
                )
            
            await query.message.edit_text(message, reply_markup=get_product_menu(user, product_id))

        case "admin_panel":
            if admin_check(user):
                message = get_user_info(user, "lang").get_admin_menu_text(
                    set_get_bot_name(),
                    bot_visitdata.get_user_count(30)
                    )
                await query.message.edit_text(message, reply_markup=get_admin_menu(user))
            else:
                message = get_user_info(user, "lang").get_no_permission_text()
                await query.message.edit_text(message, reply_markup=get_back_button(user))
        
        case "back":
            message = get_user_info(user, "lang").get_main_menu_text(
                get_user_info(user, "user_id"),
                get_user_info(user, "username"),
                set_get_bot_name(),
                get_user_info(user, "balance"))
            
            await query.message.edit_text(message, reply_markup=get_main_menu(user))

# GETTER FOR MAIN MENU, ADDS AN ADMIN PANEL FOR OPERATORS
# TODO: CART CALLBACK
def get_main_menu(user):
    keyboard = [
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("products"), callback_data="products_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("cart"), callback_data="cart_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("topup"), callback_data="topup_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("operator"), url=f"https://t.me/{OPERATOR_USERNAME}"),
         InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("channel"), url=CHANNEL_LINK)],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("language"), callback_data="language_callback")]
    ]
    
    if admin_check(user):
        keyboard.append(
            [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("admin"), callback_data="admin_panel")]
        )
    
    return InlineKeyboardMarkup(keyboard)

# GETTER FOR PRODUCT MENU
# TODO: PAYMENT HANDLING
def get_product_menu(user, product_id):
    callback_data = f"product_{product_id}"
    
    if (get_product_info(product_id,"stock")):
        keyboard = [
            [InlineKeyboardButton(get_user_info(user, "lang").get_purchase_button(), callback_data=callback_data)],
        ]
    else:
        keyboard = [
            [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("operator"), url=f"https://t.me/{OPERATOR_USERNAME}")],
        ]
    
    keyboard.append([InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="products_callback")])
    
    return InlineKeyboardMarkup(keyboard)

# GETTER FOR PRODUCTS MENU & GENERATOR FOR ALL THE PRODUCT BUTTONS
def get_products_menu(user):
    keyboard = []
    products = productdata.list_products()
    
    for product in products:
        if product['in_stock'] == False:
            in_stock = get_user_info(user, "lang").get_product_state("soldout")
        else:
            in_stock = get_user_info(user, "lang").get_product_state("instock")
            
        if admin_check(user):
            button_text = f"ID: {product['id']} - {product['name']} - {product['price']} PLN - {in_stock}"
        else:
            button_text = f"{product['name']} - {product['price']} PLN - {in_stock}"
        
        callback_data = f"product_{product['id']}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

    keyboard.append([InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")])

    return InlineKeyboardMarkup(keyboard)

# GETTER FOR TOPUP MENU
def get_topup_menu(user):
    keyboard = [
        [InlineKeyboardButton(get_user_info(user, "lang").get_payment_text("btc"), callback_data="topup_balance_btc")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_payment_text("sol"), callback_data="topup_balance_sol")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_payment_text("eth"), callback_data="topup_balance_eth")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_payment_text("blik"), callback_data="topup_balance_blik")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")]
    ]
    
    return InlineKeyboardMarkup(keyboard)

# GETTER FOR LANGUAGE MENU
def get_language_menu(user):
    keyboard = [
        [InlineKeyboardButton("🇵🇱 Polski", callback_data="set_language_polish")],
        [InlineKeyboardButton("🇺🇸 English", callback_data="set_language_english")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")]
    ]
    
    return InlineKeyboardMarkup(keyboard)

# GETTER FOR BACK BUTTON (MAIN MENU BACK)
def get_back_button(user):
    keyboard = [
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")]
    ]
    
    return InlineKeyboardMarkup(keyboard)

# GETTER FOR ADMIN MENU
def get_admin_menu(user):
    keyboard = [
        [InlineKeyboardButton(get_user_info(user, "lang").get_admin_menu_button_text("stats"), callback_data="back")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_admin_menu_button_text("products"), callback_data="back")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")]
    ]
    
    return InlineKeyboardMarkup(keyboard)

# AUTOSTART
if __name__ == "__main__":
    main()