# pyhrmos

[HRMOS勤怠API](https://ieyasu.co/docs/api.html)へのリクエストを簡易化するためのPythonラッパーライブラリです。

## インストール

以下のコマンドでインストールできます。

```sh
pip install git+https://github.com/KensukeShimoji/pyhrmos
```

## 使い方

```python
from pyhrmos import Hrmos

url = 'https://ieyasu.co/api/company_url'
api_key = 'MGE3M2Y2NDA3MTIxZTRlMzNkMDFhOTgw'
with Hrmos(url, api_key) as hrmos:
	# 認証TokenはAPI KEYから自動で取得
	# 以降はメソッド経由でにて各種APIへアクセス

    # 2018年6月12日時点の日次勤怠データ一覧取得(Pagenationあり)
    data = hrmos.get_daily_work_output(datetime.date(2018,6,12))

    # 2018年6月12日時点の日次勤怠データ一覧取得(Pagenationなし)
    data = hrmos.get_daily_work_output_all(datetime.date(2018,6,12))

# 取得したTokenは自動で削除される
```

## テスト

個々人の環境でテストを実行するためには`.env.sample`を参考にプロジェクトルートに`.env`を作成する必要があります。  
[APIのURL](https://ieyasu.co/docs/api.html#section/APIURL)や[API KEY](https://ieyasu.co/docs/api.html#section/Authentication)の取得方法については[公式ページ](https://ieyasu.co/docs/api.html)を参考にして下さい。
