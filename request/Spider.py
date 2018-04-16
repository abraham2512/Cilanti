from requests import get, post
from multiprocessing.pool import ThreadPool
from links import Links
from hasher import Hasher
import Cilanticonfig
from database import Database

request_method = {
    'get': get,
    'post': post,
}


class Spider:

    def __init__(self):
        self.threadPool = ThreadPool(Cilanticonfig.MAX_THREAD)
        self.URLset = Cilanticonfig.getSeed()
        self.URLhash = set([])
        self.database = Database(Cilanticonfig.dbfile)

    def spi_request(self, method, *args, **kwargs):
        '''used to get the request pages async
        '''
        method = request_method[method]
        self.threadPool.apply_async(method, args=args, kwds=kwargs, callback=self.spi_response)

    def spi_response(self, response, *args, **kwargs):
        '''Response of the spi_request are handled here
        '''

        if 'text/html' in response.headers['Content-Type']:
            hash_val = Hasher.HashMD5(response.content)
            if hash_val not in self.URLhash:
                self.URLhash.add(hash_val)
                self.URLset.union(Links.parse_link(response))

               #STORE CURRENT URL AND DATA HERE
               # Database.saveData(url,response.content,keyword)













