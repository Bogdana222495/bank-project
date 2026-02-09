from src.utils import get_transactions_from_json
from src.masks import get_mask_card_number

# Тест utils
get_transactions_from_json("data/operations.json")

# Тест masks
get_mask_card_number("1234567890123456")