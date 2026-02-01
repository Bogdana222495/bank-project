import logging
import os
from datetime import datetime

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

# Создаем отдельный логер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер с нужным форматом
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
logger.addHandler(file_handler)
logger.propagate = False  # Отключаем распространение логов выше


def get_transaction_date(transaction: dict) -> str:
    """
    Извлекает и форматирует дату транзакции из словаря.
    """
    try:
        if not isinstance(transaction, dict):
            raise TypeError("Транзакция должна быть словарем")

        date_str = transaction.get("date")
        if not date_str:
            raise KeyError("В транзакции отсутствует поле 'date'")

        # Парсим дату (пример формата: "2023-12-15T15:30:45")
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y")
        logger.debug(f"Успешное извлечение даты: {date_str} -> {formatted_date}")
        return formatted_date

    except Exception as e:
        logger.error(f"Ошибка при извлечении даты из транзакции: {str(e)}")
        raise


def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует транзакции по статусу.
    """
    try:
        if not isinstance(transactions, list):
            raise TypeError("Транзакции должны быть списком")

        filtered = [t for t in transactions if t.get("state") == state]
        logger.debug(f"Успешная фильтрация: {len(transactions)} транзакций -> {len(filtered)} с состоянием {state}")
        return filtered

    except Exception as e:
        logger.error(f"Ошибка при фильтрации транзакций: {str(e)}")
        raise