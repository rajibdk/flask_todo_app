from flask import Flask, jsonify, request, Response
import json
from settings import app
import jwt
import datetime

app.config['SECRET_KEY'] = 'hello'

books = [
    {
        "name": "Python Programming",
        "price": 440,
        "isbn": "1234-12-33"    
    },
    {
        "name": "Java Programming",
        "price": 340,
        "isbn": "1234-12-345"
    }
]

def isValidBook(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route("/login")
def get_token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route("/books", methods = ['GET'])
def getBooks():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'error': 'Invalid token passed'})
    return jsonify(books)

@app.route("/books", methods = ['POST'])
def add_books():
    new_book = request.get_json()
    if isValidBook(new_book):
        books.insert(0, new_book)
        return "True"
    else:
        invalidRequest = {
            "error": "Invalid request parameter",
            "help": "Try with a valid JSON structure"
        }
        return Response(json.dumps(invalidRequest), status=400, mimetype="application/json")
        

@app.route("/books/<string:isbn_no>", methods = ['GET'])
def getBookByIsbn(isbn_no):
    for book in books:
        if book["isbn"] == isbn_no:
            return jsonify(book)
    
    invalidIsbn = {
        "error": "ISBN number is not valid",
        "help": "Try with a valid number"
    }
    return Response(json.dumps(invalidIsbn), status=404, mimetype="application/json")

@app.route("/books/<string:isbn_no>", methods = ['PUT'])
def updateBooks(isbn_no):
    book_to_update = request.get_json()
    updated_book = {
        "name": book_to_update["name"],
        "price": book_to_update["price"],
        "isbn": isbn_no
    }

    i = 0
    for book in books:
        if book["isbn"] == isbn_no:
            books[i] = updated_book
        i += 1 

    print(books)
    return Response("", status=202)

@app.route("/books/<string:isbn_no>", methods = ['PATCH'])
def updateBookDetails(isbn_no):
    request_data = request.get_json()
  
    updated_book = {}
    if("name" in request_data):
        updated_book["name"] = request_data["name"]
    if("price" in request_data):
            updated_book["price"] = request_data["price"]
   
    for book in books:
        if(isbn_no == book["isbn"]):
            book.update(updated_book)
   
    reponse = Response("", 204) 
    reponse.headers["Location"] = "/books/" + isbn_no
    return reponse 

@app.route("/books/<string:isbn_no>", methods = ['DELETE'])
def deleteBook(isbn_no):
    i = 0
    for book in books:
        if(isbn_no == book["isbn"]):
            books.pop(i)
            return Response("", status=204)
        i += 1
    return Response("", status=404)

if(__name__ == "__main__"):
    app.run()