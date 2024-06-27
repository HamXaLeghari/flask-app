import os
from flask import Flask,render_template,redirect,url_for,current_app
from flask_migrate import Migrate
from .Configurations.DatabaseConfig import DatabaseConfig as dbConfig


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
    
    app.UserService = UserService(db)
    
    from .Blueprints.UserBlueprint import userBp
    
    app.register_blueprint(userBp)
    
    
    @app.route('/',methods=['GET'])
    def index():
        return redirect(url_for('userBp.index'))
    
    
    return app;