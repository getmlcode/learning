import logging

def simpleLogFilter(record: logging.LogRecord):
    if "x" in record.msg:
        return False
    return True

logger = logging.getLogger()
logger.warning("this is msg")
logger.addFilter(simpleLogFilter)
logger.warning("x this is filtered message1")

class CustomLogginFilter(logging.Filter):

    def addContext(self, data):
        self.ip = data['ip']
        self.user = data['user']

    def filter(self, record: logging.LogRecord):
        if super().filter(record):
            record.ip = self.ip
            record.user = self.user

            return True

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s %(levelname)-10s: %(name)s - %(ip)s - %(user)s - %(lineno)d %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )

cstmLogFilter = CustomLogginFilter("ApplyForm")
cstmLogFilter.addContext({"ip":"192.168.2.1",
                          "user":"siddharth"
                          })

loggerA = logging.getLogger("ApplyForm")
loggerB = logging.getLogger("ApplyForm.Now") # will be printed as it is a part of package ApplyForm
loggerC = logging.getLogger("AcceptRequest") # wont be printed as it is not part of package ApplyForm

loggerA.addFilter(cstmLogFilter)
loggerB.addFilter(cstmLogFilter)
loggerC.addFilter(cstmLogFilter)

loggerA.warning("Apply forms hurry up!!")
loggerB.warning("Apply forms hurry up!!")
loggerC.warning("Apply forms hurry up!!")