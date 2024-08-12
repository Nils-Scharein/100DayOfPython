import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"{func.__name__} ran in {t2} sec.)
    return wrapper

@tictoc
def this():
    time.sleep(.4)
    print("Test")

print("Done")