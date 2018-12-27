import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def fun1():
    logging.debug('Start')
    time.sleep(3)
    logging.debug('Close')

def fun2():
    logging.debug('Start')
    time.sleep(5)
    logging.debug('Close')

f1_1 = threading.Thread(name='fun1', target=fun1)
f2_1 = threading.Thread(name='fun2', target=fun2)
f1_2 = threading.Thread(target=fun1) # use default name

f1_1.start()
f2_1.start()
f1_2.start()