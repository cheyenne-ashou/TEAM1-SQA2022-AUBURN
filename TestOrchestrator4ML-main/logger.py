import logging

def getLogger():
    logging.basicConfig(filename='PROJECT.LOG', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H-%M-%S')
    logObj = logging.getLogger('logger')
    return logObj 