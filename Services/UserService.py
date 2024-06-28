from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from ..Models.User import User
from ..Models.Post import Post

class UserService:
    
    def __init__(self, db : SQLAlchemy):
        self.db = db
                
        
    def findAll(self):
            return User \
            .query \
            .outerjoin(Post,User.id == Post.user_id) \
            .all()
    
    
    def findByUsernameAndPassword(self,username,password): # remember: password arg should be hashed
        return User \
                .query \
                .filter_by(username=username,password=password) \
                .first()
    
    def findByUsername(self,username):
        return User \
                .query \
                .filter_by(username=username) \
                .first()

            
    def findById(self,id):
        return User \
                .query \
                .filter_by(id=id) \
                .first()
                
 
    def addOrUpdate(self, user: User):
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise

        
    def delete(self, user: User):
        try:
            self.db.session.delete(user)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise
        
        