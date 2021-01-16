from typing import Optional

from pydantic import BaseModel, Field


class PersonSchema(BaseModel):
    Name: str = Field(...)
    Amount: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Name": "John Doe",
                "Amount": "300.0",
            }
        }


class LobbySchema(BaseModel):
    Name: str = Field(...)
    Entry_Fee: int
    Capcity: int

    class Config:
        schema_extra = {
            "example": {
                "Name": "lobby1",
                "Entry_Fee": "300",
                "Capcity": "6",
            }
        }


class WinnersSchema(BaseModel):
    Lobby_id: int
    Winner_id: int

    class Config:
        schema_extra = {
            "example": {
                "Lobby_id": "1",
                "Winner_id": "2",
            }
        }


class DeductionSchema(BaseModel):
    Lobby_id: int

    class Config:
        schema_extra = {
            "example": {
                "Lobby_id": "1",
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
