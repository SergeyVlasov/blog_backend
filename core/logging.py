import logging

logger = logging.getLogger("apps")

def log_action(message: str):
    logger.info(message)
