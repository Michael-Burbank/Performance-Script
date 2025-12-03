# Imported libraries
import time
import requests

URL = "https://www.tattoosbyeder.com"


def check_http_health():
    # Latency test
    start_time = time.perf_counter()
    try:
        response = requests.get(
            URL, timeout=10, headers={"Cache-Control": "no-cache"}
        )
    except requests.RequestException as error:
        end_time = time.perf_counter()
        elapsed_seconds = end_time - start_time
        elapsed_ms = elapsed_seconds * 1000
        elapsed_us = elapsed_seconds * 1_000_000
        print(
            f"Performance test failed: {URL} is not reachable. Error: "
            f"{error}"
        )
        print(f"Response time: {elapsed_ms:0.2f} ms ({elapsed_us:.2f})")
        return

    end_time = time.perf_counter()
    elapsed_seconds = end_time - start_time
    elapsed_ms = elapsed_seconds * 1000
    elapsed_us = elapsed_seconds * 1_000_000

    if response.status_code == 200:
        print(f"Performance test passed: {URL} is reachable.")
        print(f"Response time: {elapsed_ms:.2f} ms ({elapsed_us:0.2f})")
    elif response.status_code == 404:
        print(f"Performance test failed: {URL} returned 404 Not Found.")
        print(f"Response time: {elapsed_ms:.2f} ms ({elapsed_us:0.2f})")
    elif response.status_code == 505:
        print(
            "Performance test failed: 505 HTTP Version Not Supported for "
            f"{URL}."
        )
        print(f"Response time: {elapsed_ms:.2f} ms ({elapsed_us:0.2f})")
    else:
        print(
            "Performance test returned unexpected status code "
            f"{response.status_code} for {URL}."
        )
        print(f"Response time: {elapsed_ms:.2f} ms ({elapsed_us:0.2f})")

# if __name__ == '__main__':
#     http_health_check.check_http_health()