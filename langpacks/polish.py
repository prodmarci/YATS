def get_main_menu_text(user_id: int, username: str, bot_name: str, balance: float) -> str:
    return (
        f"Witaj, {username} w {bot_name}!\n\n"
        f"💌 Twoje ID: {user_id}\n"
        f"💰 Saldo: {balance} PLN.\n\n"
        f"💸 Dostępne metody płatności:\n"
        + get_payment_text("btc") + "\n"
        + get_payment_text("sol") + "\n"
        + get_payment_text("eth") +"\n"
        + get_payment_text("blik") +"\n\n"
        f"⚠️ Wpłata salda powyższymi metodami płatności odbywa się automatycznie w ciągu 30 minut."
    )
    
def get_topup_menu_text(bot_name: str) -> str:
    return (
        f"💰 Uzupełnij saldo w {bot_name}!\n\n"
        f"⚠️ Sugerujemy korzystanie z płatności w kryptowalutach korzystając z zabezpieczonych portfeli krypto.\n\n"
        f"💸 Wybierz metodę płatności:\n"
    )
    
def get_products_menu_text(bot_name: str) -> str:
    return (
        f"🛍️ Produkty w {bot_name}!\n\n"
        f"🛒 Wybierz produkt z listy poniżej:\n"
    )
    
def get_language_menu_text(bot_name: str) -> str:
    return (
        f"🌐 Wspierane języki w {bot_name}!\n\n"
        f"🌍 Wybierz język z listy poniżej:\n"
    )
    
def get_admin_menu_text(bot_name: str) -> str:
    return (
        f"📊 Panel Administracyjny w {bot_name}!\n\n"
        f"⚠️ Wszystkie dane powinny być wyświetlane w czasie rzeczywistym.\n\n"
        f"🤖 Wybierz funkcję:\n"
    )
    
def get_product_state(state):
    match state:
        case "instock":
            return (f"🟩 DOSTĘPNY")
        case "soldout":
            return (f"🟥 WYPRZEDANY")
        case _:
            return (f"⚠️ Błąd")
    
def get_payment_text(button_name):
    match button_name:
        case "btc":
            return (f"🪙 Bitcoin (BTC) - bonus 5%")
        case "sol":
            return (f"🌀 Solana (SOL) - bonus 5%")
        case "eth":
            return (f"💎 Ethereum (ETH) - bonus 5%")
        case "blik":
            return (f"💳 Doładowanie Blik (PLN)")
        case _:
            return (f"⚠️ Błąd")
    
def get_main_menu_button_text(button_name):
    match button_name:
        case "topup":
            return (f"💰 Uzupełnij Saldo")
        case "products":
            return (f"🛍️ Produkty")
        case "operator":
            return (f"⭐ Operator")
        case "channel":
            return (f"📢 Kanał Informacyjny")
        case "language":
            return (f"🌐 Wybierz Język")
        case "admin":
            return (f"📊 Panel Administracyjny")
        case "back":
            return (f"🔙 Powrót")
        case _:
            return (f"⚠️ Błąd")
        