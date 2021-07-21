from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Edit(BaseModel):
    content: str


class Edits(BaseModel):
    edits: List[Edit] = []
