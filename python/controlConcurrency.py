import asyncio
import aiohttp
import aiofiles

CONCURRENCY = 5
URL = 'https://www.zhihu.com'

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
##Don’t create a session per request. Most likely you need a session per application which performs all requests altogether.

async def scrape_api():
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            content =  await response.text()
            async with aiofiles.open('content.html', mode='w') as f:
                await f.write(content)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(6)]
    await asyncio.gather(*scrape_index_tasks)
    await session.close()

## https://cuiqingcai.com/202272.html
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main()) 