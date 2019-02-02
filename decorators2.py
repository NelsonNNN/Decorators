from functools import wraps

def logg_in(retireved_fn):
    import logging
    logging.basicConfig(filename=('{}.log').format(retireved_fn.__name__), level=logging.INFO)
    
    @wraps(retireved_fn)
    def inner_fn(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return retireved_fn(*args, **kwargs)
    return inner_fn

def timer(retireved_fn):
    import time
    @wraps(retireved_fn)
    def in_fn(*args, **kwargs):
        t1 = time.time()
        results = retireved_fn(*args, *kwargs)
        t2= time.time() - t1
        print('{} ran in {} sec'.format(retireved_fn.__name__, t2))
        return results
    return in_fn

# @logg_in
# def outer_fn():
#     print('This ran correctly')

@timer
@logg_in

def other_outer_fn(name, seconds):
    print('This was ran by {} at {} secs'.format(name, seconds))

#outer_fn()
other_outer_fn('Hank', 3600)