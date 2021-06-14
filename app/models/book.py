from app import db

# here is a book classs, it is a model, and it will have 3 columns
class Book(db.Model): # an instance of db = SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String) 

    # return a string with the id and title
    def __str__(self):
        return f"{self.id}: {self.title} Description {self.description}"