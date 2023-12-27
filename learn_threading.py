# %%
import time
import threading
# %%

def calc_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i**2
    print(f"Sum of squares from 0 to {n} is {sum_squares}")

def sleep_a_little(seconds):
    time.sleep(seconds)

# %%
def main():
    calc_start = time.perf_counter()

    current_threads = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        t = threading.Thread(target=calc_sum_squares, args=(maximum_value, ), daemon=True)
        t.start()
        current_threads.append(t)
        # calc_sum_squares((i + 1) * 1000000)

    for thread in current_threads:
        thread.join()
    print(f"Time elapsed for calc_sum_square: {time.perf_counter() - calc_start:.2f} seconds")

    sleep_start = time.perf_counter()

    current_threads = []
    for second in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(second, ), daemon=True)
        t.start()
        # t.join() # blocks execution until each thread is finished. An equivalent of sequential program.
        current_threads.append(t)

    # Now we wait to start all threads at once before we block each of them
    for thread in current_threads:
        thread.join()
        # sleep_a_little(i)
    print(f"Time elapsed for sleeping: {time.perf_counter() - sleep_start:.2f} seconds")


if __name__ == '__main__':
    main()
