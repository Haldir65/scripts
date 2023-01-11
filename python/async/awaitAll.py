# SuperFastPython.com
# example of an asyncio mutual exclusion (mutex) lock
from random import random
import asyncio

# async def bar(i):
#   print('started', i)
#   await asyncio.sleep(1)
#   print('finished', i)

# async def main():
#   await asyncio.gather(*[bar(i) for i in range(10)])

# asyncio.run(main())
# print("\n all completed \n")



def main():
  # run the asyncio program
  asyncio.run(_main())
  pass





 
# task coroutine with a critical section
async def task(lock, num, value):
    # acquire the lock to protect the critical section
    async with lock:
        # report a message
        print(f'>coroutine {num} got the lock, sleeping for {value}')
        # block for a moment
        await asyncio.sleep(value)
 
# entry point
async def _main():
    # create a shared lock
    lock = asyncio.Lock()
    # create many concurrent coroutines
    coros = [task(lock, i, random()) for i in range(10)]
    # execute and wait for tasks to complete
    await asyncio.gather(*coros)
 


if __name__ == "__main__":
    main()




