## 並列化

異なる処理を同時に動かすことができる

```py
import threading;
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
  logging.debug('start')
  time.sleep(5)
  logging.debug('end')

def worker2():
  logging.debug('start')
  time.sleep(2)
  logging.debug('end')

if __name__ == '__main__':
  t1 = threading.Thread(target=worker1)  # スレッドが一つ走る
  t2 = threading.Thread(target=worker2)  # スレッドが一つ走る
  t1.setDaemon(True)
  t1.start()
  t2.start()
  print('started')
  t1.join()
  # mainスレッド、t1スレッド、t2スレッドの3つが走っている
```



## スレッドに渡す引数
以下のように実装する

 ```py
  t1 = threading.Thread(name='rename worked1', target=worker1)  # スレッドが一つ走る
  t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y':200})  # スレッドが一つ走る
 ```

 ## デーモンスレッド
  t1.setDaemon(True)のように設定すると別スレッドの処理を待たずにプログラムが終了する
  t1.join()で処理の強制終了を解除する。プログラムの終了時にはjoinを明示的に記述するとよい


## 生存中のThreadオブジェクトをすべてリスト表示
print(threading.enumerate())

```py
for thread in threading.enumerate():
  print(threading.enumerate())
  if thread is threading.currentThread():
    print(thread)
    continue
  thread.join()

```
[<_MainThread(MainThread, started 140704636106304)>]
[<_MainThread(MainThread, started 140704636106304)>]
[<_MainThread(MainThread, started 140704636106304)>]
[<_MainThread(MainThread, started 140704636106304)>]

## タイマー
スレッドを開始する際にx秒処理を遅延することができる
```py
 t = threading.Timer(3, worker1, args=(100, ), kwargs={'y': 200 })
 t.start()

```


## スレッドのLockとRLock


```py
def worker1(d, lock):
  logging.debug('start')
  lock.acquire() # lockを取得する。他のスレッドからlock解放までの処理をさせないようにする
  i = d['x']
  time.sleep(5)
  with lock:
    # 前のlockがreleaseされていないのでデットロックのような状態になる。RLockで対応
    d['x'] = i + 1
  logging.debug(d)
  lock.release() # lockを解放する
  logging.debug('end')

def worker2(d, lock):
  logging.debug('start')
  with lock
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
  logging.debug('end')

if __name__ == '__main__':
  d = {'x': 0 }
  lock = threading.Rock()
  t1 = threading.Thread(target=worker1, args=(d, lock))
  t2 = threading.Thread(target=worker2, args=(d, lock))
  t1.start()
  t2.start()
  # print('started')
  # t1.join()
  # mainスレッド、t1スレッド、t2スレッドの3つが走っている
```


## セマフォ
スレッド数のコントロール


```py

def worker1(semaphore):
  with semaphore:
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2(semaphore):
  with semaphore:
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker3(semaphore):
  with semaphore:
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

if __name__ == '__main__':
  d = {'x': 0 }
  semaphore = threading.Semaphore(2) # スレッドを二つコントロールしている
  t1 = threading.Thread(target=worker1, args=(semaphore,))
  t2 = threading.Thread(target=worker2, args=(semaphore,))
  t3 = threading.Thread(target=worker3, args=(semaphore,))

  t1.start()
  t2.start()
  t3.start()

  # workerが二つ終了してから三つ目のworkerが走り出す
  # print('started')
  # t1.join()
  # mainスレッド、t1スレッド、t2スレッドの3つが走っている
```


## キュー
woekr間でデータを入れたり受け取ったりすることができる
ロックやセマフォを使用せずにqueueがその役割を担っている


```py


```

## イベント


```py


```

## コンディション


```py


```

## バリア


```py


```

## マルチプロセス


```py


```

## ワーカープロセス


```py


```