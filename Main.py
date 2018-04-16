from request import Spider
from threading import Thread
import Cilanticonfig


def wait():
    if Cilanticonfig.DONE:
        return
    else:
        input()
        wait()


thread = Thread(target=wait)
thread.start()

'''Spider instance created here'''

spider = Spider.Spider()
for i in spider.URLset:
    spider.spi_request('get', i)


thread.join()
print("-----------------------------------------------------Done--------------------------------------------------")

for j in spider.URLhash:
    print(j)

