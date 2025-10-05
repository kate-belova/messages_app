import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from handlers import routers

app = FastAPI(
    openapi_tags=[
        {'name': 'API 📝', 'description': 'API для работы с сообщениями'},
        {'name': 'Web 🌐', 'description': 'Веб-интерфейс для сообщений'},
    ]
)

app.mount('/static', StaticFiles(directory='static'), name='static')

for router in routers:
    app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
