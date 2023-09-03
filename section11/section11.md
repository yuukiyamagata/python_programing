## コンフィグとロギング

## configparser
configファイルを読み書きする

```py
# ファイルへの書き込み
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
  'debug': True
}

config['web_server'] = {
  'host': '127.0.0.1',
  'port': 80
}

config['db_server'] = {
  'host': '127.0.0.1',
  'port': 3306
}

with open('config.ini', 'w') as config_file:
  config.write(config_file)

```

```py
# ファイルよみこみ
config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])

print(config['DEFAULT']['debug'])

```

## yaml

```py
# ファイルへの書き込み
with open('config.yml', 'w') as yaml_file:
  yaml.dump({
    'web_server': {
      'host': '127.0.0.1',
      'port': 80
    },
    'db_server':{
      'host': '127.0.0.1',
      'port': 3306
    }
  }, yaml_file)
```

```py
# ファイル読み込み
with open('config.yml', 'r') as yaml_file:
  data = yaml.safe_load(yaml_file)
  print(data, type(data))

```

## ロギング

```py
"""
CRITICAL
  ERROR
  WARNING
  INFO
  DEBUG
"""
import logging

logging.basicConfig(level=logging.INFO) # ログレベルの変更
logging.basicConfig(level=logging.DEBUG) # ログレベルの変更

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

```

## ロギング フォーマッター
https://docs.python.org/ja/3/howto/logging.html

```py
# formatter = '%(levelname)s:%(message)s '
# formatter = '%(asctime)s:%(message)s '

logging.basicConfig(level=logging.INFO, format=formatter)
logging.info('info %s %s', 'test1', 'test2')

```

## ロギング ロガー

```py
logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__) # 実行中のファイル名を取得する
logger.setLevel(logging.DEBUG) # 取得したLoggerに対してログレベルを変更することができる
logger.debug('debug')

```
mainでloggerを作成してそれ以降はloggerを使用する
```py
import logging

import logtest

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info('from main')

logtest.do_something()

```

## ロギングハンドラー
https://docs.python.org/ja/3/library/logging.handlers.html

## ロギング フィルタ
ログにパスワードなどを含めたくない時
クラスで継承して、logging.Filterを使用する

```py

class NoPassFilter(logging.Filter):
  def filter(self, record):
    log_message = record.getMessage()
    return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())

logger.info('from main')
logger.info('form main password = "test"')

```

## ロギング  config
