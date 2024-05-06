import pandas as pd
import pytest


@pytest.fixture(scope='session', autouse=True)
def sample_data():
    data = pd.DataFrame([
        ['2024-05-01', 'Доход', 100000, 'Зарплата'],
        ['2024-05-02', 'Расход', 5000, 'Покупка продуктов'],
        ['2024-05-03', 'Расход', 2000, 'Кафе']
    ], columns=['Дата', 'Категория', 'Сумма', 'Описание'])
    return data
