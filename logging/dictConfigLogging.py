import logging
from logging.config import dictConfig

config={
    'version':1,

    'formatters':{
        'standard':{
            'format':"%(asctime)s %(levelname)-10s: %(name)s - %(lineno)d %(message)s",
            'datefmt':"%Y-%m-%d %H:%M:%S"
            }
        },

    'handlers':{
        'default':{
            'level':"DEBUG",
            'formatter':'standard',
            'class':'logging.StreamHandler',
            'stream':"ext://sys.stdout"
            },
        'filehandler':{
            'level':"WARNING",
            'formatter':'standard',
            'class':'logging.FileHandler',
            'filename':"dictConfigLogs.log",
            'mode':'w'
            }
        },

    'loggers':{
        "":{
            'level':"DEBUG",
            'handlers':['default','filehandler'],
            'propagate':True
            },
        "siddharth":{
            'level':"INFO",
            'handlers':['default'],
            'propagate':False
            }
        }
    }

dictConfig(config)


def main() -> None:
    logging.debug("this is debug message")
    logging.info("this is info message")
    logging.warning("this is warning message")
    logging.error("this is error message")
    logging.critical("this is critical message")

    sidLogger = logging.getLogger('siddharth')
    sidLogger.debug("this is debug message")
    sidLogger.info("this is info message")
    sidLogger.warning("this is warning message")
    sidLogger.error("this is error message")
    sidLogger.critical("this is critical message")

if __name__=="__main__":
    main()

