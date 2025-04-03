import requests
import json

# 메가박스에서 예매 가능 관 목록 불러오기
def fetch_schedule(movie_no, branch_no, play_date):
    url = "https://m.megabox.co.kr/on/oh/ohb/SimpleBooking/selectBokdList.do"

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "https://m.megabox.co.kr/",
        "User-Agent": "Mozilla/5.0"
    }
    payload = {
        "menuId": "M-RE-MO-02",
        "imgSizeDiv": "IMG_TYPE_7",
        "flag": "DATE",
        "brchNo": branch_no,
        "brchNo1": branch_no,
        "movieNo1": movie_no,
        "playDe": play_date,
        "sellChnlCd": "MOBILEWEB",
        "youdBetterSearch": "Y"
    }

    res = requests.post(url, headers=headers, json=payload)
    res.raise_for_status()
    data = res.json()

    return data.get("scheduleList", [])

#상영관 필터 + 예매 가능 여부 확인
def filter_available_schedules(schedules, target_theater_codes=["MX", "DBC"]):
    result = []
    for s in schedules:
        if s.get("theabKindCd") in target_theater_codes and s.get("bokdAbleAt") == "Y":
            result.append({
                "movie": s.get("movieNm"),
                "theater": s.get("theabExpoNm"),
                "start": s.get("playStartTime"),
                "date": s.get("playDe")
            })
    return result
