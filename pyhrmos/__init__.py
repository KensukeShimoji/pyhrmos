
""" Main Module """

from dataclasses import dataclass
from datetime import datetime, date
from http import HTTPStatus
from typing import Optional

import requests
from pyhrmos.pagination import PagenationQuery, PagenatedResponse

from pyhrmos.work_outputs import WorkOutputs


@dataclass
class HrmosAccessToken:
    """ 認証用Token"""
    value: str
    expired_at: datetime


class HrmosApiRequestException(Exception):
    """ custom exception for failed hrmos api request """


class Hrmos:  # pylint: disable=invalid-name
    """ HRMOS勤怠APIのWrapper """

    base_url: str
    api_key: str
    http_timeout: int
    access_token: Optional[HrmosAccessToken]

    def __init__(self, base_url: str, api_key: str, http_timeout=60):
        self.base_url = base_url
        self.api_key = api_key
        self.http_timeout = http_timeout

    def __enter__(self):
        self.access_token = self.__get_access_token()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.access_token is not None:
            self.__delete_access_token()
            self.access_token = None

    def __get_auth_headers(self):
        return {'Authorization': f'Token {self.access_token.value}',
                'Content-Type': 'application/json'}

    def __get_request_headers(self, p: PagenationQuery):
        headers = self.__get_auth_headers()
        if p.limit is not None:
            headers.update({'limit': str(p.limit)})
        if p.page is not None:
            headers.update({'page': str(p.page)})
        if p.date_from is not None:
            headers.update({'from': str(p.date_from)})
        if p.date_to is not None:
            headers.update({'to': str(p.date_to)})
        return headers

    def __get_access_token(self) -> Optional[HrmosAccessToken]:
        url = f'{self.base_url}/v1/authentication/token'
        headers = {'Authorization': f'Basic {self.api_key}',
                   'Content-Type': 'application/json'}
        res = requests.get(url, headers=headers, timeout=self.http_timeout)
        if res.status_code == HTTPStatus.OK:
            data = res.json()
            return HrmosAccessToken(
                value=data['token'], expired_at=datetime.fromisoformat(data['expired_at']))
        raise HrmosApiRequestException(res.text)

    def __delete_access_token(self) -> None:
        url = f'{self.base_url}/v1/authentication/destroy'
        res = requests.delete(
            url, headers=self.__get_auth_headers(), timeout=self.http_timeout)
        if res.status_code != HTTPStatus.OK:
            raise HrmosApiRequestException(res.text)

    def get_daily_work_outputs(self, target_date: date, pagenation=PagenationQuery()) -> PagenatedResponse[list[WorkOutputs]]:
        """ 指定された日の日次勤怠データの一覧

        Args:
            target_date (date): 取得対象の日付
            pagenation (_type_, optional): ページ指定. Defaults to Pagenation().

        Returns:
            tuple[list[WorkOutputs], PagenationResponse]: 日次勤怠データの一覧, ページ情報
        """
        url = f'{self.base_url}/v1/work_outputs/daily/{target_date.strftime("%Y-%m-%d")}'
        res = requests.get(
            url, headers=self.__get_request_headers(pagenation), timeout=self.http_timeout)
        daily_work_outputs: list[WorkOutputs] = []
        for d in res.json():
            daily_work_outputs.append(WorkOutputs.of(d))
        return PagenatedResponse.of(res.headers, daily_work_outputs)

    def get_daily_work_outputs_all(self, target_date: date) -> list[WorkOutputs]:
        """ 指定された日の日次勤怠データの一覧を全て取得する

        Args:
            target_date (date): 取得対象の日付

        Returns:
            list[WorkOutputs]: 日次勤怠データの一覧
        """
        pagenation = PagenationQuery(limit=100, page=1)
        dwo = self.get_daily_work_outputs(
            target_date=target_date, pagenation=pagenation)
        response = dwo.data
        for p_index in range(2, dwo.total_page + 1):
            pagenation.page = p_index
            dwo = self.get_daily_work_outputs(target_date=target_date, pagenation=pagenation)
            response.extend(dwo.data) 
        return response
