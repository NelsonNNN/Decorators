def decorator_fn(other_fn):
    def inner_fn(*args, **kwargs):
        print('This was run before {}'.format(other_fn.__name__))
        return other_fn(*args, **kwargs)
    return inner_fn 

@decorator_fn
def new_fn():
    print('This is what is used by decorator function')

@decorator_fn
def my_name(name, age):
    print('My name is {} and I am {} yrs old'.format(name, age))


new_fn()
my_name('Nelson', 24)