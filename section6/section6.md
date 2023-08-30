## モジュールとパッケージ

## コマンドライン引数の扱い

```py
import sys

sys.argv
# コマンドライン引数をリスト形式で表示できる

```

## import文とAS
__init__.pyがあると一番最初に読み込まれる。これがないとpythonがPackageと認めない

```py
import lesson_package.utils
# lesson_packageのutilsを使用する。下記と動議
from lesson_package import utils
from lesson_package.utils import say_twice

r = lesson_package.utils.say_twice('hello')
print(r)

# from lesson_package import utils を使用する場合
# r = utils.say_twice('hello)

# from lesson_package.utils import say_twice
# r = say_twice('hello)

```

## アスタリスクのimportと__init__.pyと__all__.pyの意味
__init__.pyに`__all__ = ['animal', 'human']`を入れると、ディレクトリ配下にあるファイルを読み込む
```py
from lesson_package.talk import *
# * ですべて読み込み

print(animal.sing())
print(animal.cry())

print(human.sing())
print(human.cry())

```

## importErrorの使い方
古いパッケージでも新しいパッケージでもどちらでも使用したい時にImportErrorを使用する
```py
try:
  from lesson_package import utils
except ImportError:
  from lesson_package.tools import utils

utils.say_twice('word')

```

## setup.pyパッケージ化して配布する
独自のパッケージを作成することができる
setup.pyが格納されているディレクトリで1`python setup.py sdist`を実行する
```py
setup(
  name='python_programming',
  version='1.0.0',
  packages=['lesson_package', 'lesson_package.talk', 'lesson_package.tools'],
  utl='https://gojyo.appspopt.com',
  license='Free',
  author='s_getou',
  author_email='test@gmail.com',
  description='Sample package'
)
```

## 組み込み関数
https://docs.python.org/ja/3/library/functions.html?highlight=sorted#sorted
buildinsに組み込み関数が入っている

sorted(iterable, /, *, key=None, reverse=False)
iterable の要素を並べ替えた新たなリストを返します。
2 つのオプション引数があり、これらはキーワード引数として指定されなければなりません。
key には 1 引数関数を指定します。これは iterable の各要素から比較キーを展開するのに使われます
(例えば,key=str.lower のように指定します)。 デフォルト値は None です (要素を直接比較します)。
reverse は真偽値です。 True がセットされた場合、リストの要素は個々の比較が反転したものとして並び替えられます。


## 標準ライブラリ
`pip install termcolor` 

```py
from termcolor import colored

print('test')
print(colored('test', 'red'))
```
`help(colored)`で確認できる

## importする際の記述の仕方
`import collections, sys, os`のようにできるが、推奨はされていない
```py
import collections
import os
import sys

import lesson_package

import config
```
標準ライブラリはアルファベット順で並べる
標準ライブラリとサードパーティのライブラリはインポートする際にスペースを開ける
自分たちが作成したパッケージはスペースを開ける
ファイルもスペースを開ける

## __name__と__main__
実行しているmainのスクリプトの時に__name__はmainを返す
importして読み込まれた場合、__name__はファイル名を返す

mainで実行しているとしても、下記のように書く
```py
import lesson_package.talk.animal

import config


def main():
  lesson_package.talk.animal.sing()

if __name__=='__main__':
  main()

```