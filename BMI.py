weight=float(input("vazn khod ra vared  konid(kg): "))
height=float(input('ghad khod ra vared konid(m): '))
BMI=weight/(height**2)
print(f'bmi shoma {BMI} ast.')
if BMI <= 18.5 :
    print('shoma kambood vazn darid')
elif 18.5 <= BMI <= 24.9:
    print('vazn shoma normal ast')
elif 25 <= BMI <= 29.9:
    print('shoma ezafe vazn darid')
else:
    print('shoma chagh hastid')