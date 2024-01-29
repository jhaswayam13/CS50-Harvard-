def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars*percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d.replace("$","")
    d=float(d)
    d=float(f"{d:.1f}")
    return d



def percent_to_float(p):
    p=p.replace("%","")
    p=float(p)
    p=p/100
    return p


main()
