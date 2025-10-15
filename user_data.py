from dataclasses import dataclass


@dataclass()
class UserData:
    id: int
    username: str
    firstname: str
    lastname: str
    phone_number: str | None

    def to_dict(self):
        return dict(id=self.id,
                    username=self.username,
                    firstname=self.firstname,
                    lastname=self.lastname,
                    phone_number=self.phone_number)
