# Async IO in python 

# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O oprations in a concurrent and nun-blocking manner. In python, async programming is a achieved through the user of the asyncio module and asynchronous functions.


import asyncio
import time

# async def function1():
#     await asyncio.sleep(1)
#     print("func1")
#     return "Parht"

# async def function2():
#     await asyncio.sleep(1)
#     print("func2")

# async def function3():
#     await asyncio.sleep(4)
#     print("func3")

# async def main():
#     L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#     print(L)

# #     task = asyncio.create_task(function1())
# #     # await function1()
# #     await function2()
# #     await function3()

# asyncio.run(main())


print("--------------------------------------------------")

import requests


async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("CodeWithHarry/96_instagram1.ico", "wb").write(response.content)
    print("func1")
    return "Parht"

async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("CodeWithHarry/96_instagram2.ico", "wb").write(response.content)
    print("func2")

async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("CodeWithHarry/96_instagram3.ico", "wb").write(response.content)
    print("func3")

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()

asyncio.run(main())




