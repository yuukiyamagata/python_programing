import threading
import queue
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(queue):
    logging.debug('start')
    queue.put(100) # [100, 200] first in first out
    time.sleep(5)
    queue.put(200)
    logging.debug('end')

def worker2(queue):
    logging.debug('start')
    logging.debug(queue.get()) # 100
    logging.debug(queue.get()) # 200
    logging.debug('end')

if __name__ == '__main__':
  queue = queue.Queue()
  t1 = threading.Thread(target=worker1, args=(queue,))
  t2 = threading.Thread(target=worker2, args=(queue,))

  t1.start()
  t2.start()

  # print('started')
  # t1.join()
  # mainスレッド、t1スレッド、t2スレッドの3つが走っている
