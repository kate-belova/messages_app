from fastapi import APIRouter, Form, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from schemas import messages_db, MessageResponseSchema

web_router = APIRouter(tags=['Web 🌐'])

templates = Jinja2Templates(directory='templates')


@web_router.get(
    '/web/messages',
    summary='Получить все сообщения через веб-интерфейс',
    response_class=HTMLResponse,
)
async def get_messages_page(request: Request):
    return templates.TemplateResponse(
        'index.html', {'request': request, 'messages': messages_db}
    )


@web_router.get(
    '/web/messages/create',
    summary='Перейти на страницу создания нового сообщения',
    response_class=HTMLResponse,
)
async def get_create_message_page(request: Request):
    return templates.TemplateResponse('create.html', {'request': request})


@web_router.post(
    '/web/messages',
    summary='Создать новое сообщение через веб-интерфейс',
    response_class=HTMLResponse,
)
async def create_message_form(request: Request, content: str = Form()):
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = MessageResponseSchema(id=next_id, content=content)
    messages_db.append(new_message)
    return templates.TemplateResponse(
        'index.html', {'request': request, 'messages': messages_db}
    )


@web_router.get(
    '/web/messages/{message_id}',
    summary='Перейти на страницу сообщения по его id',
    response_class=HTMLResponse,
)
async def get_message_detail_page(request: Request, message_id: int):
    for message in messages_db:
        if message.id == message_id:
            return templates.TemplateResponse(
                'detail.html', {'request': request, 'message': message}
            )
    raise HTTPException(status_code=404, detail='Сообщение не найдено')
