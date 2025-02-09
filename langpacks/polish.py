# LANGPACK START

def get_no_permission_text():
    return (
        f"💀 Odmowa permisji, zablokowano nieautoryzowaną próbę dostepu.\n\n"
        f"🤡 Następnym razem bardziej się postaraj."
        )

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
        f"⚠️ Informacja o dostępności:\n"
        f"Produkty dostępne w magazynie mają obok swojej nazwy znak 🟩, a produkty niedostępne są oznaczone znakiem 🟥.\n\n"
        f"🛒 Wybierz produkt z listy poniżej:\n"
    )
    
def get_language_menu_text(bot_name: str) -> str:
    return (
        f"🌐 Wspierane języki w {bot_name}!\n\n"
        f"🌍 Wybierz język z listy poniżej:\n"
    )
    
def get_admin_menu_text(bot_name: str, thirty: int) -> str:
    return (
        f"📊 Panel Administracyjny w {bot_name}!\n\n"
        f"🌍 Użytkownicy w ostatnie 30 dni: {thirty}\n\n"
        f"⚠️ Wszystkie dane powinny są wyświetlane w czasie rzeczywistym.\n\n"
        f"🤖 Wybierz funkcję:\n"
    )
    
def get_product_state(state: str) -> str:
    match state:
        case "instock":
            return (f"🟩")
        case "soldout":
            return (f"🟥")
        case _:
            return (f"⚠️")
        
def get_soldout_product_text():
    return (f"⚠️ Produkt jest obecnie niedostępny, skontaktuj się z operatorem w celu uzyskaniu informacji o ponownej dostępności.")

def get_product_menu_text(bot_name: str, item_name: str, price: int, description: str, stock: str, instock: bool) -> str:
    if instock:
        return (
            f"🛍️ Zakup w {bot_name}\n\n"
            f"{item_name} - {price} PLN - {stock}\n\n"
            f"{description}\n"
        )
    else:
        soldout_message = get_soldout_product_text()
        return (
            f"🛍️ Zakup w {bot_name}\n\n"
            f"{item_name} - {price} PLN - {stock}\n\n"
            f"{description}\n\n"
            f"{soldout_message}"
        )
    
def get_purchase_button():
    return (f"🛒 Dodaj do koszyka")
    
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
        case "cart":
            return (f"🛒 Twój koszyk")
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

def get_admin_menu_button_text(button_name):
    match button_name:
        case "stats":
            return (f"📊 Statystyki")
        case "products":
            return (f"🛍️ Zarządzanie produktami")
        case _:
            return (f"⚠️ ERROR")