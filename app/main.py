from app.service import Wallet
from app.validators import Validator


def main():
    file_path = '../wallet/finances.csv'
    data = Wallet.load_data(file_path)

    while True:
        print('\nВыберите действие:')
        print('1. Вывод баланса')
        print('2. Добавление записи')
        print('3. Редактирование записи')
        print('4. Поиск по записям')
        print('5. Выход')

        choice = input('\nВведите номер действия: ').strip()

        match choice:
            case '1':
                Wallet.show_balance(data)

            case '2':
                get_date = input('Введите дату (гггг-мм-дд): ').strip()
                transaction_date = Validator.validate_transaction_date(get_date)

                get_category = input('Введите категорию (Доход/Расход): ').strip().title()
                category = Validator.validate_category(get_category)

                get_amount = input('Введите сумму: ').strip()
                amount = Validator.validate_amount(get_amount)

                description = input('Введите описание: ').strip()
                data = Wallet.add_record(data, transaction_date, category, amount, description)
                Wallet.save_data(data, file_path)
                print('Запись успешно добавлена.')

            case '3':
                get_index = input('Введите индекс записи для редактирования: ').strip()
                index = Validator.validate_index(get_index)

                get_date = input('Введите новую дату (гггг-мм-дд): ').strip()
                transaction_date = Validator.validate_transaction_date(get_date)

                get_category = input('Введите новую категорию (Доход/Расход): ').strip().title()
                category = Validator.validate_category(get_category)

                get_amount = input('Введите новую сумму: ').strip()
                amount = Validator.validate_amount(get_amount)

                description = input('Введите новое описание: ').strip()
                data = Wallet.edit_record(data, index, transaction_date, category, amount, description)
                Wallet.save_data(data, file_path)
                print('Запись успешно отредактирована.')

            case '4':
                print('Введите параметры для поиска:\n')

                category = input('Категория (Доход/Расход): ').strip().title()
                if category != '':
                    category = Validator.validate_category(category)

                get_date = input('Дата (гггг-мм-дд): ').strip()
                if get_date != '':
                    transaction_date = Validator.validate_transaction_date(get_date)

                amount = input('Сумма: ').strip()
                if amount != '':
                    amount = Validator.validate_amount(amount)

                result = Wallet.search_records(data, category, transaction_date, amount)
                print(result)

            case '5':
                break

            case _:
                print('Неверный выбор. Пожалуйста, выберите номер действия из списка.')


if __name__ == '__main__':
    main()
