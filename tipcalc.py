#GATHERING INFORMATION ABOUT BILL COST AND DIVISIONS
while True :
    try :
        total = float(input('Enter the total cost of the meal: '))
    except :
        print('Please enter a numerical value. ')
        continue
    if total < 1 :
        print('Please enter a value greater than 0. ')
        continue
    break

while True :
    try :
        guests = int(input('How many guests? '))
    except :
        print('Please enter a numerical value. ')
        continue
    if guests < 1 :
        print('Please enter a value greater than 0. ')
        continue
    break

while True :
    try :
        quality = int(input('How was the quality of your service? 1 - 3: '))
    except :
        print('Please enter a numerical value. ')
        continue
    if quality > 3 or quality < 1 :
        print('Please enter a value between 1 and 3. ')
        continue
    break

#DETERMINING TIP PERCENTAGE BASED ON QUALITY
if quality == 1 :
    tip_percent = 0.15
elif quality == 2 :
    tip_percent = 0.20
elif quality == 3 :
    tip_percent = 0.25

#CALCULATING PER PERSON TIP AMOUNT
gross_tip = total * tip_percent
perperson_tip = (total / guests) * tip_percent

#PRINTING TIP PER PERSON AND GROSS TIP
print('Per-person tip: ' + str(perperson_tip) + '\nGross tip: ' + str(gross_tip))
exit()
