import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s-%(filename)s]: %(message)s")

logging.error("This is error message")

l = [1, 2]

try:
    print(l[3])
except Exception as e:
    logging.error(e)
    print(e)