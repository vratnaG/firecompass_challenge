from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_person,
    retrieve_persons,
    retrieve_person,
    add_lobby,
    retrieve_lobbys,
    retrieve_lobby,
    add_winner,
    retrieve_winners,
    retrieve_deducted_amount,
)
from ..models.lotery import (
    ErrorResponseModel,
    ResponseModel,
    PersonSchema,
    LobbySchema,
    WinnersSchema,
    DeductionSchema,
)

router = APIRouter()


@router.post("/person/", response_description="person data added into the database")
async def add_person_data(person: PersonSchema = Body(...)):
    person = jsonable_encoder(person)
    print(person)
    new_person = add_person(person)
    return ResponseModel(new_person, "Person added successfully.")


@router.get("/person/", response_description="Persons retrieved")
async def get_persons():
    persons = retrieve_persons()
    if persons:
        return ResponseModel(persons, "Persons data retrieved successfully")
    return ResponseModel(persons, "Empty list returned")


@router.get("/person/{id}", response_description="Person data retrieved")
async def get_person_data(id: str):
    person = retrieve_person(id)
    if person:
        return ResponseModel(person, "person data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "person doesn't exist.")


@router.post("/lobby/", response_description="lobby data added into the database")
async def add_lobby_data(lobby: LobbySchema = Body(...)):
    lobby = jsonable_encoder(lobby)
    print(lobby)
    new_lobby = add_lobby(lobby)
    return ResponseModel(new_lobby, "lobby added successfully.")


@router.get("/lobby/", response_description="lobby retrieved")
async def get_lobbys():
    lobbys = retrieve_lobbys()
    if lobbys:
        return ResponseModel(lobbys, "lobbys data retrieved successfully")
    return ResponseModel(lobbys, "Empty list returned")


@router.get("/lobby/{id}", response_description="lobby data retrieved")
async def get_lobby_data(id: str):
    lobby = retrieve_lobby(id)
    if lobby:
        return ResponseModel(lobby, "lobby data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "lobby doesn't exist.")


@router.post("/winners/", response_description="winners data added into the database")
async def add_winners_data(winner: WinnersSchema = Body(...)):
    winner = jsonable_encoder(winner)
    print(winner)
    new_winner = add_winner(winner)
    return ResponseModel(new_winner, "winner added successfully.")


@router.get("/winners/", response_description="winners retrieved")
async def get_winners():
    winners = retrieve_winners()
    if winners:
        return ResponseModel(winners, "winners data retrieved successfully")
    return ResponseModel(winners, "Empty list returned")


@router.put("/entry_deduction/{id}", response_description="entry deduction")
async def put_entry(id: str, deduction: DeductionSchema = Body(...)):
    deduction = jsonable_encoder(deduction)
    print(deduction)
    new_deduction = retrieve_deducted_amount(id, deduction)
    if new_deduction:
        return ResponseModel(new_deduction, "winners data retrieved successfully")
    return ErrorResponseModel(new_deduction, 500, "not entry")
