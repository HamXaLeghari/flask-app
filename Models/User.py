from Configurations.DatabaseConfig import DatabaseConfig as db
from .Post import Post


class User(db.conn.Model):
    
    __tablename__ = 'users'
    
    id = db.conn.Column('id',db.conn.Integer,primary_key=True)
    username = db.conn.Column('username',db.conn.String(100),unique=True,nullable=False)
    password = db.conn.Column('password',db.conn.String(255))
    created_at = db.conn.Column('created_at',db.conn.DateTime, server_default=db.conn.func.now())
    updated_at = db.conn.Column('updated_at',db.conn.DateTime, server_default=db.conn.func.now(), server_onupdate=db.conn.func.now())

    posts = db.conn.relationship(Post, backref='user',lazy=True)
    
    
    def __init__(self,username,password,id=None):
        
        super().__init__()
        self.id = id
        self.username = username
        self.password = password
        
        
    def toDict(self):
        return  {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'posts': [post.to_dict() for post in self.posts]
        } 
        
    