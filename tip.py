def total_calc(billamt,tipperc):
    total=billamt*(1+0.01*tipperc)
    total=round(total,2)
    print(f"Please pay ${total}")

total_calc(190,35)