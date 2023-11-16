"""
Модуль со всеми сервисами для магазина "4 лапы"
"""
import aiofiles
import json

from .repository import ScriptRepository

from config import URL


class ScriptService:
    """ Выполняет выборку данных и сохранение в файл """
    def __init__(self):
        self.repo = ScriptRepository()

    async def __save(self, products: list):
        """ Сохраняет данных в файл """
        async with aiofiles.open('products.json', mode='w') as f:
            await f.write(json.dumps(products))

    def _convert_json(self, data: list) -> list:
        """ Выбирает из сырых данных нужное """
        products = []
        if data is None:
            print("Получены пустые данные")
            exit()
        for product in data:
            json_product = {
                "id": product["ItemId"],
                "name": product["Name"],
                "url": product["Url"],
                "price": product["Price"],
                "oldPrice": product["OldPrice"],
                "vendor": product["Vendor"]
            }
            products.append(json_product)
        return products

    async def parse_data(self):
        """ Забирает сырые данные и отправляет их обрабатываться """
        print("Получение данных...")
        raw_data: list = await self.repo.get_products(URL)
        print("Конвертация данных...")
        products: list = self._convert_json(raw_data)
        print("Сохранение в файл...")
        await self.__save(products)
