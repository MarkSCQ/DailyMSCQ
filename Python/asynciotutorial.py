import asyncio


async def task1():
    print("Send first email")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("First Email reply")


async def task2():
    print("Send second email")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("Second Email reply")


async def task3():
    print("Send third email")
    await asyncio.sleep(1)
    print("Third Email reply")


# asyncio.run(task1())


async def TASK1():
    print("TASK1 Start")
    await asyncio.sleep(1)
    print("TASK1 End")
    return "TASK1"


async def t1():
    await t2()
    print("T1")


async def t2():
    print("T2")


async def t3():
    await t1()
    print("T3")


async def tm():
    await asyncio.create_task(t3())

# asyncio.run(tm())


async def fetch_data():
    print("fetching data")
    await asyncio.sleep(2)
    print("data returned")
    return "DATA"


async def iteration():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def pmain():
    t1 = asyncio.create_task(fetch_data())
    t2 = asyncio.create_task(iteration())

    data = await t1
    print(data)
    await t2
    # await t2
asyncio.run(pmain())
