from fastapi import APIRouter

from customer_support.domain.models import Complaint
from customer_support.domain.services.complaint import service

router = APIRouter(
    prefix="/complaints",
    tags=["complaints"],
)


@router.get("/search")
def find():
    return service.find()


@router.post("/")
def create(complaint: Complaint):
    return service.create(complaint)


@router.get("/{_id}")
def read(_id: int):
    return service.read(_id)


@router.put("/{_id}")
def update(_id: int, complaint: Complaint) -> Complaint:
    return service.update(_id, complaint)


@router.delete("/{_id}")
def delete(_id: int):
    return service.delete(_id)
