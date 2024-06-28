import os
from flask import Flask,render_template,redirect,url_for,current_app,session,g
from flask_migrate import Migrate
from .Configurations.DatabaseConfig import DatabaseConfig as dbConfig
from sqlalchemy.exc import SQLAlchemyError


def create_app(testConfig=None):
    
    app = Flask(__name__)
    
    if testConfig is None:
        app.config.from_object(dbConfig)
        
    else:
        app.config.from_mapping(testConfig)
    
    db = dbConfig.create_instance()
    
    from .Models import Post,User    
        
    db.init_app(app)
    
    migrate = Migrate(app,db)
    
        
    from .Services.UserService import UserService
    from .Services.PostService import PostService
    
    app.UserService : UserService = UserService(db)
    app.PostService : PostService = PostService(db)
    
    @app.before_request
    def loadUser():
        userId = session.get('user_id')
        
        if userId:
            g.user = app.UserService.findById(userId)
        else:
            g.user = None
    
    from .Blueprints.UserBlueprint import userBp
    from .Blueprints.PostBlueprint import postBp
    
    
    app.register_blueprint(userBp)
    app.register_blueprint(postBp)
    
    from .Exceptions.ExceptionHandler import ExceptionHandler
    
    exceptionHandler = ExceptionHandler(app)
    app.register_error_handler(Exception, exceptionHandler.handleBaseExceptions)
    app.register_error_handler(SQLAlchemyError,  exceptionHandler.handleDatabaseExceptions)
    
    @app.route('/',methods=['GET'])
    def index():
        return redirect(url_for('userBp.index'))
    
    
    return app;