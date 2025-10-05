from fastapi import APIRouter, HTTPException

from schemas import MessageResponseSchema, messages_db, MessageRequestSchema

api_router = APIRouter(tags=['API 📝'])


@api_router.get(
    '/messages',
    summary='Прочитать все сообщения',
    response_model=list[MessageResponseSchema],
)
async def read_messages() -> list[MessageResponseSchema]:
    return messages_db


@api_router.get(
    '/messages/{message_id}',
    summary='Получить сообщение по его id',
    response_model=MessageResponseSchema,
)
async def read_message(message_id: int) -> MessageResponseSchema | None:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(
        status_code=404, detail=f'Message with id {message_id} not found.'
    )


@api_router.post(
    '/messages',
    status_code=201,
    summary='Создать новое сообщение',
    response_model=MessageResponseSchema,
)
async def create_message(
    message_create: MessageRequestSchema,
) -> MessageResponseSchema:
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = MessageResponseSchema(
        id=next_id, content=message_create.content
    )
    messages_db.append(new_message)
    return new_message


@api_router.put(
    '/messages/{message_id}',
    summary='Полностью заменить сообщение по его id',
    response_model=MessageResponseSchema,
)
async def update_message(
    message_id: int, message_update: MessageRequestSchema
) -> MessageResponseSchema | None:
    for idx, msg in enumerate(messages_db):
        if msg.id == message_id:
            updated_message = MessageResponseSchema(
                id=message_id, content=message_update.content
            )
            messages_db[idx] = updated_message
            return updated_message
    raise HTTPException(
        status_code=404, detail=f'Message with id {message_id} not found.'
    )


@api_router.delete(
    '/messages/{message_id}', summary='Удалить сообщение по его id'
)
async def delete_message(message_id: int) -> dict[str, str]:
    for idx, msg in enumerate(messages_db):
        if msg.id == message_id:
            messages_db.pop(idx)
            return {
                'detail': f'Message with id {message_id} '
                f'has been successfully deleted.'
            }
    raise HTTPException(
        status_code=404, detail=f'Message with id {message_id} not found.'
    )


@api_router.delete('/messages', summary='Удалить все сообщения')
async def delete_messages() -> dict[str, str]:
    messages_db.clear()
    return {'detail': 'Messages have been successfully deleted.'}
