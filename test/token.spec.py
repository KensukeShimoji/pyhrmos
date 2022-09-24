""" Token管理テストモジュール"""
from datetime import date
import os
import unittest

from dotenv import load_dotenv
from pyhrmos import Hrmos


class TestTokenManagements(unittest.TestCase):
    """ Token管理テストケース """

    def setUp(self) -> None:
        load_dotenv()

    def test_token_lifecycle(self):
        """ Token取得・削除処理 """
        base_url = os.environ.get('HRMOS_URL')
        auth_token = os.environ.get('HRMOS_API_KEY')
        with Hrmos(base_url, auth_token) as hrmos:
            self.assertEqual(hrmos.base_url, base_url)
            self.assertEqual(hrmos.api_key, auth_token)
            self.assertIsNotNone(hrmos.access_token)
            data = hrmos.get_daily_work_outputs(date.today())
            print(data)
            data = hrmos.get_daily_work_outputs_all(date.today())
            print(len(data))
            self.assertIsNotNone(data)
        self.assertIsNone(hrmos.access_token)



if __name__ == '__main__':
    unittest.main()
