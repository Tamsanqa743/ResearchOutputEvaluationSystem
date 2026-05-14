import time
from functools import wraps
from datetime import datetime


class benchmark:
    """
    Benchmark utility that logs execution times to a text file.
    """

    LOG_FILE = "benchmark_logs.txt"

    @staticmethod
    def track(label=None):

        def decorator(func):

            @wraps(func)
            def wrapper(*args, **kwargs):

                benchmark_name = label or func.__name__

                start_time = time.perf_counter()

                try:
                    return func(*args, **kwargs)

                finally:

                    end_time = time.perf_counter()

                    execution_time = end_time - start_time

                    timestamp = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    log_message = (
                        f"[{timestamp}] "
                        f"{benchmark_name} executed in "
                        f"{execution_time:.6f} seconds\n"
                    )

                    # Console output
                    print(log_message.strip())

                    # File output
                    with open(benchmark.LOG_FILE, "a") as log_file:
                        log_file.write(log_message)

            return wrapper

        return decorator