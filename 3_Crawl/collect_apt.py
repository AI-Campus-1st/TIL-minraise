import requests

URL = "https://asil.kr/app/data/data_apt_list.jsp"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "referer": "https://asil.kr/app/apt_list.jsp",
}
PARAMS = {
    "building": "",
    "household": 50,  
    "order": 0,
    "order_type": 0,
}


def fetch(dong: str) -> list:
    """행정동 코드로 아파트 목록 JSON을 가져온다. 실패하면 예외를 그대로 던진다."""
    r = requests.get(URL, params={**PARAMS, "dong": dong}, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def parse(datas: list) -> list[dict]:
    rows = []
    for item in datas:
        rows.append(
            {
                "seq": item.get("seq", ""),
                "동": item.get("dongname", ""),
                "단지명": item.get("name", ""),
                "세대수": item.get("household", ""),
                "건축년도": item.get("movein", ""),
                "매물수": item.get("offer", ""),
                "위도": item.get("lat", ""),
                "경도": item.get("lng", ""),
            }
        )
    return rows