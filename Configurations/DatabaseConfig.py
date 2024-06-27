from flask_sqlalchemy import SQLAlchemy
from os import environ
from class_utils import typed_property

class DatabaseConfig:
   
    conn: SQLAlchemy = None
    
    DB_USER = environ.get('MARIADB_USER')
    DB_PASSWORD = environ.get('MARIADB_PASSWORD')
    DB_HOST = environ.get('MARIADB_HOST','127.0.0.1')
    DB_PORT = environ.get('MARIADB_PORT',3306)
    DB_NAME = environ.get('MARIADB_DATABASE','blog')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    SECRET_KEY=environ.get('SECRET_KEY')
    
    @classmethod         
    def create_instance(cls) -> SQLAlchemy:
        if cls.conn is None:
            cls.conn = SQLAlchemy()
        return cls.conn
    
    