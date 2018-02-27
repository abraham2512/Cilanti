from request import Spider
from threading import Thread
import Cilanticonfig

def wait():
    if Cilanticonfig.DONE == True:
        return
    else:
        input()
        wait()

thread = Thread(target=wait)
thread.start()

spider = Spider.Spider()
for i in spider.initial_url :
    spider.spi_request('get', i)
    
thread.join()
print("Done")
