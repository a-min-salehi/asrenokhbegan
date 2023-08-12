# coroutine is a function that can suspend its execution before reaching return
import asyncio


async def main():
    task = asyncio.create_task(other())
    task2 = asyncio.create_task(others())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task2
    print("C")
    await task


async def other():
    print("1")
    await asyncio.sleep(2)
    print("2")


async def others():
    print("3")
    await asyncio.sleep(2)
    print("4")


asyncio.run(main())
