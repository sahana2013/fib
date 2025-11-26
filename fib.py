def fib_sum(n: int) -> int:
    
    a, b = 0, 1
    total = 0
    for i in range(n):
        total += a         
        print(a, end=' ' if i < n - 1 else '\n')
        a, b = b, a + b
    return total

def main() -> None:
    n = int(input("Enter the value: "))
    if n < 0:
        print("give a non-negative value.")
        return
    print(f"First {n} Fibonacci numbers:")
    s = fib_sum(n)
    print(f"Sum: {s}")
    
if __name__=="_main_":
    main()