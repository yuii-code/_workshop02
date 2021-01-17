cafe_ao_udom_set = {
    "เพียวนม",
    "The HOME FACT",
    "Zlowpoke",
    "Milk Land",
}

# 1.จงเขียนคำสั่งเพื่อแสดงค่าของใน cafe_ao_udom_set ทั้งหมด

print(cafe_ao_udom_set)

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน cafe_ao_udom_set โดยเพิ่ม "Baannom" ลงไป

cafe_ao_udom_set = {"เพียวนม", "The Home FACT", "Zlowpoke", "Milk Land"}
cafe_ao_udom_set.add("Baannom")
print(cafe_ao_udom_set)


# 3.จงเขียนคำสั่งเพื่ออัพเดตค่าใน cafe_ao_udom_set โดยให้อัพเดต set ของ {"SaiNom's", "COFFEE DOE"} ในตัวแปร cafe_ao_udom_set
set1 = {"เพียวนม", "The Home FACT"}
set2 = {"Zlowpoke", "Milk Land"}
set3 = {"SaiNom's", "COFFEE DOE"}
set1.update(set1, set2, set3)
print(set1)

# 4.จงเขียนคำสั่งเพื่อลบค่า "เพียวนม" ออกจากตัวแปร  cafe_ao_udom_set

cafe_ao_udom_set = {
    "เพียวนม",
    "The Home FACT",
    "Zlowpoke",
    "Milk Land",
    "SaiNom's",
    "COFFEE DOE",
}
cafe_ao_udom_set.discard("เพียวนม")
print(cafe_ao_udom_set)

# 5.จงเขียนคำสั่งเพื่อสุ่มลบหนึ่งค่าในตัวแปร cafe_ao_udom_set

cafe_ao_udom_set = {
    "เพียวนม",
    "The Home FACT",
    "Zlowpoke",
    "Milk Land",
    "SaiNom's",
    "COFFEE DOE",
}
x = cafe_ao_udom_set.pop()
print(cafe_ao_udom_set)

# 6.จงเขียนคำสั่งเพื่อเคลียค่าของ cafe_ao_udom_set ทั้งหมด

cafe_ao_udom_set = {
    "เพียวนม",
    "The Home FACT",
    "Zlowpoke",
    "Milk Land",
    "SaiNom's",
    "COFFEE DOE",
}
cafe_ao_udom_set.clear()
print(cafe_ao_udom_set)