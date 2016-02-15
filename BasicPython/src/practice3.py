# < $240, Tax = 0%
# $241 to $480, Tax = 15% 
# > $481, Tax = 28%

#Aim is to calculate the Tax and  final amount after deducting tax 

def tax(amount):
    if amount < 240:
        print("0% tax for $",amount)
    elif amount > 240 and amount <= 480:
        t = amount * 0.15 
        print('For $',amount,', the tax is 15%. Tax = ',t)
    else : 
        t = amount * 0.28
        print('For $',amount,', the tax is 28%. Tax = ',t)
 

def netpay(grosspay):
    t1 = tax(grosspay)
    net = grosspay - t1
    print("Net amount after tax deduction is : ", net)
     
        
grosspay = input("Enter the Gross pay :")
netpay(grosspay)
    