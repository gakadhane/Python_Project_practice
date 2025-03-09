import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()



import multiprocessing

def square_numbers():
    for i in range(5):
        print(i * i)

process = multiprocessing.Process(target=square_numbers)
process.start()
process.join()





import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('This is an info message.')
logging.error('This is an error message.')