from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.user import User

# VIEW ALL USERS

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    context = {
        'users' : User.get_all()
    }
    return render_template("read_all.html", **context)

# Create a NEW USER

@app.route('/users/new')
def new():
    return render_template("create.html")

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

# Update User

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    context = {
        'user' : User.get_one(data)
    }
    return render_template("edit.html", **context)

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

# Show one user

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    context = {
        'user' : User.get_one(data)
    }
    return render_template("read_one.html", **context)

# delete user

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/users')