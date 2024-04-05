from rich.console import Console
import rich.traceback
from typing import List

rich.traceback.install()
console = Console()


def fib(iter: int) -> List[int]:
    """Calculate the first n Fibonacci numbers"""
    if iter <= 0:
        raise ValueError("Invalid iteration amount, must be > 0")
    if iter < 2:
        return [1]
    if iter == 2:
        return [1, 1]

    fibs = [1, 1]
    for _ in range(2, iter):
        fibs.append(fibs[-1] + fibs[-2])

    return fibs


def main():
    console.print(fib(-1))


if __name__ == "__main__":
    main()
