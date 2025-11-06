# flask_to_TG
Пример запроса с авторизацией:

linux

curl -X POST https://srvfree.duckdns.org/send -H "Content-Type:application/json" -H "X-API-Key:123" -d '{"message": "Привет от Bot A"}'

powershell

Invoke-RestMethod -Uri "https://srvfree.duckdns.org/send" -Method POST -Headers @{ "X-API-Key" = "123" } -ContentType "application/json; charset=utf-8" -Body '{"message": "Привет от Windows"}'


bat

@echo off

powershell -NoProfile -ExecutionPolicy Bypass -Command "$payload = @{ message = 'Привет от Windows' } | ConvertTo-Json; Invoke-RestMethod -Uri 'https://srvfree.duckdns.org/send' -Method POST -Headers @{ 'X-API-Key'='123' } -ContentType 'application/json; charset=utf-8' -Body $payload"

pause


