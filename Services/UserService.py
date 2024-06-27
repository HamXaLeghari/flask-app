from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from ..Models.User import User
from ..Models.Post import Post

class UserService:
    
    def __init__(self, db : SQLAlchemy):
        self.db = db
                
        
    def findAll(self):
        try:
            return User \
            .query \
            .outerjoin(Post,User.id == Post.user_id) \
            .all()
            
        except Exception as e:
            app.log_exception(f'Error: {e}')
            raise
    
    def findByUsernameAndPassword(self,username,password):
        try:
            return User \
                .query \
                .filter_by(username=username,password=password) \
                .first()
            
                
        except Exception as e:
            app.log_exception(f'Error: {e}')
            raise
    
    def findByUsername(self,username):
        try:
            return User \
                .query \
                .filter_by(username=username) \
                .first()
            
                
        except Exception as e:
            app.log_exception(f'Error: {e}')
            raise
            
    def findById(self,id):
        try:
            return User \
                .query \
                .filter_by(id=id) \
                .first()
                
        except Exception as e:
            app.log_exception(f'Error: {e}')
            raise
            
    
    def addOrUpdate(self, user: User):
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except Exception as e:
            app.log_exception(f'Error: {e}')
            self.db.session.rollback()
            raise

        
    def delete(self, user: User):
        try:
            self.db.session.delete(user)
            self.db.session.commit()
        except Exception as e:
            app.log_exception(f'Error: {e}')
            self.db.session.rollback()
            raise
        
        