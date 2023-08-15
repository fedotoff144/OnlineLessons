# Задача №6
# Напишите программу банкомат.
#
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


COMMISSION = 0.015  # процент за снятие 1.5%
MIN_COMMISSION = 30
MAX_COMMISSION = 600
COMMISSION_FOR_RICH = 0.1  # 10%
LIMIT_FOR_RICH = 5_000_000
CONTROL_VALUE = 50
BONUS_STEP = 3 # каждая третья операция со счетом
BONUS_OPERATIONS = 0.03  # бонусные проценты за каждую третью операцию 3%
all_money = 0
operations_counter = 1


def get_money_request(message: str) -> int:
    while True:
        try:
            cash = int(input(message))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
        except Exception as e:
            print("Произошла ошибка:", str(e))
    return cash


def check_money_request(request: int) -> bool:
    res = True
    if request % CONTROL_VALUE != 0:
        res = False
    return res


def calculation_commission(request_money: int) -> int | float:
    if all_money >= LIMIT_FOR_RICH:
        return request_money * COMMISSION_FOR_RICH
    else:

        result = request_money * COMMISSION

        if result < MIN_COMMISSION:
            return MIN_COMMISSION
        elif result > MAX_COMMISSION:
            return MIN_COMMISSION
        return result


def counter_bonus(request_money: int) -> int | float:
    if operations_counter % BONUS_STEP == 0:
        return request_money * BONUS_OPERATIONS
    else:
        return 0


print('Добро пожаловать в банкомат!\n1. Пополнить баланс\n2. Снять наличные\n0. Выход')
while True:
    choice = int(input('Введите команду: '))
    match choice:
        case 1:
            request_money = get_money_request('Введите сумму пополнения баланса: ')
            if check_money_request(request_money):
                all_money += request_money + counter_bonus(request_money)
                print('На вашем счету:' + str(all_money))
                operations_counter += 1
            else:
                print('Сумма должна быть кратна 50')

        case 2:
            request_money = get_money_request('Введите сумму снятия со счета: ')
            print(all_money)

        case 0:
            print('До свидания!')
            exit()
        case _:
            print('Ошибка! Повторите ввод.')

