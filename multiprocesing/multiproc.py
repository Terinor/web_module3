from multiprocessing import Pool, cpu_count
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


def factorize(number):
    """Повертає список дільників числа."""
    return [i for i in range(1, number + 1) if number % i == 0]


@timeit
def parallel_factorize(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize, numbers)


@timeit
def sync_factorize(numbers):
    return [factorize(number) for number in numbers]


if __name__ == "__main__":
    numberes = [128000, 255000, 9999900, 10651060, 255000, 9999900, 10651060, 255000, 9999900, 10651060]
    print(cpu_count())
    # Виконання функції parallel_factorize
    results = parallel_factorize(numberes)
    results2 = sync_factorize(numberes)
