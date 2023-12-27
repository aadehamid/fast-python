# %%
import time
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
    for i in range(5):
        calc_sum_squares((i + 1) * 1000000)
    # end = time.perf_counter()
    print(f"Time elapsed for calc_sum_square: {time.perf_counter() - calc_start:.2f} seconds")

    sleep_start = time.perf_counter()
    for i in range(1, 6):
        sleep_a_little(i)
    print(f"Time elapsed for sleeping: {time.perf_counter() - sleep_start:.2f} seconds")


if __name__ == '__main__':
    main()
