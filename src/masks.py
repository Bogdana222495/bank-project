import logging
from pathlib import Path


# === Настройка логера для модуля masks ===
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Обработчик: запись в файл
file_handler = logging.FileHandler(
    "logs/masks.log",
    mode="w",          # перезапись при каждом запуске
    encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

# Формат: время | модуль | уровень | сообщение
formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    try:
        if not card_number or not card_number.isdigit():
            logger.error("Неверный формат номера карты")
            return ""

        masked = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info("Номер карты успешно замаскирован")
        return masked

    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        return ""


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта."""
    try:
        if not account_number or not account_number.isdigit():
            logger.error("Неверный формат номера счёта")
            return ""

        masked = "**" + account_number[-4:]
        logger.info("Номер счёта успешно замаскирован")
        return masked

    except Exception as e:
        logger.error(f"Ошибка при маскировке счёта: {e}")
        return ""
