import httpx
import asyncio

async def ht2():
    async with httpx.AsyncClient(http2= True) as client:
        r = await client.get('https://www.zhihu.com/')
        r2 = await client.get('https://www.taobao.com/')
        print(r.http_version) 
        print('\n')
        print(r2.http_version) 




if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(ht2())

