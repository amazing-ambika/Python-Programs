price = int(input("Enter a Price : "))
if(price>0 and price<1000):
    print("No Discount")
elif(price>1000 and price<5000):
    print("5% discount of price is " ,price*5/100 ,"After Discount the amount is : ",price*95/100)
elif(price>5000 and price<10000):\
    print(price*10/100 ,"10% discount")
elif(price>10000 and price<20000):\
    print(price*20/100 ,"20% discount")
elif(price>20000 and price<30000):\
    print(price*30/100 ,"30% discount")
elif(price>30000 and price<40000):\
    print(price*40/100 ,"40% discount")
elif(price>40000):\
    print(price*40/100 ,"40% discount")
else:
    print("Invalid Prize")
exit()

# QUESTION upto 1000 = no discount
# 1000-5000 = 5% discount
# 5000-10,000 = 10% discount
# 10,000-20,000 = 20% discount
# 20,000-30,000= 30% discount
# 30,000-40,000= 40%
# 40,000= 50%
