import time

def a_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{func.__name__} виконана за {elapsed_time} сек.")
    return result

def test_a_time():
    def test_func_1():
        time.sleep(1)
        return 42

    def test_func_2(a, b):
        time.sleep(2)
        return a + b

    assert a_time(test_func_1) == 42
    assert a_time(test_func_2, 2, 3) == 5

test_a_time()