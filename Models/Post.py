from Configurations.DatabaseConfig import DatabaseConfig as db
from flask_sqlalchemy import SQLAlchemy
class Post(db.conn.Model):
   
    __tablename__ = 'posts'
    
    id = db.conn.Column('id', db.conn.Integer, primary_key=True)
    title = db.conn.Column('title', db.conn.String(200))
    body = db.conn.Column('body', db.conn.Text)
    created_at = db.conn.Column('created_at', db.conn.DateTime, server_default=db.conn.func.now())
    updated_at = db.conn.Column('updated_at', db.conn.DateTime, server_default=db.conn.func.now(), server_onupdate=db.conn.func.now())
    user_id = db.conn.Column('user_id', db.conn.Integer, db.conn.ForeignKey('users.id'), nullable=False)
    
    
    def __init__(self, title, body, user_id, id=None):
      
        super().__init__()
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
        
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user_id': self.user_id
        }
    
    