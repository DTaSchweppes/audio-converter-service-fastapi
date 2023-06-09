from pydantic import BaseModel, Field


class Audio(BaseModel):
    name: str
    user_id: int = Field(ge=1, le=10)


class User(BaseModel):
    name: str
