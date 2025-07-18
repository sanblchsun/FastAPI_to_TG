import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app:app",             # имя файла (без .py): app.py → app
        host="0.0.0.0",        # слушать на всех интерфейсах
        port=5004,             # порт
        reload=True,           # авто-перезапуск при изменениях (только для разработки)
        log_level="info"       # уровень логирования
    )
