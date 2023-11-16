"""
Модуль получения данных с серверов с помощью запросов.
"""
import aiohttp


class ScriptRepository:
    """ Получает данные для магазина "4 лапы" """

    def __init__(self):
        self.ai_session: aiohttp.ClientSession = aiohttp.ClientSession()

    async def get_products(self, url: str) -> list:
        """ Получает данные и форматирует в json формат """
        async with self.ai_session as session:
            try:
                # Открытие запроса
                async with session.get(url) as response:
                    if response.status != 200:
                        print(f"Не удалось получить данные, ошибка{response.status}")
                        exit()
                    # Получение тела в формате json
                    products = await response.json()
                    return products
            except Exception as e:
                print(e)
                exit()
