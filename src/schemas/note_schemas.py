from pydantic import BaseModel, ConfigDict,Field
import uuid
import json
import datetime

class NoteRequest(BaseModel):
    title : str = Field(min_length = 1 , max_length = 5000)
    content : str = Field(min_length=1 , max_length=5000)

class NoteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : uuid
    title : str
    content : str
    embedding : json
    created_at : datetime.datetime
