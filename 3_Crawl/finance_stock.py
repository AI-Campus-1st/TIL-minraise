import requests

BASE_URL = ("https://apis.data.go.kr/1160100/service/"
            "GetStockSecuritiesInfoService")

class ApiError(Exception):
    pass

import requests
from urllib.parse import urlencode

class GetStockAPI:
    """공공데이터 금융위원회 주식시세정보 API"""

    def __init__(self, key, **kwargs):
        self.key = key 
        self.extra_params = {
            "resultType": "json",
            **kwargs,
        }

    def _fetch(self, url, params):
        query = urlencode(params)
        full_url = f"{url}?serviceKey={self.key}&{query}"

        r = requests.get(full_url, timeout=10)
        r.raise_for_status()

        try:
            body = r.json()
        except ValueError:
            raise ApiError(f"JSON이 아닌 응답: {r.text[:200]}")

        header = body["response"]["header"]
        code, msg = header["resultCode"], header["resultMsg"]

        if code != "00":
            if code == '30' or "SERVICE_KEY_IS_NOT_REGISTERED_ERROR" in msg:
                raise ApiError("인증키 오류 — 승인이 반영됐는지 확인하세요.")
            if code == '22' or "LIMITED_NUMBER_OF_SERVICE_REQUESTS_EXCEEDS_ERROR" in msg:
                raise ApiError("일일 쿼터(10,000건)를 초과했습니다. 내일 다시 시도하세요.")
            if code == '10' or "INVALID_REQUEST_PARAMETER_ERROR" in msg:
                raise ApiError(f"필수 파라미터 누락 — 전달값: {list(params)}")
            raise ApiError(f"[{code}] {msg}")

        return body["response"]["body"]

    def get_stocks(self, page, size):
        url = BASE_URL + '/getStockPriceInfo'
        params = {**self.extra_params, 'pageNo': page, 'numOfRows': size}
        body = self._fetch(url, params)
        return body["items"]["item"]

samsung = GetStockAPI(KEY, likeSrtnCd="005930")

try:
    items = samsung.get_stocks(1, 5)
    for it in items:
        print(it["basDt"], it["itmsNm"], it["clpr"], it["trqu"])
except ApiError as e:
    print("API 오류:", e)