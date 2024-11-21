import random
try:
    f = open("lines.txt", "r", encoding="utf-8")
    data = f.read().split("\n")
    if len(data) > 0:
        random.shuffle(data)
        print(data[0])

except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")