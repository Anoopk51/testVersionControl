import logging

logging.basicConfig(
    level=logging.INFO
    )

logger = logging.getLogger("__name__")

def divide(a,b):
    logger.info("start logger module")
    try:
        result = a/b
        logger.info("divide successfull.")
        return result
    
    except ZeroDivisionError as z:
        logger.info("can't devide by zero because ")
        print(z)


divide(4,0)