def solution(a, b):
    bmi = b / ((a / 100)**2)
    print(bmi)
    if bmi < 18.5:
        print("저체중")
    elif bmi >= 18.5 and bmi < 23:
        print("정상")
    elif bmi >= 23 and bmi < 25:
        print("과체중")
    elif bmi >= 25 and bmi < 30:
        print("비만")
    elif bmi >= 30:
        print("고도비만")

if __name__ == "__main__":
    a = int(input("키를 입력하세요"))
    b = int(input("몸무게를 입력하세요"))
    solution(a, b)