price=float(input("Enter the price of item:"))
quantity=int(input("Enter the numbers of item:"))
total=(price*quantity)
totalWithGst=total*0.18
print(f"Total: {total}\nTotal + GST:{totalWithGst+total}")