"""
TRAWA Telegram Bot · keyboards.py
Все клавиатуры бота собраны здесь.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка «Вернуться в начало» — используется на каждом экране
BACK_BTN = InlineKeyboardButton(
    text="← Вернуться в начало",
    callback_data="menu:main"
)


def main_menu() -> InlineKeyboardMarkup:
    """Главное меню — уровень 1."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌟 Хиты продаж",           callback_data="cat:hits:0")],
        [InlineKeyboardButton(text="🫚 Масла",               callback_data="menu:oils")],
        [InlineKeyboardButton(text="🥗 Деликатесы и суперфуды", callback_data="menu:food")],
        [InlineKeyboardButton(text="🌿 Пищеварение",          callback_data="cat:digestion:0")],
        [InlineKeyboardButton(text="🧁 Для выпечки",          callback_data="cat:baking:0")],
        [InlineKeyboardButton(text="🍫 Десерты без сахара",   callback_data="cat:desserts:0")],
        [InlineKeyboardButton(text="🌸 Косметика",            callback_data="cat:cosmetics:0")],
        [InlineKeyboardButton(text="🔥 Акции",                callback_data="cat:promotions:0")],
        [InlineKeyboardButton(text="🌻 Дачный сезон",         callback_data="special:dacha")],
    ])


def oils_menu() -> InlineKeyboardMarkup:
    """Подменю масел — уровень 2."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👩 Масла для женщин",  callback_data="cat:women_oils:0")],
        [InlineKeyboardButton(text="👨 Масла для мужчин",  callback_data="cat:men_oils:0")],
        [InlineKeyboardButton(text="👶 Масла для детей",   callback_data="cat:children_oils:0")],
        [InlineKeyboardButton(text="🍳 Масла для жарки",   callback_data="cat:frying:0")],
        [BACK_BTN],
    ])


def food_menu() -> InlineKeyboardMarkup:
    """Подменю «Деликатесы и суперфуды» — уровень 2."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🧄 Деликатесы и соусы", callback_data="cat:delicacies:0")],
        [InlineKeyboardButton(text="🌾 Клетчатка и мука",   callback_data="cat:fiber:0")],
        [BACK_BTN],
    ])


def card_keyboard(category: str, next_index: int, url: str, total: int) -> InlineKeyboardMarkup:
    """
    Кнопки под карточкой товара.
    Кнопка «Показать другой вариант» скрывается, если продукт только один.
    """
    rows = [
        [InlineKeyboardButton(text="🛒 Купить на сайте →", url=url)],
    ]
    # Показываем «другой вариант» только если продуктов больше одного
    if total > 1:
        rows.append([
            InlineKeyboardButton(
                text="🔄 Показать другой вариант",
                callback_data=f"cat:{category}:{next_index}",
            )
        ])
    rows.append([BACK_BTN])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def dacha_keyboard(url: str) -> InlineKeyboardMarkup:
    """Кнопки для раздела «Дачный сезон»."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌻 Перейти на сайт →", url=url)],
        [BACK_BTN],
    ])
