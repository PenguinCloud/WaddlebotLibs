import logging

# Usage Example: 
# from botLogger import BotLogger       # This will import the BotLogger class
# mylog = BotLogger(logFile="bot.log")  # This will create a logger with the name WaddleBot and logfile to bot.log
# mylog.fileLogger()                    # This will create a file handler for the logger, defaults to console
# log = mylog.logger                    # This will get the logger object with both file and console handler now
# log.info("This is a test message")    # This will log the message to the file

# ---------------------
# This is a class which will handle all logging for the bot
# ---------------------
class BotLogger:
    def __init__(self, logname: str = "WaddleBot", logFile: str = "/var/log/waddlebot.log"):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.INFO)
        self.callFunction = self.caller()
        self.logFile = logFile
    
    # ---------------------
    # This is a function which will set the handler name to the caller function
    # ---------------------
    def caller(self) -> None:
        from inspect import stack
        try:
            self.callFunction = stack()[2][3]
        except Exception:
            self.logger.debug("Unable to get the caller 2 levels up, tryin 1 level up!")
        if len(self.callFunction) < 2:
            self.callFunction = stack()[1][3]
    
    # ---------------------
    # This is a function which will create a logger using file handler
    # ---------------------
    def fileLogger(self):
        file_handler = logging.FileHandler(self.logFile)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
    
    # ---------------------
    # This is a function which will create a logger using syslog handler
    # ---------------------
    def syslogLogger(self):
        syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
        syslog_handler.setLevel(logging.INFO)
        syslog_handler.setFormatter(
            logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(syslog_handler)
    
    # ---------------------
    # This is a function which will create a logger using file handler with JSON format
    # ---------------------
    def fileJSONLogger(self):
        json_handler = logging.FileHandler(self.logFile)
        json_handler.setLevel(logging.INFO)
        json_handler.setFormatter(
            logging.Formatter('{"function": "%(name)s", "level": "%(levelname)s", "rawMsg": "%(message)s"}'))
        self.logger.addHandler(json_handler)
        
    # ---------------------
    # this is a functin which will change the logging level
    # ---------------------
    def changeLevel(self, level):
        self.logger.setLevel(level)
