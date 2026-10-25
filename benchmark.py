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

_cached_version = platform.python_version()

def test():
    v1 = _cached_version
    v2 = _cached_version
    return v1, v2
"""

def main():
    baseline = timeit.timeit("test()", setup=setup_baseline, number=100000)
    optimized = timeit.timeit("test()", setup=setup_optimized, number=100000)

    print(f"Baseline:  {baseline:.4f}s")
    print(f"Optimized: {optimized:.4f}s")
    print(f"Improvement: {(baseline - optimized) / baseline * 100:.2f}%")

if __name__ == "__main__":
    main()
