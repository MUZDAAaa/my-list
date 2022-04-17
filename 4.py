id = input("enter your employee id")
rate = float(input("enter  rate"))
hours = float(input("enter hours"))
over =(40 *rate + (hours - 40) * 1.5 * rate)
gross = hours*rate
deduction = gross*1.5
if gross > 500:
    print(deduction)
net=over+gross-deduction
print(id)
print(rate)
print(hours)
print(over)
print(gross)
print(deduction)
print(net)

