import logging
import os

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

# Создаем отдельный логер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер с нужным форматом
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
logger.addHandler(file_handler)
logger.propagate = False  # Отключаем распространение логов выше


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: оставляет первые 6 и последние 4 цифры,
    остальные заменяет на звездочки.
    """
    try:
        # Удаляем пробелы и проверяем длину
        cleaned = card_number.replace(" ", "")
        if not cleaned.isdigit():
            raise ValueError("Номер карты должен содержать только цифры")
        if len(cleaned) != 16:
            raise ValueError(f"Неверная длина номера карты: {len(cleaned)} (ожидается 16)")

        masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"
        logger.debug(f"Успешная маскировка карты: {card_number} -> {masked}")
        return masked

    except Exception as e:
        logger.error(f"Ошибка при маскировке карты {card_number}: {str(e)}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета: оставляет последние 4 цифры,
    остальные заменяет на звездочки.
    """
    try:
        cleaned = account_number.replace(" ", "")
        if not cleaned.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        if len(cleaned) < 4:
            raise ValueError(f"Слишком короткий номер счета: {len(cleaned)}")

        masked = f"**{cleaned[-4:]}"
        logger.debug(f"Успешная маскировка счета: {account_number} -> {masked}")
        return masked

    except Exception as e:
        logger.error(f"Ошибка при маскировке счета {account_number}: {str(e)}")
        raise
# Логирование маскировки карт и счетов (домашнее задание)