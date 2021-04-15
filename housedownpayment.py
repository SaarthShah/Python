price= 1000000
good_creditscore= False
downpayment=0
if good_creditscore:
    downpayment= 0.1 * price
else:
    downpayment= 0.2 * price

print(f'Downpayment= {downpayment}')