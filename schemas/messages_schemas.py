from pydantic import BaseModel, Field


class MessageRequestSchema(BaseModel):
    content: str = Field(description='Текст сообщения')


class MessageResponseSchema(BaseModel):
    id: int = Field(description='Уникальный идентификатор сообщения')
    content: str = Field(description='Текст сообщения')


messages_db: list[MessageResponseSchema] = [
    MessageResponseSchema(id=0, content='Первое сообщение в FastAPI')
]
