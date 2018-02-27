from requests import get, post
from threading import Thread
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
import Cilanticonfig

request_method={
    'get' : get,
    'post': post,
}
#link=Links()
class Spider:
    def __init__(self):
        self.threadPool = ThreadPool(Cilanticonfig.MAX_THREAD)

    def spi_request(self, method, *args, **kwargs):
        '''used to get the request pages async
        '''
        method= request_method[method]
        self.threadPool.apply_async(method, args=args, kwds=kwargs, callback=self.spi_response)


    def spi_response(self, response, *args, **kwargs):
        '''Response of the spi_request are handled here
        '''
        link.parse_link(response)
