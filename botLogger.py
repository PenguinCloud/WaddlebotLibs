import logging

# Usage Example: 
# mylog = botLogger.BotLogger()
# mylog.fileLogger("bot.log")
# mylog.info("This is a test message")

# ---------------------
# This is a class which will handle all logging for the bot
# ---------------------
class BotLogger:
    def __init__(self, logname: str = "WaddleBot"):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.INFO)
        self.callFunction = self.caller()
    
    # ---------------------
    # This is a function which will set the handler name to the caller function
    # ---------------------
    def caller(self):
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
    def fileLogger(self, file):
        file_handler = logging.FileHandler(file)
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
    def fileJSONLogger(self, file: str='log.json'):
        json_handler = logging.FileHandler(file)
        json_handler.setLevel(logging.INFO)
        json_handler.setFormatter(
            logging.Formatter('{"function": "%(name)s", "level": "%(levelname)s", "rawMsg": "%(message)s"}'))
        self.logger.addHandler(json_handler)
        
    # ---------------------
    # this is a functin which will change the logging level
    # ---------------------
    def changeLevel(self, level):
        self.logger.setLevel(level)
