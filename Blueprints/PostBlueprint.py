from flask import Flask, current_app as app, Blueprint, redirect, render_template, url_for, request, Response, session, flash, jsonify,g
from werkzeug.security import  generate_password_hash, check_password_hash
from ..Services.PostService import PostService
from ..Models.Post import Post

   
postBp = Blueprint('postBp',__name__,url_prefix='/post',template_folder='templates',static_folder='static')



@postBp.route('/index',methods=['GET']) 
def index():
   
    postService : PostService = app.PostService
    
    posts = postService.findAll()
    
    return render_template('note_index.html',posts=posts) 


@postBp.route('/view/<int:post_id>',methods=['GET']) 
def view(post_id):
    
    postService : PostService = app.PostService
    
    post = postService.findById(post_id)
      
    return render_template('post_view.html',post=post)
    

@postBp.route('/create',methods=['GET']) 
def createView():
    
    return render_template('note_create.html') 


@postBp.route('/create',methods=['POST']) 
def create():
    
    postService : PostService = app.PostService
    
    payload = request.form
    
    postService.addOrUpdate(Post(payload["title"],payload["body"],g.user.id))
    
    flash(f'Post created successfully: {payload["title"]}','success')
    
    return redirect(url_for('postBp.index'))


@postBp.route('/update/view/<int:post_id>',methods=['GET'])
def updateView(post_id):
    
      postService : PostService = app.PostService
      
      post = postService.findById(post_id)
      
      return render_template('note_update.html',post=post)
    

@postBp.route('/update',methods=['POST']) 
def update():
    
    postService : PostService = app.PostService
    
    payload = request.form
    
    post = postService.findById(payload["id"])
    
    post.title = payload["title"]
    post.body = payload["body"]
    post.user.id = g.user.id
    
    postService.addOrUpdate(post=post)
    
    flash(f'Post Updated successfully: {payload["title"]}')
    
    return redirect(url_for('postBp.index'))


@postBp.route('/delete/<int:post_id>',methods=['GET']) 
def delete(post_id):
    
    postService : PostService = app.PostService
    
    postService.delete(post_id)
    
    flash(f'Post deleted successfully','success')
    
    return redirect(url_for('postBp.index'))  
