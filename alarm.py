import requests

def send_kakao_message(msg):
    access_token = "beE--1nhrPbilBNFkLDuo-u04dfmbOOIAAAAAQoNDSEAAAGV-nJGm_sTCyemC-i_"

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'template_object': str({
            "object_type": "text",
            "text": msg,
            "link": {
                "web_url": "https://megabox.co.kr",
                "mobile_web_url": "https://megabox.co.kr"
            },
            "button_title": "예매하러 가기"
        }).replace("'", '"')  # JSON 문자열로 변환 
    }

    res = requests.post(url, headers=headers, data=data)
    print(f"[카카오톡 응답] {res.status_code}: {res.text}")
