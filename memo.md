# ファイル操作
ファイル操作は基本的に下記のライブラリを使用すればやりたいことは出てくる

import os  
import pathlib  
import glob  
import shutil


## ファイルの書き込み
```py
s = """\
AAA
# 0=A,1=A,2=A,3=\n
BBB
CCC
DDD
"""

with open('test.txt', 'r') as f:
        # print( f.print() )
        while True:
            chunk = 2
            line = f.read(chunk)
            print(line)
            if not line:
                  break

```

```py
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)

# 
```

## CSVファイルの読み込みと書き込み
windowsを使用する場合、改行が\r\nとなりCSV読み込みの際に2行改行されてしまう。  
newline=''をいれて、ファイルをオープンする

```py
import csv

with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})


with open('test.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
              print(row['Name'], row['Count'])
```

```py
import os
import pathlib
import glob
import shutil

os.path.exists('test.txt') 
# ファイルが存在するかどうか確認
os.path.isfile('test.txt') 
#  引数に入力された名前のファイルがファイル形式であるかどうか確認する
os.path.isdir('design')
# 引数に入力された名前のファイルorディレクトリがディレクトリであるかどうかを確認する
os.rename('test.txt', 'renamed.txt')
# 第一引数に入力されたファイル名を、第二引数に入力されたファイル名に変更する
os.symlink('renamed.txt', 'symlink.txt')
# シンボリックリンク(ショートカットコピー)の作成
os.mkdir('test_dir')
#  ディレクトリの作成
os.rmdir('test_dir')
# ディレクトリの削除
pathlib.Path('empty.txt').touch() 
# 空のファイルを作成
os.remove('empty.txt')
# ファイルの削除
os.listdir('test.dir')
# ディレクトリの配下のディレクトリ、ファイルを表示
glob.glob('test_dir/test_dir2/*')
# 引数に入力されたPath内のファイルを全取得
shutil.copy('test_dir/empty.txt', 'test_dir/test_dir2/empty2.txt')
# 第一引数で入力されたファイルを第二引数で入力されたPath配下にcopyする
shutil.retree('test_dir')
# 配下のディレクトリをすべて削除
os.getcwd()
# 現在いるPathを表示
```

glob  
glob モジュールは Unix シェルで使われているルールに従い指定されたパターンに一致するすべてのパス名を見つけ出します。返される結果の順序は不定です。

## tarfile
**macで圧縮ファイルを解凍する方法**  
`tar zxvf test.tat.gz -C /tmp`

```py
import tarfile
tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
       # tr.extractall(path='test_tar')
        with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
                print(f.read())
         # ファイル読み込み       

```

## zipfile
Macの場合以下のコマンドでzipファイルを解凍できる  
`unzip test.zip -d ディレクトリ名`

```py
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir') # この時点だとディレクトリしか作らない
    z.write('test_dir/test.txt')

# zipfileの読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2') # zzz2にtest.zipを展開
    with z.open('test_dir/test.txt') as f:
        print(f.read())
```

## tempfile
I/Oバッファでファイルを作成する  
使用後は自動で削除される

rf)  
バッファーという一時保存用メモリーを介してアクセスする入出力方式です。  
ハードディスクなどの二次記憶装置は、主記憶に比べるとデータの入出力速度が大幅に遅いのが普通です。  
読み書き対象のデータを一時的にバッファーに置き、それに対して入出力処理を実施すれば、二次記憶装置の速度に左右されずに高速処理が実現できます。  