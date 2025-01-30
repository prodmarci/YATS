import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

import importlib
import user.user as userdata
import products.products as productdata
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
    app.run_polling()

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

# GETTER AND SETTER FOR BOT NAME STRING
def set_get_bot_name(context=None):
    if context is not None:
        set_get_bot_name.bot_name = context.bot.name

    return getattr(set_get_bot_name, "bot_name", BOT_NAME)

# START COMMAND
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    
    # SAVES BOT NAME IN THE FUNCTION
    set_get_bot_name(context)
    
    message = get_user_info(user, "lang").get_main_menu_text(
        get_user_info(user, "user_id"),
        get_user_info(user, "username"),
        set_get_bot_name(),
        get_user_info(user, "balance"))
    await update.message.reply_text(message, reply_markup=get_main_menu(user))
    
# GETTER FOR MAIN MENU, ADDS AN ADMIN PANEL FOR OPERATORS
def get_main_menu(user):
    keyboard = [
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("products"), callback_data="products_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("topup"), callback_data="topup_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("operator"), url=f"https://t.me/{OPERATOR_USERNAME}"),
         InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("channel"), url=CHANNEL_LINK)],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("language"), callback_data="language_callback")]
    ]
    
    if get_user_info(user, "user_id") in OPERATOR_IDS:
        keyboard.append(
            [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("admin"), callback_data="admin_panel")]
        )
    
    return InlineKeyboardMarkup(keyboard)
    
# MAIN BUTTON HANDLER
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

        case "admin_panel":
            message = get_user_info(user, "lang").get_admin_menu_text(set_get_bot_name())
            #TODO: ADD TOTAL USERS STAT
            await query.message.edit_text(message, reply_markup=get_admin_menu(user))
        
        case "back":
            message = get_user_info(user, "lang").get_main_menu_text(
                get_user_info(user, "user_id"),
                get_user_info(user, "username"),
                set_get_bot_name(),
                get_user_info(user, "balance"))
            
            await query.message.edit_text(message, reply_markup=get_main_menu(user))

# GETTER FOR PRODUCTS MENU & GENERATOR FOR ALL THE PRODUCT BUTTONS
def get_products_menu(user):
    keyboard = []
    products = productdata.list_products()
    
    for product in products:
        if product['in_stock'] == False:
            in_stock = get_user_info(user, "lang").get_product_state("soldout")
        else:
            in_stock = get_user_info(user, "lang").get_product_state("instock")
        
        button_text = f"{product['name']} - {product['price']} PLN - {in_stock}"
        callback_data = f"product_{product['name'].lower().replace(' ', '_')}"
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

# GETTER FOR ADMIN MENU
def get_admin_menu(user):
    keyboard = [
        [InlineKeyboardButton("product management", callback_data="topup_callback")],
        [InlineKeyboardButton("banhammer", callback_data="topup_callback")],
        [InlineKeyboardButton(get_user_info(user, "lang").get_main_menu_button_text("back"), callback_data="back")]
    ]
    
    return InlineKeyboardMarkup(keyboard)

# AUTOSTART
if __name__ == "__main__":
    main()