# stock.py
# Проверка наличия товара

def is_available(item_name: str) -> bool:
    """Возвращает True, если товар в наличии"""
    stock = {
        "Вакцина для собак": True,
        "Ошейник": True,
        "Лекарство от блох": False,
        "Корм для кошек": True
    }
    return stock.get(item_name, False)
