import logging
import pandas as pd
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import F
from dotenv import load_dotenv

load_dotenv()

TABLE_FILE_PATH = 'table.xlsx'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def load_table(file_path):
    if os.path.exists(file_path):
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, engine='openpyxl')
        elif file_path.endswith('.xls'):
            df = pd.read_excel(file_path, engine='xlrd')
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, sep=';', encoding='utf-8-sig', skipinitialspace=True)
        else:
            raise ValueError("Неподдерживаемый формат файла. Используйте .xlsx, .xls или .csv.")

        df.columns = df.columns.str.strip().str.lower()
        return df
    else:
        return pd.DataFrame()


def find_serial_number(serial_number, df):
    serial_number = str(serial_number).strip()

    result = df[df['серийный номер'].astype(str).str.strip() == serial_number]
    if not result.empty:
        # Форматируем строку: "название колонки - значение"
        formatted_result = []
        for _, row in result.iterrows():
            for col in df.columns:
                formatted_result.append(f"{col} - {row[col]}")
        return "\n".join(formatted_result)  # Объединяем строки через перенос
    else:
        return "Серийный номер не найден."


API_TOKEN = os.getenv("BOT_TOKEN")
if not API_TOKEN:
    raise ValueError("Токен бота не найден в переменных окружения. Проверьте файл .env.")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    logging.info("/start from user_id: %s", message.from_user.id)
    await message.answer("Привет! Отправь мне серийный номер, и я найду соответствующую строку в таблице. "
                         "Также ты можешь загрузить новую версию таблицы, отправив её мне как файл.")


@dp.message(F.text)
async def handle_message(message: types.Message):
    logging.info("/text from user_id: %s", message.from_user.id)
    serial_number = message.text
    df = load_table(TABLE_FILE_PATH)
    if df.empty:
        await message.answer("Таблица не загружена. Пожалуйста, загрузите таблицу.")
        return
    result = find_serial_number(serial_number, df)
    await message.answer(result, parse_mode=ParseMode.MARKDOWN)


@dp.message(F.document)
async def handle_document(message: types.Message):
    logging.info("/document from user_id: %s", message.from_user.id)
    if message.document.mime_type in [
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-excel',
        'text/csv'
    ]:
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        file_extension = os.path.splitext(file_path)[1].lower()
        new_table_path = f"table{file_extension}"

        await bot.download_file(file_path, new_table_path)
        global TABLE_FILE_PATH
        TABLE_FILE_PATH = new_table_path
        await message.answer("Таблица успешно обновлена!")
    else:
        await message.answer("Пожалуйста, загрузите файл в формате .xlsx, .xls или .csv.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    logging.info("Bot started polling")
    asyncio.run(main())