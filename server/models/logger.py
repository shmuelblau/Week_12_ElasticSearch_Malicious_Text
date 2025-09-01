import functools
import logging

def get_logger():
    logger = logging.getLogger("console_logger")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%d-%m-%Y %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

log = get_logger()

def Logger(_func=None, *, log_start=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if log_start:
                log.info(f"start func: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                if log_start:
                    log.info(f" finish func: {func.__name__}")
                return result
            except Exception as e:
                log.error(f"{func.__name__}: {e}", exc_info=True)
                raise
        return wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)
