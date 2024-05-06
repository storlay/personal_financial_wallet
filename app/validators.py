from datetime import datetime

from app.service import Wallet


class Validator:
    @classmethod
    def validate_amount(
            cls,
            amount: str,
    ) -> float:
        amount_is_valid = cls._amount_validator(amount)
        while not amount_is_valid:
            print(f'Неверный формат суммы - {amount}')
            amount = input('Введите корректную сумму: ').strip()
            amount_is_valid = cls._amount_validator(amount)
        return float(amount)

    @classmethod
    def validate_category(
            cls,
            category: str
    ) -> str:
        category_is_valid = cls._category_validator(category)
        while not category_is_valid:
            print(f'Неверная категория - {category}')
            category = input('Введите корректную категорию (Доход/Расход): ').strip().title()
            category_is_valid = cls._category_validator(category)
        return category

    @classmethod
    def validate_transaction_date(
            cls,
            transaction_date: str
    ) -> str:
        date_is_valid = cls._date_validator(transaction_date)
        while not date_is_valid:
            print(f'Неверный формат даты - {transaction_date}')
            transaction_date = input('Введите корректную дату (гггг-мм-дд): ').strip()
            date_is_valid = cls._date_validator(transaction_date)
        return transaction_date

    @classmethod
    def validate_index(
            cls,
            index: str
    ) -> int:
        index_is_valid = cls._index_validator(index)
        while not index_is_valid:
            print(f'Неверный формат или номер индекса - {index}')
            index = input('Введите корректный индекс записи: ').strip()
            index_is_valid = cls._index_validator(index)
        return int(index)

    @staticmethod
    def _amount_validator(amount: str) -> bool:
        try:
            float(amount)
            return True
        except ValueError:
            return False

    @staticmethod
    def _category_validator(category: str) -> bool:
        if category not in ('Доход', 'Расход'):
            return False
        return True

    @staticmethod
    def _date_validator(date: str) -> bool:
        try:
            datetime.fromisoformat(date)
            return True
        except ValueError:
            return False

    @staticmethod
    def _index_validator(index: str) -> bool:
        df = Wallet.load_data('../wallet/finances.csv')
        max_index = df.index.max()
        return index.isdecimal() and int(index) <= max_index
