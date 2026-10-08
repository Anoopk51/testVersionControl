import logging
from typing import Optional

logger = logging.getLogger("__name__")

def divide(a:float,b:float) -> Optional[float]:
    logger.info("start logger module")
    try:
        return a / b
    except ZeroDivisionError:
        logger.warning("Cannot divide by zero.")
        return None

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    result = divide(4,0)
    logger.info("Result %s" ,result)

if __name__ == "__main__":
    main()