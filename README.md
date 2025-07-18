# flask_to_TG
Пример запроса с авторизацией:
С помощью curl:
✅ Вариант для PowerShell (Windows):
powershell:
curl -X POST http://localhost:5004/send `
  -H "Content-Type: application/json" `
  -H "X-API-Key: supersecretkey" `
  -d "{\"message\": \"Привет от Bot A\"}"
✅ Вариант для Bash / Linux / WSL / macOS:
bash:
curl -X POST http://localhost:5004/send \
  -H "Content-Type: application/json" \
  -H "X-API-Key: supersecretkey" \
  -d '{"message": "Привет от Bot A"}'


Альтернатива: Проверка через httpie
Если у тебя установлен httpie, можно проверить проще:

bash:
http POST http://localhost:5004/send X-API-Key:supersecretkey message="Привет от Bot A"


На python:
import requests

url = "http://localhost:5004/send"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "supersecretkey"
}
data = {
    "message": "Привет от Bot A"
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.json())
