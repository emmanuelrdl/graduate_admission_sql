from app import db

class Result(db.Model):
    __tablename__ = "linregresults"

    id = db.Column(db.Integer, primary_key = True)
    yearsexperience = db.Column(db.Float)
    prediction = db.Column(db.Float)

    def __init__(self, YearsExperience, Prediction):
        self.yearsexperience = YearsExperience
        self.prediction = Prediction

    def __repr__(self):
        return '<id {}>'.format(self.id)
