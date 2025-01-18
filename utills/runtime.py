import time
import timeit

def runtime(func):
    """
    A decorator that measures and prints the runtime of the decorated function in milliseconds.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with added runtime measurement.

    Example:
        @runtime
        def example_function():
            # Function implementation
            pass

        example_function()
        # Output: Runtime: <time_in_milliseconds> milliseconds
    NOTE: 
        if it return something like (1.3828, 2.384838) just take it as something like 
        (0.0013883, 2.384838) which is multiply by 1000
    """
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        total = end_time - start_time
        timer = total * 1000
        print(f"Runtime: {timer} milliseconds")
        return result
    return wrapper


if __name__ == "__main__":

    @runtime
    def test_function(n):
        print("Do This")

    test_function(5)
