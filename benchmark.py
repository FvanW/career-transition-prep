import timeit

setup_baseline = """
import platform

def test():
    v1 = platform.python_version()
    v2 = platform.python_version()
    return v1, v2
"""

setup_optimized = """
import platform

def test():
    v = platform.python_version()
    v1 = v
    v2 = v
    return v1, v2
"""

baseline = timeit.timeit("test()", setup=setup_baseline, number=100000)
optimized = timeit.timeit("test()", setup=setup_optimized, number=100000)

print(f"Baseline:  {baseline:.4f}s")
print(f"Optimized: {optimized:.4f}s")
print(f"Improvement: {(baseline - optimized) / baseline * 100:.2f}%")
