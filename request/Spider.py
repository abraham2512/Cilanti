from requests import get, post
from threading import Thread
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
from links import Links
import hashlib
import Cilanticonfig

request_method={
    'get' : get,
    'post': post,
}

class Spider:

    def __init__(self):
        self.threadPool = ThreadPool(Cilanticonfig.MAX_THREAD)
        self.initial_url=set(['https://stackoverflow.com','https://en.wikipedia.org/'])
        self.hash_value=set([])

    def spi_request(self, method, *args, **kwargs):
        '''used to get the request pages async
        '''
        method= request_method[method]
        self.threadPool.apply_async(method, args=args, kwds=kwargs, callback=self.spi_response)


    def spi_response(self, response, *args, **kwargs):
        '''Response of the spi_request are handled here
        '''
        if 'text/html' in response.headers['Content-Type']:
            hash_val= self.HashMD5(response.content)
            if hash_val not in self.hash_value:
                self.hash_value.add(hash_val)
                self.initial_url.union(Links.parse_link(response))

    def HashMD5(self, content):
        hashMD5=hashlib.md5()
        hashMD5.update(content)
        return hashMD5.hexdigest()
