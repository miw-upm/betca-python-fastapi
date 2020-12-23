import datetime

from pydantic import BaseModel


class Complaint(BaseModel):
    id: int
    mobile: int
    barcode: str
    description: str
    registration_date: datetime.datetime
