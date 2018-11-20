import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

from flask import Flask,  jsonify, abort, request, make_response
#from Book import booklist
#import sys

#sys.path.append('C:\PythonProjects\JSONExamples\local\Lib\site-packages\SQLAlchemy-1.2.10.dist-info')

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Json.db'

db = SQLAlchemy(app)

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
def __str__():
       pass




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('JsonEx.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM JsonEx;').fetchall()

    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('JsonEx.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
