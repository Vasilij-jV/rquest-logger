log_config = {
    "version": 1,
    "formatters": {
        "response_formatter": {
            "format": "%(levelname)s: %(message)s"
        },
    },
    "handlers": {
        "success_handler": {
            "class": "logging.FileHandler",
            "formatter": "response_formatter",
            "filename": "success_responses.log",
            "encoding": "UTF-8",
        },
        "bad_handler": {
            "class": "logging.FileHandler",
            "formatter": "response_formatter",
            "filename": "bad_responses.log",
            "encoding": "UTF-8",
        },
        "blocked_handler": {
            "class": "logging.FileHandler",
            "formatter": "response_formatter",
            "filename": "blocked_responses.log",
            "encoding": "UTF-8",
        },
        "timeout_handler": {
            "class": "logging.FileHandler",
            "formatter": "response_formatter",
            "filename": "timeout_responses.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "success": {
            "handlers": ["success_handler"],
            "level": "INFO",
        },
        "bad": {
            "handlers": ["bad_handler"],
            "level": "WARNING",
        },
        "blocked": {
            "handlers": ["blocked_handler"],
            "level": "ERROR",
        },
        "timeout_error": {
            "handlers": ["timeout_handler"],
            "level": "ERROR",
        },
    }
}