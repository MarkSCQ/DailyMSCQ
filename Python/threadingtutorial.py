import logging
import threading
import time


def func(name):
    logging.info("starting %s", name)
    time.sleep(2)

    logging.info("finsihing %s", name)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s" 
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("before")

    x = threading.Thread(target=func, args=(1,))
    x.start()

    logging.info("end")

    # x.join()
    logging.info("Done")


"""

parallelism

cpu speed: ghz


"""