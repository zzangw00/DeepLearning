def mul_arr(A, B):
    arr = []
    for i in range(len(A)):
        arr.append(A[i] * B[i])
    return arr
if __name__ == '__main__':
    A = [1, 2, 3]
    B = [4, 5, 6]
    print(mul_arr(A, B))