units=int(input("Kindly enter the number of units consumed: "))

if (units<50):
    amount=units*2.60
    tax=25

elif(units<=100):
    amount=130+((units-50)*3.25)
    tax=35

elif(units<=200):
    amount=130+162.5+((units-100)*5.26)
    tax=45

else:
    amount=130+162.5+526+((units-200)*8.45)
    tax=75


total=amount+tax
print("\nElectricity Bill=%.2f₹" %total)