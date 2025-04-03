import requests

def get_access_token(auth_code):
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": "1f4366db499f7d39f5619beae94903f6",
        "redirect_uri": "https://example.com",  # 콘솔에 등록된 URI랑 똑같아야 함
        "code": auth_code
    }

    response = requests.post(url, data=data)
    result = response.json()
    print("🔑 access_token:", result.get("access_token"))
    return result.get("access_token")

if __name__ == "__main__":
    auth_code = "46BV7fRAethAK4UvRAdwCk6LHyGlVhPRE5Wwfoa3cLJk4FIUliU4GwAAAAQKFxJVAAABlfpxDnQWphHJzwXJqw"
    get_access_token(auth_code)
