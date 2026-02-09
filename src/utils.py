import json
from pathlib import Path
from typing import List, Dict, Any
import logging


# === Настройка логера для модуля utils ===
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    "logs/utils.log",
    mode="w",
    encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_transactions_from_json(file_path: str) \
        -> List[Dict[str, Any]]:

    """
    Считывает список транзакций из JSON-файла.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            logger.error(f"Файл не найден: {file_path}")
            return []

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            logger.info(f"Успешно прочитано {len(data)} транзакций из {file_path}")
            return data
        else:
            logger.error(f"Данные в файле не являются списком: {file_path}")
            return []

    except (json.JSONDecodeError, IOError, ValueError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []
