from requests import get, post
from threading import Thread
from multiprocessing.pool import ThreadPool
import MyCrawlconfig

request_method={
    'get' : get,
    'post': post,
}

class Spider:
    def __init__(self):
        self.threadPool = ThreadPool(MyCrawlconfig.MAX_THREAD)

    def spi_request(self, method, *args, **kwargs):
        '''used to get the request pages async
        '''
        method= request_method[method]
        self.threadPool.apply_async(method, args=args, kwds=kwargs, callback=self.spi_response)


    def spi_response(self, response, *args, **kwargs):
        '''Response of the spi_request are handled here
        '''
        print(response.content)
