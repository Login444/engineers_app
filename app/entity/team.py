from pydantic import BaseModel
from typing import List


class Team(BaseModel):
    id: str
    name: str
    members: List[str]
