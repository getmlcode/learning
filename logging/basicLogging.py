import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s \t: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="basic.log"
    )

def main() -> None:

    logging.debug("this is debug message")
    logging.info("this is info message")
    logging.warning("this is warning message")
    logging.error("this is error message")
    logging.critical("this is critical message")

if __name__=="__main__":
    main()