from app import db
from flask import Blueprint
from flask import request
from flask import make_response
from flask import jsonify # take an argument and convert it to JSON
from app.models.book import Book

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def books():
    if request.method == "GET": # if it's a GET
        title_from_url = request.args.get("title")# this code replaces the previous query all code
        if title_from_url:
            books = Book.query.filter_by(title=title_from_url)
        else:
            books = Book.query.all() # query an object on the class, the . all function will get us all the books
        # end of the new code

        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    # ... existing code for creating a new book
    
    elif request.method == "POST":
        request_body = request.get_json() # what to do if it's a post request
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])
    return {
        "success": True,
        make_response: f"Book {new_book.title} has been created"
    }, 200

#returns one book and now updates the book (PUT)
@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
        
    elif request.method == "PUT":
        form_data = request.get_json()

        try: 
            book.title = form_data["title"] # updates the model
            book.description = form_data["description"]

            # save action
            db.session.commit()
            return {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description
            }, 200
        except KeyError: # key error handeling

            return make_response("Request requires both title and description"), 400
        # return make_response(f"Book #{book.id} successfully updated") # returns a string value
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book with title {book_id} has been deleted."), 200

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response = "Hello, World!"
    return my_beautiful_response

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }, 200
    

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }, 404
#     new_hobby = "Surfing"
#     response_body["hobbies"] + new_hobby

    return response_body