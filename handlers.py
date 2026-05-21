"""
TRAWA Telegram Bot · handlers.py
Все обработчики сообщений и нажатий кнопок.
"""

import json
import logging
import os

import aiohttp
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import BufferedInputFile, CallbackQuery, FSInputFile, InputMediaPhoto, Message

from analytics import log_event, save_contact
from content import (
    CATEGORY_THEME,
    DACHA_TEXT,
    DACHA_URL,
    FRYING_WARNING,
    NO_PROMOTIONS_TEXT,
    PRODUCTS,
    WELCOME_TEXT,
)
from keyboards import card_keyboard, dacha_keyboard, food_menu, main_menu, oils_menu

logger = logging.getLogger(__name__)
router = Router()


# ─── FSM: хранение контекста пользователя ────────────────────────────────────

class UserState(StatesGroup):
    browsing = State()  # Пользователь листает каталог


# ─── Вспомогательные функции ─────────────────────────────────────────────────

def format_card_text(product: dict) -> str:
    """Форматирует текст карточки товара по шаблону из ТЗ."""
    partner_suffix = " <i>(от партнёров)</i>" if product.get("is_partner") else ""
    name     = f"🌿 <b>{product['name']}</b>{partner_suffix}"
    benefits = "\n".join(f"✅ {b}" for b in product["benefits"])
    return f"{name}\n\n{benefits}"


def load_promotions() -> list[dict]:
    """
    Загружает акции из content_dynamic.json при каждом обращении —
    без перезапуска бота. Возвращает пустой список при ошибке.
    """
    try:
        with open("content_dynamic.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("акции", [])
    except FileNotFoundError:
        logger.warning("content_dynamic.json не найден")
    except json.JSONDecodeError as exc:
        logger.error(f"Ошибка парсинга content_dynamic.json: {exc}")
    return []


async def fetch_photo(url: str) -> BufferedInputFile | None:
    """Скачивает фото с сервера и возвращает как файл для Telegram."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    data = await resp.read()
                    ext = "jpg" if url.lower().endswith(".jpg") else "png"
                    return BufferedInputFile(data, filename=f"photo.{ext}")
    except Exception as e:
        logger.warning(f"Не удалось скачать фото ({url[:60]}…): {e}")
    return None


async def show_text_screen(callback: CallbackQuery, text: str, keyboard) -> None:
    """
    Показывает текстовый экран (меню или простое сообщение).
    Если текущее сообщение — фото, отправляем новое, иначе редактируем.
    """
    if callback.message.photo:
        await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")
    else:
        try:
            await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        except Exception:
            # На случай если текст не изменился
            await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")


async def show_card(callback: CallbackQuery, product: dict, keyboard) -> None:
    """
    Показывает карточку товара (с фото или без).
    Бот сам скачивает фото и отправляет в Telegram напрямую.
    Если фото не загрузилось — показывает карточку текстом (без краша).
    """
    text      = format_card_text(product)
    photo_url = product.get("photo_url", "")

    if photo_url:
        photo_file = await fetch_photo(photo_url)
        if photo_file:
            try:
                if callback.message.photo:
                    await callback.message.edit_media(
                        media=InputMediaPhoto(media=photo_file, caption=text, parse_mode="HTML"),
                        reply_markup=keyboard,
                    )
                else:
                    await callback.message.answer_photo(
                        photo=photo_file,
                        caption=text,
                        reply_markup=keyboard,
                        parse_mode="HTML",
                    )
                return  # фото отправлено — выходим
            except Exception as e:
                logger.warning(f"Ошибка при отправке фото ({photo_url[:60]}…): {e}. Показываю текст.")

    # Фото нет или не загрузилось — показываем текстом
    if callback.message.photo:
        await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")
    else:
        try:
            await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        except Exception:
            await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")


# ─── Команда /start ───────────────────────────────────────────────────────────

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """Приветствие и главное меню."""
    await state.set_state(UserState.browsing)
    await state.update_data(theme="", category="", product="")
    save_contact(message.from_user)          # сохраняем контакт
    log_event(message.from_user.id, "start")
    await message.answer(WELCOME_TEXT, reply_markup=main_menu(), parse_mode="HTML")


# ─── Команда /contacts (только для администратора) ────────────────────────────

@router.message(Command("contacts"))
async def cmd_contacts(message: Message) -> None:
    """Отправляет администратору файл contacts.csv со всеми контактами."""
    admin_id = int(os.getenv("ADMIN_ID", "0"))
    if message.from_user.id != admin_id:
        return  # молча игнорируем запрос от не-администратора

    if not os.path.isfile("contacts.csv"):
        await message.answer("Контактов пока нет — никто не запускал бота.")
        return

    await message.answer_document(
        FSInputFile("contacts.csv"),
        caption="📋 Все пользователи, запускавшие бота.",
    )


# ─── Главное меню (кнопка «← Вернуться в начало») ────────────────────────────

@router.callback_query(F.data == "menu:main")
async def cb_main_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """Возврат на главный экран."""
    await state.update_data(theme="", category="", product="")
    log_event(callback.from_user.id, "start")
    await show_text_screen(callback, WELCOME_TEXT, main_menu())
    await callback.answer()


# ─── Подменю «Масла» ──────────────────────────────────────────────────────────

@router.callback_query(F.data == "menu:oils")
async def cb_oils_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """Показывает подменю масел."""
    await state.update_data(theme="Масла")
    log_event(callback.from_user.id, "theme_select", theme="Масла")
    await show_text_screen(callback, "🥜 <b>Масла</b>\n\nВыберите категорию:", oils_menu())
    await callback.answer()


# ─── Подменю «Еда и суперфуды» ───────────────────────────────────────────────

@router.callback_query(F.data == "menu:food")
async def cb_food_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """Показывает подменю еды и суперфудов."""
    await state.update_data(theme="Деликатесы и суперфуды")
    log_event(callback.from_user.id, "theme_select", theme="Деликатесы и суперфуды")
    await show_text_screen(callback, "🥗 <b>Деликатесы и суперфуды</b>\n\nВыберите категорию:", food_menu())
    await callback.answer()


# ─── Раздел «Дачный сезон» ───────────────────────────────────────────────────

@router.callback_query(F.data == "special:dacha")
async def cb_dacha(callback: CallbackQuery, state: FSMContext) -> None:
    """Показывает раздел «Дачный сезон» с кнопкой-ссылкой на сайт."""
    log_event(callback.from_user.id, "theme_select", theme="Дачный сезон")
    await show_text_screen(callback, DACHA_TEXT, dacha_keyboard(DACHA_URL))
    await callback.answer()


# ─── Карточки товаров ─────────────────────────────────────────────────────────

@router.callback_query(F.data.startswith("cat:"))
async def cb_category(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Универсальный обработчик для всех категорий товаров.
    Формат callback_data: cat:{category}:{index}
    """
    parts = callback.data.split(":")
    category  = parts[1]
    raw_index = int(parts[2])

    # ── Раздел «Акции» — загружается из JSON ─────────────────────────────────
    if category == "promotions":
        promotions = load_promotions()
        if not promotions:
            await show_text_screen(callback, NO_PROMOTIONS_TEXT, main_menu())
            await callback.answer()
            return

        index    = raw_index % len(promotions)
        promo    = promotions[index]
        promo_url = promo.get("url", "https://trawaoil.ru")
        keyboard = card_keyboard("promotions", index + 1, promo_url, len(promotions))

        # Формат карточки акции (нет benefits — только name + description)
        text = (
            f"🌿 <b>{promo['name']}</b>\n\n"
            f"💬 <i>{promo.get('description', '')}</i>"
        )
        photo_url = promo.get("photo_url", "")

        log_event(callback.from_user.id, "card_view",
                  theme="Акции", category="promotions", product=promo["name"])

        # Показываем карточку акции
        if photo_url:
            photo_file = await fetch_photo(photo_url)
            if photo_file:
                try:
                    if callback.message.photo:
                        await callback.message.edit_media(
                            media=InputMediaPhoto(media=photo_file, caption=text, parse_mode="HTML"),
                            reply_markup=keyboard,
                        )
                    else:
                        await callback.message.answer_photo(
                            photo=photo_file, caption=text,
                            reply_markup=keyboard, parse_mode="HTML",
                        )
                    await callback.answer()
                    return
                except Exception as e:
                    logger.warning(f"Ошибка при отправке фото акции: {e}. Показываю текст.")

        if callback.message.photo:
            await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")
        else:
            try:
                await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
            except Exception:
                await callback.message.answer(text, reply_markup=keyboard, parse_mode="HTML")

        await callback.answer()
        return

    # ── Обычные категории ────────────────────────────────────────────────────
    products = PRODUCTS.get(category, [])
    if not products:
        await callback.answer("Раздел в разработке 🛠", show_alert=True)
        return

    index    = raw_index % len(products)
    product  = products[index]
    theme    = CATEGORY_THEME.get(category, "")
    next_idx = (index + 1) % len(products)
    keyboard = card_keyboard(category, next_idx, product["url"], len(products))

    # Аналитика
    await state.update_data(theme=theme, category=category, product=product["name"])
    log_event(
        callback.from_user.id, "card_view",
        theme=theme, category=category, product=product["name"],
    )

    # ── Специальное предупреждение для «Масел для жарки» (только первая карточка)
    if category == "frying" and index == 0:
        await callback.message.answer(FRYING_WARNING, parse_mode="HTML")

    # Показываем карточку
    await show_card(callback, product, keyboard)
    await callback.answer()
