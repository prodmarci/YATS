# LANGPACK START

def get_no_permission_text():
    return (
        f"💀 Permission denied, unauthorized access blocked.\n\n"
        f"🤡 Try better next time."
        )

def get_main_menu_text(user_id: int, username: str, bot_name: str, balance: float) -> str:
    return (
        f"Welcome, {username} at {bot_name}!\n\n"
        f"💌 Account ID: {user_id}\n"
        f"💰 Balance: {balance} PLN.\n\n"
        f"💸 Available payment methods:\n"
        + get_payment_text("btc") + "\n"
        + get_payment_text("sol") + "\n"
        + get_payment_text("eth") +"\n"
        + get_payment_text("blik") +"\n\n"
        f"⚠️ Balance topup using above payment methods is automatic within 30 minutes."
    )
    
def get_topup_menu_text(bot_name: str) -> str:
    return (
        f"💰 Topup balance at {bot_name}!\n\n"
        f"⚠️ We suggest using cryptocurrency payments using secured crypto wallets.\n\n"
        f"💸 Choose payment method:\n"
    )
    
def get_products_menu_text(bot_name: str) -> str:
    return (
        f"🛍️ Products at {bot_name}!\n\n"
        f"⚠️ Availability info:\n"
        f"Items in stock are marked with 🟩 next to their name, while unavailable items are indicated with 🟥.\n\n"
        f"🛒 Choose product from the list below:\n"
    )
    
def get_language_menu_text(bot_name: str) -> str:
    return (
        f"🌐 Supported languages at {bot_name}!\n\n"
        f"🌍 Choose language from list below:\n"
    )
    
def get_admin_menu_text(bot_name: str, thirty: int) -> str:
    return (
        f"📊 Admin Panel at {bot_name}!\n\n"
        f"🌍 Users last 30 days: {thirty}\n\n"
        f"⚠️ All data displayed is being updated in realtime.\n\n"
        f"🤖 Choose desired function:\n"
    )
    
def get_product_state(state):
    match state:
        case "instock":
            return (f"🟩")
        case "soldout":
            return (f"🟥")
        case _:
            return (f"⚠️")
        
def get_soldout_product_text():
    return (f"⚠️ Product is currently out of stock, contact operator for restock info.")
        
def get_product_menu_text(bot_name: str, item_name: str, price: int, description: str, stock: str, instock: bool) -> str:
    if instock:
        return (
            f"🛍️ Shopping at {bot_name}\n\n"
            f"{item_name} - {price} PLN - {stock}\n\n"
            f"{description}\n\n"
        )
    else:
        soldout_message = get_soldout_product_text()
        return (
            f"🛍️ Shopping at {bot_name}\n\n"
            f"{item_name} - {price} PLN - {stock}\n\n"
            f"{description}\n\n"
            f"{soldout_message}"
        )

    
def get_purchase_button():
    return (f"🛒 Add to cart")
    
def get_payment_text(payment_method):
    match payment_method:
        case "btc":
            return (f"🪙 Bitcoin (BTC) - 5% bonus")
        case "sol":
            return (f"🌀 Solana (SOL) - 5% bonus")
        case "eth":
            return (f"💎 Ethereum (ETH) - 5% bonus")
        case "blik":
            return (f"💳 Blik Topup (PLN)")
        case _:
            return (f"⚠️ ERROR")
    
def get_main_menu_button_text(button_name):
    match button_name:
        case "topup":
            return (f"💰 Balance topup")
        case "products":
            return (f"🛍️ Products")
        case "cart":
            return (f"🛒 Your cart")
        case "operator":
            return (f"⭐ Contact Operator")
        case "channel":
            return (f"📢 Information channel")
        case "language":
            return (f"🌐 Choose language")
        case "admin":
            return (f"📊 Admin Panel")
        case "back":
            return (f"🔙 Back")
        case _:
            return (f"⚠️ ERROR")    

def get_admin_menu_button_text(button_name):
    match button_name:
        case "stats":
            return (f"📊 Analitycs")
        case "products":
            return (f"🛍️ Product management")
        case _:
            return (f"⚠️ ERROR")