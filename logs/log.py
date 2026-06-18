from datetime import datetime
from colorama import Fore as f

def timenow():
    date = datetime.now()
    time = (date.strftime("%Y-%m-%d %H:%M:%S"))
    return time

def start():
    time = timenow()

    print(f"{f.LIGHTBLACK_EX}{time}{f.MAGENTA} > {f.LIGHTBLUE_EX}TON CHECKER {f.GREEN}by KitikiticH{f.LIGHTBLUE_EX} успешно инициализирован{f.RESET}")
    with open("logs/logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{time} > TON CHECKER by KitikiticH успешно инициализирован\n")
        log.close()

def price_error(token):
    time = timenow()

    print(f"{f.LIGHTBLACK_EX}{time}{f.MAGENTA} > {f.RED}Произошла непредвиденная ошибка при получении цены {f.BLUE}{token}{f.RESET}")
    with open("logs/logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{time} > Произошла непредвиденная ошибка при получении цены {token}\n")
        log.close()

def error(error):
    time = timenow()

    print(f"{f.LIGHTBLACK_EX}{time}{f.MAGENTA} > {f.RED}{error}{f.RESET}")
    with open("logs/logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{time} > {error}\n")
        log.close()

def price(token, price):
    time = timenow()

    print(f"{f.LIGHTBLACK_EX}{time}{f.MAGENTA} > {f.YELLOW}Цена {f.BLUE}{token}{f.YELLOW} зафиксирована на {f.GREEN}{price}${f.RESET}")
    with open("logs/logs.txt", "a", encoding="utf-8") as log:
        log.write(f"{time} > Цена {token} зафиксирована на {price}$\n")
        log.close()