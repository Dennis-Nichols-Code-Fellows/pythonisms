import functools
import time

# Example 1 - generator function

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


# example 2 - using a decorator to time a function call
def timeit(func):
    """A decorator that times the execution of a function."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result

    return wrapper

# Example 3 - use the timing decorator on the generator function
@timeit
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
            
for line in read_lines('story.txt'):
    print(line)


# Example 4 - using a decorator to add caching fuctionality


def cache(expiry_time):
    """A decorator that caches the results of a function for a certain amount of time."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in wrapper.cache:
                timestamp, result = wrapper.cache[cache_key]
                if time.time() - timestamp <= expiry_time:
                    return result
            result = func(*args, **kwargs)
            wrapper.cache[cache_key] = (time.time(), result)
            return result
        wrapper.cache = {}
        return wrapper
    return decorator
