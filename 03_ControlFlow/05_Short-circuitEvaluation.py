# 2'06

# Kad naidje na 1 ispunjeni uvjet prekida daljnju evaliaciju (ala struja kad ima ks ne ide dalje na druge otpore)
# Primjenjuje se jedanko kod svih logickih operatora i "and" i "or"

high_income = False
good_credit = True
student = True

if high_income and good_credit and student:
    print("Eligible")
    
if high_income or good_credit or student:
    print("Eligible")