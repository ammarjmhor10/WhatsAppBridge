from __future__ import annotations
from pyexpat.errors import messages

from typing import List, Optional

from pydantic import BaseModel, Field



class Metadata(BaseModel):
    display_phone_number: str
    phone_number_id: str


class Profile(BaseModel):
    name: str


class Contact(BaseModel):
    profile: Profile
    wa_id: str

class Audio(BaseModel):
    mime_type: str
    sha256: str
    id: str
    voice: bool

class Sticker(BaseModel):
    mime_type: str
    sha256: str
    id: str

class Text(BaseModel):
    body: str


class Image(BaseModel):
    caption: Optional[str]
    mime_type: str
    sha256: str
    id: str

class Message(BaseModel):
    from_: str = Field(..., alias='from')
    id: str
    timestamp: str
    text: Optional[Text]
    image:Optional[Image]
    audio:Optional[Audio]
    sticker:Optional[Sticker]
    type: str




class Value(BaseModel):
    messaging_product: str
    metadata: Metadata
    contacts: List[Contact]
    messages: List[Message]


class Change(BaseModel):
    value: Value
    field: str


class EntryItem(BaseModel):
    id: str
    changes: List[Change]


class Model(BaseModel):
    object: str
    entry: List[EntryItem]



