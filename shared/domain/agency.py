import uuid

from domain.abstract_domain import AbstractDomain


class Agency(AbstractDomain):
    id: str
    name: str
    contact: str
    cnpj: str
    representative: str
    email: str

    def __init__(self, _id, _name, _contact, _cnpj, _representative, _email):
        self.id = _id
        self.name = _name
        self.contact = _contact
        self.cnpj = _cnpj
        self.representative = _representative
        self.email = _email

    @staticmethod
    def to_domain(obj):
        return Agency(
            str(uuid.uuid4()),
            obj['name'],
            obj['contact'],
            obj['cnpj'],
            obj['representative'],
            obj['email'],
        )
