from src.masks import get_mask_card_number, get_mask_account
from src.utils import get_transaction_date, filter_by_state


def main():
    # Пример использования маскировки
    card = "1234567890123456"
    account = "12345678901234567890"

    print("Маскировка карты:", get_mask_card_number(card))
    print("Маскировка счета:", get_mask_account(account))

    # Пример использования утилит
    transaction = {
        "id": 1,
        "date": "2023-12-15T15:30:45",
        "state": "EXECUTED",
        "amount": "1000"
    }

    print("Дата транзакции:", get_transaction_date(transaction))

    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"}
    ]

    executed = filter_by_state(transactions)
    print(f"Найдено {len(executed)} выполненных транзакций")


if __name__ == "__main__":
    main()