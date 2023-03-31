import httpx
import asyncio
import aiofiles,shutil,os
import tempfile
from urllib.parse import urlparse
# from urlparse import urlparse  # Python 2


async def ht2():
    async with httpx.AsyncClient(http2= True) as client:
        r = await client.get('https://www.zhihu.com/')
        r2 = await client.get('https://www.taobao.com/')
        print(r.http_version) 
        print('\n')
        print(r2.http_version) 


async def download_file_to_temp_file(url):
    async with httpx.AsyncClient(http2= True) as client:
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-encoding':'gzip, deflate, br','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        r = await client.get(url,headers= headers)
        fd, path = tempfile.mkstemp()
        print("temp path is {0}\n".format(path))
        os.write(fd, r.content)
        os.close(fd)
        parsed_uri = urlparse(url = url)
        dest =  os.path.join(os.getcwd(),parsed_uri.netloc.split('.')[1]+'.html') 
        print(parsed_uri.netloc)
        shutil.copy(path, dest)
        os.remove(path)
        # print(r.http_version) 
        # print('\n')
        # print(r2.http_version) 
        


async def multiple_tasks():
    urls = ['https://www.taobao.com/','https://www.tmall.com/']
    coros = [download_file_to_temp_file(i) for i in urls]
    res = await asyncio.gather(*coros, return_exceptions=True)
    return res


if __name__ == '__main__':
    # res = await asyncio.gather(*coros, return_exceptions=True)
    # asyncio.get_event_loop().run_until_complete(ht2())
    asyncio.get_event_loop().run_until_complete(multiple_tasks())


