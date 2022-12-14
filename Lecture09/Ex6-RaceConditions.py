import logging
import time
import concurrent.futures



class FakeDatabase:
    def __init__(self):
        self.value = 0 

    def updata(self, name):
        logging.info("Thread %s: starting update" , name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.vale = local_copy
        logging.info("Therad %s: finshing update" ,name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%M:%M:%S")


    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.updata, index)
    logging.info("Testing update. Ending value is %d.", database.value)


    