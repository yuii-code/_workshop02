# 3.#จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้
# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F
# และให้แสดงผลตามตัวอย่างด้านล่าง
# Enter your score: 49
# grade:  F

score = int(input("Enter your score:"))
if score >= 80:
    print("Grade: A")
elif score >= 75:
    print("Grade: B+")
elif score >= 70:
    print("Grade: B")
elif score >= 65:
    print("Grade: C+")
elif score >= 60:
    print("Grade: C")
elif score >= 55:
    print("Grade: D+")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")