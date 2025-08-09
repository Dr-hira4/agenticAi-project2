#synchronous example:

import time

#step 1:
print("water boils....")
time.sleep(5)
print("water boiled.")

#step 2:
print("food is cooking....")
time.sleep(3)
print("food has cooked.")


#async example

import asyncio

async def pani_ubalo():
    print("pani ubalna shuru....")
    await asyncio.sleep(5)
    print("pani ubal gaya")

async def roti_banao():
    print("Roti banana shuru....")
    await asyncio.sleep(3)
    print("roti ban gayi.")

async def main():
    await asyncio.gather(
        pani_ubalo(),
        roti_banao()
    )

asyncio.run(main())