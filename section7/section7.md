# クラス

クラスとは：オブジェクトを生成するためのひな形のようなもの
インスタンスとは：
コンストラクターとは：クラスがインスタンス化されたときに一番初めに呼ばれる関数

```py
class Person(object):
    def say_something(self):
        print('hello')

person = Person()
person.say_something()

```
Python3では`class Persion(object)`のように書かなくてもよい。
以下のコードすべて同じ意味
```py
class Person():
    def say_hello(self):
        print('hello')
class Person(object):
    def say_hello(self):
        print('hello')
class Person:
    def say_hello(self):
        print('hello')

```

## クラスの初期化

```py
class Person(object):
    def __init__(self):
        print('First')
    
    def say_something(self):
        print('hello')

```