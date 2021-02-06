# 1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
multiplication_table = 2
while multiplication_table <= 12:
    print("   [{}]".format(multiplication_table))
    col = 1
    num = 1
    while num < 12:
        print(
            "{} * {} : {}".format(multiplication_table, num, num * multiplication_table)
        )
        num += 1
    multiplication_table += 1
    print("-----------------")

# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
for number in range(2, 13):
    for i in range(1, 13):
        result = number * i
        print("%d x %d = %d" % (number, i, result))
        print("  ")
    print("----------------------")