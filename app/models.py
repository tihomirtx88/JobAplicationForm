from . import db
from datetime import datetime

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date = db.Column(db.Date, default=datetime.utcnow)
    occupation = db.Column(db.String(80))

    def __repr__(self):
        return f"<Form {self.first_name} {self.last_name}>"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date": self.date.isoformat(),
            "occupation": self.occupation,
        }