correct_pin = '1234'
balance = 1000.0
attempts = 0
authenticated = False

# Проверка на PIN код (макс 3 опита)
while attempts < 3:
    user_pin = input('Въведете 4-цифрен PIN код: ')
    if user_pin == correct_pin:
        authenticated = True
        print('Успешна автентикация! Добре дошли.')
        break
    else:
        attempts += 1
        print(f'Грешен PIN! Оставащи опити: {3 - attempts}')

if not authenticated:
    print('Картата е блокирана поради 3 грешни опита!')
else:
    # Главен цикъл на менюто
    while True:
        print('\n=== МЕНЮ БАНКОМАТ ===')
        print('1. Проверка на баланс')
        print('2. Теглене на сума')
        print('3. Депозиране на сума')
        print('4. Изход')
        choice = input('Изберете опция (1-4): ')
        
        if choice == '1':
            print(f'Текущ баланс: {balance:.2f} евро.')
        elif choice == '2':
            amount = float(input('Въведете сума за теглене: '))
            if amount <= 0:
                print('Сумата трябва да е положително число!')
            elif amount > balance:
                print('Нямате достатъчна наличност по сметката!')
            elif amount % 10 != 0:
                print('Сумата трябва да е кратна на 10 евро.!')
            else:
                balance -= amount
                print(f'Успешно изтеглени {amount:.2f} евро. Нов баланс: {balance:.2f} евро.')
        elif choice == '3':
            amount = float(input('Въведете сума за депозиране: '))
            if amount <= 0:
                print('Невалидна сума!')
            else:
                balance += amount
                print(f'Успешно депозирани {amount:.2f} евро. Нов баланс: {balance:.2f} евро.')
        elif choice == '4':
            print('Благодарим ви, че използвахте нашите услуги! Довиждане.')
            break
        else:
            print('Невалиден избор! Моля изберете от 1 до 4.')
