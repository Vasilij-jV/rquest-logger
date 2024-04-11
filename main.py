import requests as rq
import logging.config
import logging
from log_settings import log_config

logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

loggers_name = ["success", "bad", "blocked", "timeout_error"]

logging.config.dictConfig(log_config)

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger = logging.getLogger(f'{loggers_name[0]}')
            logger.info(f'{site}, response - {response.status_code}')
        elif response.status_code != 200:
            logger = logging.getLogger(f'{loggers_name[1]}')
            logger.warning(f'{site}, response - {response.status_code}')
    except rq.ConnectionError:
        logger = logging.getLogger(f'{loggers_name[2]}')
        logger.error(f'{site}, response - NO CONNECTION')
    except rq.Timeout:
        logger = logging.getLogger(f'{loggers_name[3]}')
        logger.error(f'{site}, response - истекло время ожидания')
