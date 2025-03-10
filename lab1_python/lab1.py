def get_integer():
    while True:
        try:
            n = int(input("Введіть число: "))
            return n
        except ValueError:
            print("Помилка! Будь ласка, введіть ціле число.")


def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n = get_integer()

    sum_n = sum_numbers(n)
    fact_n = factorial(n)
    prime_status = "є простим" if is_prime(n) else "не є простим"

    print(f"Сума всіх чисел від 1 до {n}: {sum_n}")
    print(f"Факторіал {n}: {fact_n}")
    print(f"Число {n} {prime_status}.")


if __name__ == "__main__":
    main()