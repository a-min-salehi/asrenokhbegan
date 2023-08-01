# coroutine is a function that can suspend its execution before reaching return
import asyncio


async def main():
    task = asyncio.create_task(other())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task

async def other():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())