"""scanner_e711b5 - Retry logic."""
import time, functools, random
MODULE_TAG = "scanner_e711b5"
def retry(max_attempts=3, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try: return func(*args, **kwargs)
                except Exception as e:
                    print(f"[{MODULE_TAG}] Attempt {attempt} failed: {e}")
                    if attempt < max_attempts: time.sleep(delay)
            raise RuntimeError(f"All {max_attempts} attempts failed")
        return wrapper
    return decorator
@retry(max_attempts=3)
def unstable_operation():
    if random.random() < 0.5: raise ValueError("transient error")
    return "success"
def main():
    print(f"[{MODULE_TAG}] Testing retry logic...")
    try:
        result = unstable_operation()
        print(f"[{MODULE_TAG}] Result: {result}")
    except RuntimeError as e:
        print(f"[{MODULE_TAG}] Final error: {e}")
if __name__ == "__main__":
    main()
