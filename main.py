from megabox_crawler import fetch_schedule, filter_available_schedules
from storage import load_previous_dates, save_current_dates
from alarm import send_kakao_message
from datetime import datetime, timedelta
import os
import time

MOVIE_NO = "25008000"       # 예: 진격의 거인 완결편
BRANCH_NO = "1351"          # 코엑스
THEATER_CODES = ["MX4D"]     # MX4D관
STORAGE_PATH = "data/open_dates.json"

def format_for_storage(schedule):
    # 날짜 + 시작시간을 기준으로 비교
    return [f"{s['date']} {s['start']}" for s in schedule]

def notify_open_schedules(schedules):
    for item in schedules:
        msg = f"[OPEN] {item['movie']} - {item['theater']} / {item['date']} {item['start']}"
        print(msg)
        send_kakao_message(msg)


if __name__ == "__main__":
    while True:
        print("🔁 예매 오픈 확인 중...")

        today = datetime.today()
        full_result = []

        for i in range(7):  # 7일간 예매 오픈 확인
            play_date = (today + timedelta(days=i)).strftime("%Y%m%d")
            schedule = fetch_schedule(MOVIE_NO, BRANCH_NO, play_date)
            filtered = filter_available_schedules(schedule, THEATER_CODES)
            full_result.extend(filtered)

        current_formatted = format_for_storage(full_result)
        previous_formatted = load_previous_dates(STORAGE_PATH)

        new_items = [s for s in full_result if f"{s['date']} {s['start']}" not in previous_formatted]

        if new_items:
            print("📢 새로운 예매 오픈이 감지되었습니다!")
            notify_open_schedules(new_items)
            save_current_dates(STORAGE_PATH, current_formatted)
        else:
            print("✅ 새로운 오픈 일정이 없습니다.")

        print("⏳ 5분 후 재확인...")
        time.sleep(300)  # 5분 = 300초
