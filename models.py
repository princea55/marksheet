from marksheet import db


class Marksheet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False)
    rollno = db.Column(db.Integer, nullable=False, unique=True) 
    maths = db.Column(db.Integer, nullable=False)
    science = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)
    
    
    def __repr__(self):
        return f"Marksheet('{self.name}')"