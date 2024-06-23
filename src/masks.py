def get_mask_card_number(card_number: str) -> str:
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Возвращает маскированный номер счета в формате **XXXX"""
    return f"**{account[-4:]}"
