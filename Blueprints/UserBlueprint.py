from flask import Flask, current_app as app, Blueprint, redirect, render_template, url_for, request, Response, session, flash, jsonify
from werkzeug.security import  generate_password_hash, check_password_hash
from ..Services.UserService import UserService
from ..Models.User import User

    
userBp = Blueprint('userBp',__name__,url_prefix='/user',template_folder='templates',static_folder='static')


@userBp.route('/index',methods=['GET'])
def index():
    return render_template('log_in.html')


@userBp.route('/signup',methods=['POST']) # FOR SEEDING ADMIN ONLY
def signup():
    
    userService : UserService = app.UserService
    
    #payload : dict = request.form.to_dict()
    
    if request.is_json:
        payload : dict = request.get_json()
    else:
        payload = request.form
    
    if userService.findByUsername(payload["username"]) is not None:
        return Response(f'Username {payload["username"]} is already taken.',400)
    
    password = generate_password_hash(payload["password"])
    
    userService.addOrUpdate(User(payload["username"],password))
    
    return Response("Signup Successful.",201)
    
    

@userBp.route('/login',methods=['GET'])
def login():
    return render_template('log_in.html')


@userBp.route('/authenticate',methods=['POST'])
def authenticate():
    if request.is_json:
        payload : dict = request.get_json()
    else:
        payload = request.form
        
    userService : UserService = app.UserService
    
    user = userService.findByUsername(payload["username"])
    
    error = None
    
    if not user or not check_password_hash(user.password,payload["password"]):
         error = "Username or password are incorrect."
    else:
        session.clear()
        session["user_id"] = user.id
        return redirect(url_for('postBp.index'))
    
    flash(error,'error')
    
    return render_template('log_in.html')

@userBp.route('/logout',methods=['GET','DELETE'])
def logout():
    session.clear()
    flash('Logout Successful','success')
    return redirect(url_for('userBp.login'))
    
     
@userBp.route('/all',methods=['GET']) # DOES NOT WORK; TO SIMULATE EXCEPTIONS ONLY
def findAll():
    
    userService : UserService = app.UserService
        
   # userList = [user.toDict() for user in userService.findAll()]
    
    #return userList,200
    return userService.findAll(), 200

    
    
    

