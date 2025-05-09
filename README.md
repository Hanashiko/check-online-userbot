# 📡 Check Online Telegram Userbot

Цей проєкт — це Telegram-юзербот, написаний на Python з використанням бібліотеки **Telethon**, що дозволяє відстежувати, коли вказаний користувач з’являється онлайн або виходить з мережі. Бот надсилає повідомлення про зміну статусу в заданий чат (лог-чат).

## 🔧 Файли проєкту

- `main.py` — основний код юзербота.
- `requirements.txt` — список залежностей.
- `.env` — файл конфігурації з особистими змінними середовища.
- `.env.example` — приклад файлу `.env`, без конфіденційних даних.
- `.gitignore` — файл для виключення файлів із git-репозиторію.

## 📂 Встановлення та запуск

### 1. Клонування репозиторію

```bash
git clone https://github.com/hanashiko/check-online-userbot.git
cd check-online-userbot
```

### 2. Створення віртуального оточення (рекомендовано)

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

### 3. Встановлення залежностей

```bash
pip install -r requirements.txt
```

### 4. Налаштування змінних середовища

Створіть файл `.env` на основі `.env.example`:

```bash
cp .env.example .env
```

Заповніть `.env` своїми значеннями:

```env
API_ID=your_api_id
API_HASH=your_api_hash
SESSION_NAME=your_session_name
USER_ID_TO_TRACK=123456789  # ID користувача, якого відстежуємо
LOG_CHAT_ID=-1001234567890  # ID чату/групи/каналу, куди слати повідомлення
```

> ✅ Для отримання `API_ID` і `API_HASH`, зареєструйте додаток на [my.telegram.org](https://my.telegram.org).

### 5. Запуск бота

```bash
python main.py
```

Після запуску бот:
- одразу перевіряє статус цільового користувача,
- надалі слідкує за оновленням його статусу в реальному часі.

## 🧠 Як це працює

- Завдяки Telethon, бот авторизується як звичайний користувач Telegram.
- При запуску бот виконує первинну перевірку онлайн/офлайн статусу.
- Через обробник подій `UserUpdate`, бот слухає зміну статусу користувача.
- Кожна зміна статусу логиться в чат у вигляді повідомлення.
