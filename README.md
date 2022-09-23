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

## 対応状況

現時点では以下のAPIしか対応しておりません。今後順次アップデートしていこうと考えています。

### 対応済

- [認証用Tokenの取得](https://ieyasu.co/docs/api.html#/paths/~1authentication~1token/get)
- [認証用Tokenの削除](https://ieyasu.co/docs/api.html#/paths/~1authentication~1destroy/delete)
- [指定された日の日次勤怠データの一覧](https://ieyasu.co/docs/api.html#/paths/~1work_outputs~1daily~1{day}/get)

### 未対応

- [指定された月の日次勤怠データの一覧](https://ieyasu.co/docs/api.html#/paths/~1work_outputs~1monthly~1{month}/get)
- [ユーザー一覧](https://ieyasu.co/docs/api.html#/paths/~1users/get)
- [ユーザー登録・更新](https://ieyasu.co/docs/api.html#/paths/~1users/post)
- [月次レポートの一覧](https://ieyasu.co/docs/api.html#/paths/~1work_output_months~1monthly~1{month}/get)
- [打刻登録](https://ieyasu.co/docs/api.html#/paths/~1stamp_logs/post)
- [日付指定の打刻履歴の一覧](https://ieyasu.co/docs/api.html#/paths/~1stamp_logs~1daily~1{day}/get)
- [ユーザー指定の打刻履歴の一覧](https://ieyasu.co/docs/api.html#/paths/~1stamp_logs~1user~1{user_id}/get)
- [拠点一覧](https://ieyasu.co/docs/api.html#/paths/~1lodgments/get)
- [都道府県一覧](https://ieyasu.co/docs/api.html#/paths/~1prefecturals/get)
- [部門一覧](https://ieyasu.co/docs/api.html#/paths/~1departments/get)
- [雇用形態一覧](https://ieyasu.co/docs/api.html#/paths/~1employments/get)
- [休暇一覧](https://ieyasu.co/docs/api.html#/paths/~1paid_holidays/get)
- [休暇管理情報の取得](https://ieyasu.co/docs/api.html#/paths/~1paid_holidays~1{id}~1users~1{user_id}~1year~1{year}/get)
- [契約一覧](https://ieyasu.co/docs/api.html#/paths/~1deal_contracts/get)
- [契約の登録](https://ieyasu.co/docs/api.html#/paths/~1deal_contracts/post)
- [契約の削除](https://ieyasu.co/docs/api.html#/paths/~1deal_contracts~1{id}/delete)
- [契約の更新](https://ieyasu.co/docs/api.html#/paths/~1deal_contracts~1{id}/put)
- [取引先一覧](https://ieyasu.co/docs/api.html#/paths/~1business_partners/get)
- [取引先の登録](https://ieyasu.co/docs/api.html#/paths/~1business_partners/post)
- [取引先の削除](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{id}/delete)
- [取引先の更新](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{id}/put)
- [取引先承認担当者一覧](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{business_partner_id}~1business_partner_users/get)
- [取引先承認担当者の登録](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{business_partner_id}~1business_partner_users/post)
- [取引先承認担当者の削除](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{business_partner_id}~1business_partner_users~1{id}/delete)
- [取引先承認担当者の更新](https://ieyasu.co/docs/api.html#/paths/~1business_partners~1{business_partner_id}~1business_partner_users~1{id}/put)
