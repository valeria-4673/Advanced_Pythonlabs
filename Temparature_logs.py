import logging
import random

FORMAT = '%(levelname)s-%(message)s C'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range (60):
    num = random.randint(20, 40)
    print(num)
    if num < 20:
        logger.debug(num)
    if (num >= 30 and num <= 35):
        logger.warning(num)
    else:    
        logger.critical(num)
