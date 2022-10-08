from re import T
from mysqlconnection import connectToMySQL
from flask import flash

class Table:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO tables (name, location, language, comment, updated_at)"
        query += "VALUES(%(name)s, %(location)s, %(language)s, %(comment)s, NOW());"
        return connectToMySQL('tables').query_db(query, data)
    
    @classmethod
    def get_one(cls):
        query = "SELECT * FROM tables ORDER BY id DESC LIMIT 1;"
        result = connectToMySQL('tables').query_db(query)
        return Table(result[0])

    @staticmethod
    def validate_table(table):
        is_valid = True
        if len(table['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False
        if len(table['comment']) < 3:
            flash('Comment must be at least 3 characters')
            is_valid = False
        if table['location'] == "Choose...":
            print("COMMENT FALSE")
            flash('Must choose a location')
        if table['language'] == "Choose...":
            flash("Must choose a language")
        return is_valid
    



