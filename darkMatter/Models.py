from darkMatter import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), unique=True)
    Attack = db.Column(db.Integer)
    Defense = db.Column(db.Integer)
    Moons = db.Column(db.Integer)
    Level = db.Column(db.Integer)

    def __repr__(self):
        return '<Planet ID#{}, Name: {}>'.format(self.id, self.Name)
