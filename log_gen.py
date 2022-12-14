import logging
import random

logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
for i in range(0, 30):
    x = random.randint(0, 2)
    if(x == 0):
        logging.warning('Log Message')
    elif(x == 1):
        logging.critical('Log Message')
    else:
        logging.error('Log Message')
