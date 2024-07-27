from src.logger_config import setup_logger

# Создание и получение именованного логгера
masks_logger = setup_logger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маскированный номер карты в формате XXXX XX** **** XXXX"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masks_logger.info(f"Masked card number: {masked_number}")
    return masked_number


def get_mask_account(account: str) -> str:
    """Возвращает маскированный номер счета в формате **XXXX"""
    masked_account = f"**{account[-4:]}"
    masks_logger.info(f"Masked account number: {masked_account}")
    return masked_account
