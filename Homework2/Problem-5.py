def solution(before_arr):
    after_arr = []
    for i in range(len(before_arr)):
        for j in range(len(before_arr)):
            if before_arr[j] == min(before_arr):
                after_arr.append(before_arr[j])
                before_arr[j] = 999
                break
    print(after_arr)

if __name__ == '__main__':
    before_arr = [7, 1, 10, 4, 6, 9, 2, 8, 15, 12, 17, 19, 18]
    solution(before_arr)