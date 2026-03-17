from ollama import chat
from pydantic import BaseModel

class Population(BaseModel):
    total: int

class Location(BaseModel):
    lat: float
    lng: float

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]
    population: Population
    location: Location

response = chat(
    model='deepseek-r1:1.5b',
    messages=[
        {
            'role': 'user',
            'content': 'En español dime acerca de Nicaragua. Responde solo con JSON válido siguiendo el schema.'
        }
    ],
    format=Country.model_json_schema(),
)

country = Country.model_validate_json(response.message.content)

print(country.model_dump_json(indent=2))
