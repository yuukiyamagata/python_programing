# クラス

クラスとは：オブジェクトを作成するためのひな形のようなもの
インスタンス化：クラスからオブジェクトを生成する処理のこと
インスタンス：クラスから生成されたオブジェクト
コンストラクター：オブジェクトの作成時に実行される処理(コンストラクタ)
デストラクタ：クラスが使用されなくなった時に実行される


## JavaScriptにおけるクラスの定義と周辺知識
クラスとは：オブジェクトを作成するためのひな形のようなもの
コンストラクター関数：新しくオブジェクトを作成するための雛形となる関数
-> Class経由で使用するコンストラクターと同様の働きをする
インスタンス化：new演算子を用いてコンストクター関数からオブジェクトを生成する処理のこと
-> インスタンス化した際に格納したいプロパティはthis.~で記述する
インスタンス：インスタンス化によって生成されたオブジェクト



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

## コンストラクタとデストラクタ

```py
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
      print('run' * num)

    def __del__(self):
      print('Good by')

person = Person('Mike')
person.say_something()
```

## クラスの継承
あるクラスが所有している機能を他のクラスにも適用すること

```py
class Car(object):
  def run(self):
    print('run')


class ToyotaCar(Car):
  pass

class TeslaCar(Car):
  def auto_run(self):
    print('auto run')

car = Car()
car.run()

print('###############')
toyota_cat = ToyotaCar()
toyota_cat.run()
print('################')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()


```

## メソッドのオーバーライドとsuperによる親のメソッド呼び出し
メソッドを継承先で再度定義すると上書きできる
__init__内でsuperを呼び出すことで継承元の__init__を呼び出すことができる

```py
class Car(object):
  def __init__(self, model=None):
    self.model = model
  def run(self):
    print('run')


class ToyotaCar(Car):
  def run(self):
    print('fast')

class TeslaCar(Car):
  def __init__(self, model='Model S', enable_auto_run=False):
    # self.model = model
    super().__init__(model)
    self.enable_auto_run = enable_auto_run
  def run(self):
    print('super fast')

  def auto_run(self):
    print('auto run')

car = Car()
car.run()

print('###############')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('################')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()


```

## プロパティを使った属性の設定
外からその変数を参照できないようにしたいとき_(アンダースコア)を使用する