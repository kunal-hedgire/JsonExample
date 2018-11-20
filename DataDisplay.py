from flask import Flask,  jsonify, abort, request, make_response
from Book import booklist
import sys
#sys.path.append('C:\PythonProjects\JSONExamples\local\Lib\site-packages\SQLAlchemy-1.2.10.dist-info')
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Json.db'

#db = SQLAlchemy(app)

'''
class JsonEx(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    isbn = db.Column(db.String(100))
    title = db.Column(db.String(100))
    subtitle = db.Column(db.Integer)
    author = db.Column(db.String(100))
    published = db.Column(db.String(20))
    publisher = db.Column(db.String(10))
    pages = db.Column(db.Integer)
    description = db.Column(db.String(10))
    website = db.Column(db.String(10))

   def __init__(self,isbn,title,subtitle,author,published,publisher,pages,description,website):
       self.isbn = isbn
       self.title = title
       self.subtitle = subtitle
       self.author =  author
       self.published = published
       self.publisher = publisher
       self.pages = pages
       self.description = description
       self.website = website
'''

@app.route('/books',methods=['GET'])
def home_data():
    return jsonify({'books': booklist})

@app.route('/books/<int:id>',methods=['GET'])
def get_book(id):
    book = [book for book in booklist if book['book_id'] == id]
    print(book)
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book})

@app.route('/books', methods=['POST'])
def add_book():
    print(request.json)
    if not request.json:
        abort(400)
    book = {
        "book_id": booklist[-1]['book_id'] + 1,#server is adding the new id
        "isbn": request.json['isbn'],
        "title": request.json['title'],
        "subtitle": request.json['subtitle'],
        "author": request.json['author'],
        "published": request.json['published'],
        "publisher": request.json['publisher'],
        "pages": request.json['pages'],
        "description": request.json['description'],
        "website":request.json['website'],
    }
    booklist.append(book)
    print(booklist)
    return jsonify({'book': book}), 201


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_employee(id):
    book = [book for book in booklist if book['book_id'] == id]
    if len(book) == 0:
        abort(404)
    booklist.remove(book[0])
    return jsonify({'status': 'success'})


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    print(request.json)

    if not request.json:
        abort(400)
    book = [book for book in booklist if book['book_id'] == id]

    if len(book) == 0:
        abort(404)
    book[0]['title'] = request.json.get('title')
    return jsonify({'book': book[0]})


if __name__ == '__main__':

    app.run(debug=True,port=8081)
