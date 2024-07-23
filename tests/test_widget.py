import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("card_or_account_inform, expected", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 1596837868705199", "Visa Classic 1596 83** **** 5199"),
    ("Visa Platinum Miles 1596837868705199", "Visa Platinum Miles 1596 83** **** 5199"),
    ("Visa Platinum Credit Card 8990922113665229", "Visa Platinum Credit Card 8990 92** **** 5229"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счёт 35383033474447895560", "Счёт **5560")
])
def test_mask_account_card(card_or_account_inform, expected):
    assert mask_account_card(card_or_account_inform) == expected


def test_get_data(ISO_8601):
    assert get_data("2018-07-11T02:26:18.671407") == ISO_8601
