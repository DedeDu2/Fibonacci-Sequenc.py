def generate_fibonacci(n):
    fibonacci_seq = [0, 1]
    for i in range(2, n):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    return fibonacci_seq

def main():
    n = int(input("Enter the number of terms: "))
    fibonacci_seq = generate_fibonacci(n)
    print("Fibonacci Sequence:", fibonacci_seq)

if __name__ == "__main__":
    main()
