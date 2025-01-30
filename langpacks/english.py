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
        f"🛒 Choose product from the list below:\n"
    )
    
def get_language_menu_text(bot_name: str) -> str:
    return (
        f"🌐 Supported languages at {bot_name}!\n\n"
        f"🌍 Choose language from list below:\n"
    )
    
def get_admin_menu_text(bot_name: str) -> str:
    return (
        f"📊 Admin Panel at {bot_name}!\n\n"
        f"⚠️ All data displayed should update in realtime.\n\n"
        f"🤖 Choose desired function:\n"
    )
    
def get_product_state(state):
    match state:
        case "instock":
            return (f"🟩 IN STOCK")
        case "soldout":
            return (f"🟥 SOLD OUT")
        case _:
            return (f"⚠️ ERROR")
    
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