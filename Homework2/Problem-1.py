def solution(n):
    for i in range(1, 10):
        print("{} * {} = {}".format(n, i, n * i))

if __name__ == "__main__":
    n = int(input())
    solution(n)