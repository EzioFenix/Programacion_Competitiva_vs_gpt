import time
from memory_profiler import memory_usage

def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        mem_usage_before = memory_usage(-1, interval=0.001, timeout=1)[0]
        
        result = func(*args, **kwargs)

        mem_usage_after = memory_usage(-1, interval=0.001, timeout=1)[0]
        end_time = time.perf_counter()

        print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
        print(f"Uso de memoria: {mem_usage_after - mem_usage_before:.6f} MiB")

        return result
    return wrapper
