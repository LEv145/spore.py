# SporeApi
Spore Api


Simple example:
```py
import asyncio
from spore_api.client import SporeClient


async def main() -> None:
    async with SporeClient() as client:
        print(await client.get_creature(500267423060))


asyncio.run(main())
```
