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
BONUS_STEP = 3  # каждая третья операция со счетом
BONUS_OPERATIONS = 0.03  # бонусные проценты за каждую третью операцию 3%
all_money = 0
operations_counter = 1


def validation_request(message: str) -> int:
    while True:
        try:
            input_number: int = int(input(message))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
        except Exception as e:
            print("Произошла ошибка:", str(e))
    return input_number


def check_control_value(request_money: int) -> bool:
    if request_money % CONTROL_VALUE == 0:
        return True
    else:
        print('Сумма должна быть кратна 50')
        return False


def calculation_commission(request_money: int) -> int | float:
    if all_money >= LIMIT_FOR_RICH:
        return request_money * COMMISSION_FOR_RICH
    else:
        result = request_money * COMMISSION
        if result < MIN_COMMISSION:
            return MIN_COMMISSION
        elif result > MAX_COMMISSION:
            return MAX_COMMISSION
        return result


def counter_bonus(request_money: int) -> int | float:
    if operations_counter % BONUS_STEP == 0:
        return request_money * BONUS_OPERATIONS
    else:
        return 0


def output(money: int | float, commission: int | float, bonus: int | float) -> str:
    if bonus != 0:
        print(f'Комиссия за операцию: -{commission} | бонусы за операцию: +{bonus} | на вашем счету:{money}')
    else:
        print(f'Комиссия за операцию: -{commission} | на вашем счету:{money}')


print('Добро пожаловать в банкомат!\n1. Пополнить баланс\n2. Снять наличные\n0. Выход')
while True:
    choice = validation_request('Введите команду: ')
    match choice:
        case 1:
            print('На вашем счету:' + str(all_money))

            while True:
                request_money = validation_request('Введите сумму пополнения баланса: ')
                if check_control_value(request_money):
                    commission = calculation_commission(request_money)
                    bonus = counter_bonus(request_money)
                    all_money += request_money - commission + bonus

                    output(all_money, commission, bonus)
                    operations_counter += 1
                    break

        case 2:
            print('На вашем счету:' + str(all_money))

            while True:
                request_money = validation_request('Введите сумму снятия со счета: ')
                if check_control_value(request_money):
                    commission = calculation_commission(request_money)
                    bonus = counter_bonus(request_money)
                    if request_money + calculation_commission(request_money) > all_money:
                        print('На счету недостаточно средств!')
                    else:
                        all_money -= request_money + commission - bonus
                        output(all_money, commission, bonus)
                        operations_counter += 1
                    break

        case 0:
            print('До свидания!')
            exit()

        case _:
            print('Команда меню не найдена, повторите ввод!')
