from request import Spider
from threading import Thread
import Cilanticonfig

def wait():
    if Cilanticonfig.DONE == True:
        return
    else:
        input("Enter value")
        wait()

thread = Thread(target=wait)
thread.start()

spider = Spider.Spider()
for i in range(0,1) :
    spider.spi_request('get', 'https://stackoverflow.com')

thread.join()
print("Done")
