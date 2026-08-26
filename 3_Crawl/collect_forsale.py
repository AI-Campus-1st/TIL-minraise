from typing import Tuple

import requests

URL = "https://realty.asil.kr/api_asil/data_sale_of_apt_nomal.aspx"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "referer": "https://asil.kr/app/apt_list.jsp",
}
DATAS = {
    "oidx": 2,
    "oby": "down",
    "total": 20,
}


def fetch(seq: str, page: int = 1) -> dict:
    r = requests.post(
        URL,
        data={**DATAS, "asil_bldcode": seq, "focus_bldcode": seq, "last_mm_num": (page - 1) * 20},
        headers=HEADERS,
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def parse(datas: dict, seq: str) -> Tuple[list, bool]:
    rows = []
    for item in datas.get("list_result", []):
        rows.append(
            {
                "seq": seq, 
                "uid": item.get("mm_uid", ""),
                "상세": item.get("FETR_DESC", ""),
                "중개사": item.get("BRKG_NM", ""),
                "매물유형": item.get("DEALTYPE_NM", ""),
                "동": item.get("BDONG_NM", ""),
                "층": item.get("CORES_FLR_CNT_NM", ""),
                "공급면적": item.get("CTRT_SPC") or item.get("SPLY_SPC", ""),
                "전용면적": item.get("EXCLS_SPC", ""),
                "매매가": item.get("DEAL_AMT", ""),
                "보증금": item.get("WRRNT_AMT", ""),
                "월세": item.get("LEASE_AMT", ""),
                "등록일": item.get("SVC_DATE_STRT", ""),
            }
        )
    has_next = bool(datas.get("next_page", False))
    return rows, has_next
