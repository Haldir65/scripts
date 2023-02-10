import asyncio
import os
import aiohttp,httpx

headers = {
            'Accepts': 'application/json',
            'authority': "somekey",
        }

async def upload_file(f):
    url = 'http://127.0.0.1:8000/file_save'
    with open(f, 'rb') as f:
        async with aiohttp.ClientSession(headers = headers) as session:
            async with session.post(url, data={'file': f}) as response:
                res =  await response.text()
                print(res)
                return res

async def upload_via_httpx(f):
    url = 'http://127.0.0.1:8000/file_save'
    async with httpx.AsyncClient() as client:
        files = {'file': ('you_can_use_any_name_you_like.txt', open(f, 'rb'), 'text/plain; charset=UTF-8')}
        r = await client.post(url , files = files ,headers = headers)
        print(r.text)
  




if __name__ == '__main__':
    fpath = os.path.join(os.getcwd(),"sample.txt") 
    # asyncio.run(upload_file(fpath))
    asyncio.run(upload_via_httpx(fpath))