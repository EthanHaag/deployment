from flask_app.config.mySqlconnection import connectToMySQL
from flask import flash
class Recipe:
    name_db = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under_30_minutes = data["under_30_minutes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    @classmethod
    def save(cls, data):
        query = "insert into recipes (name,description,instructions,under_30_minutes,created_at,updated_at,user_id) values (%(name)s, %(description)s, %(instructions)s,%(under_30_minutes)s,now(),now(),%(user_id)s)"
        return connectToMySQL(cls.name_db).query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "update recipes set name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30_minutes = %(under_30_minutes)s, updated_at = now() where id = %(id)s"
        return connectToMySQL(cls.name_db).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "delete from recipes where id = %(id)s"
        return connectToMySQL(cls.name_db).query_db(query, data)
    @classmethod
    def get_one(cls, data):
        query = "select * from recipes where id = %(id)s"
        return connectToMySQL(cls.name_db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "select * from recipes"
        results = connectToMySQL(cls.name_db).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    @staticmethod
    def recipe_validation(data):
        valid = True
        if len(data["name"])<1:
            flash("Input a name for your recipe.")
            valid = False
        if len(data["description"])<10:
            flash("be more descriptive.")
            valid = False
        if len(data["instructions"])<1:
            flash("Input some instructions.")
            valid = False
            
        return valid