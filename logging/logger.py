import logging


logging.basicConfig(
    filename="example2.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug("This will get debugged")
logging.info("This will get uuiiinfoed")
logging.warning("This will get warned")
logging.error("This will get errored")
logging.critical("This will get criticaled")