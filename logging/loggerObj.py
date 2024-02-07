import logging

def main() -> None:
    logger = logging.getLogger("mylogger")
    logger.setLevel(logging.DEBUG)
    
    consoleHndlr = logging.StreamHandler()
    fileHndlr = logging.FileHandler("mylogs.log")

    formatter = logging.Formatter("%(asctime)s %(levelname)-8s Line-%(lineno)d: %(message)s")
    consoleHndlr.setFormatter(formatter)
    fileHndlr.setFormatter(formatter)

    logger.addHandler(consoleHndlr)
    #logger.addHandler(fileHndlr)

    logger.debug("this is debug message")
    logger.info("this is info message")
    logger.warning("this is warning message")
    logger.error("this is error message")
    logger.critical("this is critical message")

if __name__=="__main__":
    main()
