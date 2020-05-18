import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

payload = '* trạng từ chỉ sự thường xuyên nằm trước động từ thường, sau động từ To be'
headers = {
    'api-key': 'ZSYKrguLqkQyJ7FIOi4KcLL11U6fLwye',
    'speed': '',
    'voice': 'banmai'
}

response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)

print(response.text)