# def decorator_fn(other_fn):
#     def inner_fn(*args, **kwargs):
#         print('This was run before {}'.format(other_fn.__name__))
#         return other_fn(*args, **kwargs)
#     return inner_fn 

class decorator_class(object):
    def __init__(self, other_fn):
        self.other_fn = other_fn

    def __call__(self, *args, **kwargs):
        print("call was printed before {}".format(self.other_fn.__name__))
        return self.other_fn(*args, **kwargs)
@decorator_class
def new_fn():
    print('This is what is used by decorator function')

@decorator_class
def my_name(name, age):
    print('My name is {} and I am {} yrs old'.format(name, age))


new_fn()
my_name('Nelson', 24)