from flask import render_template, redirect, session, request, flash
from flask_app.models.recipe import Recipe
from flask_app import app
@app.route("/newRecipe")
def newRecipe():
    return render_template("create_recipe.html")
@app.route("/newRecipe/process", methods=["POST"])
def process_recipe():
    if not Recipe.recipe_validation(request.form):
        return redirect("/newRecipe")
    data = {
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_30_minutes":request.form["under_30_minutes"],
        "user_id":session["id"]
    }
    Recipe.save(data)
    return redirect("/dashboard")
@app.route("/editRecipe/<int:id>")
def editRecipe(id):
    data = {"id":id}
    recipe = Recipe.get_one(data)
    return render_template("edit.html", recipe = recipe[0])
@app.route("/editRecipe/<int:id>/process", methods=["POST"])
def processEdit(id):
    if not Recipe.recipe_validation(request.form):
        return redirect(f"/editRecipe/{id}")
    data = {
        "id":id,
        "name" : request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_30_minutes":request.form["under_30_minutes"]
    }
    Recipe.update(data)
    return redirect(f"/recipe/{id}")
@app.route("/recipe/<int:id>")
def Viewrecipe(id):
    data = {"id":id}
    recipe = Recipe.get_one(data)
    return render_template("recipe.html", recipe = recipe[0])
@app.route("/recipe/<int:id>/delete")
def delete(id):
    data = {"id":id}
    Recipe.delete(data)
    return redirect ("/dashboard")
