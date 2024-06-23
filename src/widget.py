from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_inform: str) -> str:
    """
    - Принимает на вход строку с информацией — тип карты/счета и номер карты/счета
    - Возвращает исходную строку с замаскированным номером карты/счета
    """

    # Получение типа и номера карты/счета
    card_or_account_type, card_or_account_num = card_or_account_inform.rsplit(" ", 1)

    if card_or_account_type.lower() in ("счет", "счёт"):
        return f"{card_or_account_type} {get_mask_account(card_or_account_num)}"
    else:
        return f"{card_or_account_type} {get_mask_card_number(card_or_account_num)}"


def get_data(date_of_transaction: str) -> str:
    """
    - Принимает на вход строку вида  2018-07-11T02:26:18.671407
    - Возвращает строку с датой в виде  11.07.2018
    """

    # Получение даты и времени
    date, _ = date_of_transaction.split("T")
    # Получение списка, элементами которого являются yy, mm, dd
    date_list = date.split("-")

    return f"{date_list[2]}.{date_list[1]}.{date_list[0]}"
