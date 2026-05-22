"""
TRAWA Telegram Bot · analytics.py
Запись событий в Google Таблицу через gspread.
Если Google Sheets не настроены — fallback в файл analytics_log.txt.

Настройка Google Sheets:
1. Создай сервисный аккаунт в Google Cloud Console
2. Скачай JSON с ключами, положи рядом с ботом
3. Добавь в .env: GOOGLE_CREDENTIALS_FILE=credentials.json
4. Добавь в .env: GOOGLE_SHEET_ID=<id таблицы из URL>
5. Дай сервисному аккаунту доступ «Редактор» к таблице
"""

import csv
import datetime
import logging
import os

logger = logging.getLogger(__name__)

# Глобальные объекты подключения к Google Sheets
_sheet = None


def _init_gspread() -> bool:
    """Попытка подключиться к Google Sheets. Возвращает True при успехе."""
    global _sheet
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        creds_file = os.getenv("GOOGLE_CREDENTIALS_FILE", "")
        sheet_id   = os.getenv("GOOGLE_SHEET_ID", "")

        if not creds_file or not sheet_id:
            logger.info("Google Sheets: переменные окружения не заданы, используем лог-файл")
            return False

        scopes = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        creds  = Credentials.from_service_account_file(creds_file, scopes=scopes)
        gc     = gspread.authorize(creds)
        _sheet = gc.open_by_key(sheet_id).sheet1

        # Добавляем заголовки, если таблица пустая
        if not _sheet.row_values(1):
            _sheet.append_row(
                ["timestamp", "user_id", "event", "theme", "category", "product"]
            )

        logger.info("Google Sheets: подключение успешно")
        return True

    except ImportError:
        logger.info("gspread не установлен — используем лог-файл")
    except Exception as exc:
        logger.warning(f"Google Sheets: ошибка подключения — {exc}")

    return False


# Инициализируем при импорте модуля
_gspread_ready = _init_gspread()


def log_event(
    user_id: int,
    event: str,
    theme: str = "",
    category: str = "",
    product: str = "",
) -> None:
    """
    Записать одно событие.

    Параметры
    ---------
    user_id   : Telegram ID пользователя
    event     : start | theme_select | category_select | card_view | buy_click
    theme     : выбранная тема (Масла, Косметика …)
    category  : ключ категории (women_oils, digestion …)
    product   : название продукта
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, str(user_id), event, theme, category, product]

    # 1. Попытка записать в Google Sheets
    if _gspread_ready and _sheet:
        try:
            _sheet.append_row(row)
            return
        except Exception as exc:
            logger.warning(f"Google Sheets: ошибка записи строки — {exc}")

    # 2. Fallback: запись в текстовый файл
    try:
        with open("analytics_log.txt", "a", encoding="utf-8") as f:
            f.write("\t".join(row) + "\n")
    except Exception as exc:
        logger.error(f"Аналитика: не удалось записать в файл — {exc}")


CONTACTS_FILE = "contacts.csv"
CONTACTS_FIELDS = ["date", "user_id", "username", "first_name", "last_name"]

CONSENT_FILE   = "consent.csv"
CONSENT_FIELDS = ["date", "user_id", "consent_given"]


def has_seen_consent(user_id: int) -> bool:
    """Возвращает True, если пользователь уже видел экран согласия (любой ответ)."""
    if not os.path.isfile(CONSENT_FILE):
        return False
    try:
        with open(CONSENT_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("user_id") == str(user_id):
                    return True
    except Exception as exc:
        logger.warning(f"Согласие: ошибка чтения — {exc}")
    return False


def save_consent(user_id: int, given: bool) -> None:
    """Сохраняет решение пользователя о согласии на обработку персональных данных."""
    try:
        file_exists = os.path.isfile(CONSENT_FILE)
        with open(CONSENT_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CONSENT_FIELDS)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "date":          datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "user_id":       str(user_id),
                "consent_given": "yes" if given else "no",
            })
    except Exception as exc:
        logger.error(f"Согласие: не удалось сохранить — {exc}")


def save_contact(user) -> None:
    """
    Сохраняет контакт пользователя в contacts.csv при каждом /start.
    Дубли по user_id не перезаписывают существующие строки —
    каждый визит добавляется новой строкой с датой.
    """
    try:
        file_exists = os.path.isfile(CONTACTS_FILE)
        with open(CONTACTS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CONTACTS_FIELDS)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "date":       datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "user_id":    user.id,
                "username":   f"@{user.username}" if user.username else "",
                "first_name": user.first_name or "",
                "last_name":  user.last_name or "",
            })
    except Exception as exc:
        logger.error(f"Контакты: не удалось сохранить — {exc}")
