print("Enter the Total Income of the year: ")
total__amount=int(input())
taxable_amount=total__amount-18201
a=(taxable_amount*19) / 100
b= (5092+(taxable_amount*32.5) / 100)
c= (29467+ (taxable_amount*37) / 100)
d= (51667+ (taxable_amount*45)/100)


if total__amount <= 18200:
    {
        
        print("Your Total Payable Tax :", taxable_amount)
    }

elif total__amount >18200 and total__amount <=45000:
    {
        # a=((taxable_amount)*19)/100
        print("Your Total Payable Tax :", a )
    }
elif total__amount > 45000 and total__amount <=120000:
    {
        print("Your Total Payable Tax :", b)
    }
elif total__amount > 120000 and total__amount <= 180000:
    {
        print("Your Total Payable Tax :", c)
    }
elif total__amount >180000:
    {
        print("Your Total Payable Tax :", d)
    }

else:
    {
        print("Please re-check your tax details: Error Detected ")
    }
