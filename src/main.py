"""
Главный модуль
"""
import asyncio

from script.service import ScriptService


async def main():
    service = ScriptService()
    print("Старт")
    await service.parse_data()
    print("Финиш!")


if __name__ == "__main__":
    asyncio.run(main())
