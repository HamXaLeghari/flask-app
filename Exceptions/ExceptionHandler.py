
from flask import Flask
from sqlalchemy.exc import SQLAlchemyError
import uuid
import traceback as tb
from werkzeug.exceptions import HTTPException

class ExceptionHandler:
    
    errorResponse = {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred. Please check the logs for details."
        }
    
    logMessage = "Log ID: {logId} - Exception occurred: {message}"
    
    logMessageWithTrace = "Log ID: {logId} - Exception occurred: {message} - Trace: {trace}"


    def __init__(self, app : Flask):
               
            self.app = app
           # app.register_error_handler(Exception, self.handleBaseExceptions)
            #app.register_error_handler(SQLAlchemyError, self.handleDatabaseExceptions)

    
    def handleBaseExceptions(self, e: Exception):
        
        logId = self.logError(e)
        
        return {**self.errorResponse, "log ID": logId}, 500

    
    def handleDatabaseExceptions(self, e: SQLAlchemyError):
        
        logId = self.logError(e)    
        
        return {**self.errorResponse, "log ID": logId}, 500
    
    def handleHttpExceptions(self, e : HTTPException):
    
        logId = self.logError(e)
        
        return {"error": e.name,  "message": e.description, "log ID": logId },e.code 
    
   
    def logError(self, e: Exception) -> str:
        
        logId = uuid.uuid4().hex
        
        if not isinstance(e, HTTPException): 
           message = self.logMessageWithTrace.format(logId=logId, message=e, trace=tb.format_exc())
        else:
            message = self.logMessage.format(logId=logId,message=e)
        
        self.app.logger.error(message)
        
        return logId
        
        
        
        
        
        
        
        
        
        
        