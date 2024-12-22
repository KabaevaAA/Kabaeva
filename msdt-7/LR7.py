import asyncio
import random


async def fetch_data(source_id):
    """Имитирует асинхронное получение данных из источника."""
    print(f"Запрос данных из источника {source_id}...")
    # Имитируем задержку на получение данных
    await asyncio.sleep(random.uniform(1, 3))
    data = f"Данные из источника {source_id}"
    print(f"Получены данные из источника {source_id}: {data}")
    return data


async def process_data(data):
    """Имитирует асинхронную обработку данных."""
    print(f"Обработка данных: {data}...")
    # Имитируем задержку на обработку данных
    await asyncio.sleep(random.uniform(1, 2))
    processed_data = f"Обработанные {data}"
    print(f"Завершена обработка данных: {processed_data}")
    return processed_data


async def main():
    """Основная функция приложения."""
    sources = [1, 2, 3, 4, 5]  # Идентификаторы источников данных
    fetch_tasks = [fetch_data(source) for source in sources]

    # Получаем данные из всех источников асинхронно
    raw_data_list = await asyncio.gather(*fetch_tasks)

    # Обрабатываем полученные данные асинхронно
    process_tasks = [process_data(data) for data in raw_data_list]
    processed_data_list = await asyncio.gather(*process_tasks)

    print("Все данные обработаны:")
    for processed_data in processed_data_list:
        print(processed_data)


# Запуск основного приложения
if __name__ == "__main__":
    asyncio.run(main())
