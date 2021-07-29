from app import db


class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self, count) -> None:
        self.count = count

    def __repr__(self) -> str:
        return '<Count %r>' % self.count