from pydantic import BaseModel

class DocumentSegment(BaseModel):
    doc_id: str
    page: int
    text: str
