import pandas as pd

from app.service import Wallet


def test_add_record(sample_data: pd.DataFrame):
    new_data = Wallet.add_record(
        sample_data,
        '2024-05-04',
        'Доход',
        10000,
        'Подарок'
    )
    assert len(new_data) == len(sample_data) + 1


def test_edit_record(sample_data):
    edited_data = Wallet.edit_record(
        sample_data,
        1,
        '2024-05-02',
        'Расход',
        20000,
        'Покупка мебели'
    )
    assert edited_data.iloc[1]['Сумма'] == 20000


def test_search_records(sample_data):
    result = Wallet.search_records(
        sample_data,
        category='Расход'
    )
    assert len(result) == 2
    assert result.iloc[0]['Сумма'] == 20000
    assert result.iloc[1]['Сумма'] == 2000
