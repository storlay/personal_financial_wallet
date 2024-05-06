import pandas as pd


class Wallet:
    @classmethod
    def load_data(
            cls,
            file_path: str
    ) -> pd.DataFrame:
        """
        Функция для загрузки данных из файла
        :param file_path: путь к файлу
        :return: датафрейм
        """
        try:
            data = pd.read_csv(file_path, sep='|')
            return data
        except FileNotFoundError:
            print('Файл не найден. Создайте новый файл или укажите правильный путь к существующему файлу.')
            return pd.DataFrame(columns=['Дата', 'Категория', 'Сумма', 'Описание'])

    @classmethod
    def save_data(
            cls,
            data: pd.DataFrame,
            file_path: str
    ) -> None:
        """
        Функция для сохранения данных в файл
        :param data: датафрейм с данными
        :param file_path: путь к файлу
        """
        data.to_csv(file_path, sep='|', index=False)

    @classmethod
    def show_balance(
            cls,
            data: pd.DataFrame
    ) -> None:
        """
        Функция для вывода баланса
        :param data: датафрейм с данными
        """
        income = data[data['Категория'] == 'Доход']['Сумма'].sum()
        expenses = data[data['Категория'] == 'Расход']['Сумма'].sum()
        balance = income - expenses
        print(f'Текущий баланс: {balance}')
        print(f'Доходы: {income}')
        print(f'Расходы: {expenses}')

    @classmethod
    def add_record(
            cls,
            data,
            transaction_date: str,
            category: str,
            amount: float,
            description: str
    ) -> pd.DataFrame:
        """
        Функция для добавления записи
        :param data: датафрейм с данными
        :param transaction_date: дата записи
        :param category: категория (Доход/Расход)
        :param amount: сумма
        :param description: описание
        :return: обновленный датафрейм с данными
        """
        new_record = pd.DataFrame([[transaction_date, category, amount, description]], columns=data.columns)
        data = pd.concat([data, new_record])
        return data

    @classmethod
    def edit_record(
            cls,
            data: pd.DataFrame,
            index: int,
            transaction_date: str,
            category: str,
            amount: float,
            description: str
    ) -> pd.DataFrame:
        """
        Функция для редактирования записи
        :param data: датафрейм с данными
        :param index: индекс записи для редактирования
        :param transaction_date: новая дата записи
        :param category: новая категория (Доход/Расход)
        :param amount: новая сумма
        :param description: новое описание
        :return: обновленный датафрейм с данными
        """
        data.loc[index] = [transaction_date, category, amount, description]
        return data

    @classmethod
    def search_records(
            cls,
            data: pd.DataFrame = None,
            category: str = None,
            transaction_date: str = None,
            amount: str = None
    ) -> pd.DataFrame | str:
        """
        Функция для поиска записей
        :param data: датафрейм с данными
        :param category: категория для поиска (Доход/Расход)
        :param transaction_date: дата для поиска (гггг-мм-дд)
        :param amount: сумма для поиска
        """
        if all((transaction_date is None, category is None, amount is None)):
            return 'Введите хотя бы один параметр для поиска.'

        filters = {'Категория': category, 'Дата': transaction_date, 'Сумма': amount}
        query = ' & '.join(
            f'{col} == "{value}"'
            for col, value in filters.items()
            if value not in ('', None)
        )
        result = data.query(query)

        if len(result):
            return result
        return '\nСовпадений не найдено'
