import logging

log_file = "auto_complete.log"
def get_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and add it to the logger
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Remove any existing handlers from the logger
    for existing_handler in logger.handlers:
        logger.removeHandler(existing_handler)

    # Add the new handler to the logger
    logger.addHandler(handler)

    return logger