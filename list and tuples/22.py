fruits = {"سیب", "گلابی", "موز","آناناس","آواکادو"}

# اگر موز در مجموعه وجود داشت، آن را حذف می‌کنیم
if "موز" in fruits:
    fruits.remove("موز")

# اگر هلو در مجموعه نبود، آن را اضافه می‌کنیم
if "هلو" not in fruits:
    fruits.add("هلو")

print(fruits)
