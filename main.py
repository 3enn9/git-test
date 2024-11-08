

def decor(func):
    def wrapper(*args, **kwargs):
        print('start')
        func()
        print('end')
    return wrapper

@decor
def hello():
    print('hello world')


