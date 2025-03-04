## Telegram Bot for Serial Number Lookup

Этот Telegram-бот позволяет искать информацию по серийному номеру в таблице. Пользователь может загрузить новую версию таблицы, и бот будет использовать её для поиска.

---

### Основные функции:
1. **Поиск по серийному номеру**:
   - Пользователь отправляет боту серийный номер.
   - Бот ищет строку с этим номером в таблице и возвращает информацию.

2. **Загрузка новой таблицы**:
   - Пользователь может отправить боту новый файл таблицы (в формате `.xlsx`, `.xls` или `.csv`).
   - Бот сохраняет файл и использует его для поиска.

---

### Как запустить бота

#### 1. Убедитесь, что у вас установлены:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### 2. Клонируйте репозиторий (если ещё не сделали):
```bash
git clone https://github.com/InsafMin/serial_number_bot
cd serial_number_botff
```

#### 3. Запустите бота с помощью Docker Compose:
Передайте токен бота через переменную окружения:

```bash
BOT_TOKEN=7832141370:AAGKTsMghkOzjPl7oCb8Mm01ckdNTYTZaOo docker-compose up --build
```

#### 4. Остановка бота:
Чтобы остановить бота, нажмите `Ctrl+C` в терминале или выполните:

```bash
docker-compose down
```

---

### Как использовать бота

1. **Запустите бота** (см. выше).
2. Перейдите в Telegram и найдите своего бота.
3. Отправьте команду `/start`, чтобы начать.
4. Отправьте серийный номер, чтобы получить информацию из таблицы.
5. Чтобы загрузить новую таблицу, отправьте файл в формате `.xlsx`, `.xls` или `.csv`.

---

### Пример использования

1. Пользователь отправляет боту:
   ```
   /start
   ```
   Бот отвечает:
   ```
   Привет! Отправь мне серийный номер, и я найду соответствующую строку в таблице. Также ты можешь загрузить новую версию таблицы, отправив её мне как файл.
   ```

2. Пользователь отправляет серийный номер:
   ```
   1234
   ```
   Бот отвечает:
   ```
   1234 - Some information
   ```

3. Пользователь отправляет новый файл таблицы (например, `table.xlsx`).
   Бот отвечает:
   ```
   Таблица успешно обновлена!
   ```

---

### Структура проекта

```
.
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

```

---

### Зависимости

Все зависимости указаны в файле `requirements.txt` и автоматически устанавливаются при сборке Docker-образа.

---

### Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.

---

### Контакты

Если у вас есть вопросы или предложения, свяжитесь со мной:

- **Email**: [insaf.min.in@yandex.ru](mailto:insaf.min.in@yandex.ru)
- **Telegram**: [@Insaf_Min](https://t.me/Insaf_Min)
- **GitHub**: [InsafMin](https://github.com/InsafMin)
