import datetime

from customer_support.domain.models import Complaint


class ComplaintService:

    def find(self):
        complaints = [
            Complaint(id=666, mobile=666666666, barcode=8400000000017, description='Description',
                      registration_date=datetime.datetime.now()),
            Complaint(id=666, mobile=666666666, barcode=8400000000017, description='Description',
                      registration_date=datetime.datetime.now()),
            Complaint(id=666, mobile=666666666, barcode=8400000000017, description='Description',
                      registration_date=datetime.datetime.now()),
        ]
        return complaints

    def create(self, complaint: Complaint):
        return complaint

    def read(self, _id: int):
        return Complaint(id=_id, mobile=666666666, barcode=8400000000017, description='Description',
                         registration_date=datetime.datetime.now())

    def update(self, _id: int, complaint: Complaint):
        print("PUT " + str(_id))
        return complaint

    def delete(self, _id: int):
        print("DELETE " + str(_id))
        return None


service = ComplaintService()

