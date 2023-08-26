fruits = {"apple": 3, "banana": 5, "orange": 2}
vegetables = {"parsley": 7, "broccoli": 4, "spinach": 2, "basil": 10}

greengroceries = {**fruits, **vegetables}  # {**dict1,**dict2,**dict3,...,**dictn}

print(greengroceries)

goods_name = input("Enter a name: ")
if goods_name in greengroceries:
    print("Quantity:", greengroceries[goods_name])
else:
    print("Not Found.")
