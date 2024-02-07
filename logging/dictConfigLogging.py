import logging
from logging.config import dictConfig

config={
    'version':1,

    'formatters':{
        'standard':{
            'format':"%(asctime)-10s: %(lineno)d %(message)s"
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

if __name__=="__main__":
    main()

