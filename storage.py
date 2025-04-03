import os 
import json

def load_previous_dates(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_current_dates(file_path, date_list):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(date_list, f, ensure_ascii=False, indent=2)