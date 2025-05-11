name = "Владислав"
age = 11
value_int = 10
value_float = 5.4523123

# < - вирівнювання за правим краєм
# > - вирівнювання за лівим краєм
# ^ - вирівнювання по центру
# s - строка
# d | n - int
# f - з плавуючую точкою
# .[кількість_цифр_після_коми]f
result = f"Привіт {name:^15s}! Тобі {age:02n} роки/років. \nvalue_int = {value_int:^10d}\nvalue_float = {value_float:0.2f}"

print(result)

print("N) Hello \nWorld!")
print("T) Hello \tWorld!")
print("B) Hello \bWorld!")
print("R) Hello \rWorld!")
print("Hello \"World!")
print('Hello \'World!')
print('Hello \\World! см')