from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from Models.User import User
from Models.Post import Post

class PostService:
    
    def __init__(self, db : SQLAlchemy):
        self.db = db
                
        
    def findAll(self):
        return Post \
                .query \
                .join(User,Post.user_id == User.id) \
                .all()
    
            
    def findById(self,id):
        return Post \
                .query \
                .filter_by(id=id) \
                .first()       
    
    def addOrUpdate(self, post : Post):
        try:
            self.db.session.add(post)
            self.db.session.commit()
        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise

        
    def delete(self, post_id : int):
     try:
        post = self.db.session.query(Post).get(post_id)
        if post is not None:
            self.db.session.delete(post)
            self.db.session.commit()
     except SQLAlchemyError as e:
         self.db.session.rollback()
         raise
        