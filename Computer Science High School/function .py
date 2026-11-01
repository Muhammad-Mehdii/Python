def odd_num():
    product =1
    for i in range(1,20,2):
        product=product*i
    return product
def even_number():
    product=1
    for i in range (2,21,2):
        product= product*i
    return product
odd=odd_num()
even=even_number()
print("sum of odd num less then 20 :",odd)
print("sum of even num less then 20 :",even)
print("Differena", even-odd)

