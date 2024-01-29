def main():
    samay = input("Enter time u wanna seek the food for ;)")
    num_con=convert(samay)
    if 7.0<=num_con<=8.0:
        print("breakfast time")
    elif 12.0<=num_con<=13.0:
        print("lunch time")
    elif 18.0<=num_con<=19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    time = time.strip().partition(":")
    time = list(time)
    for i in range(0, 3, 2):
        time[i] = float(time[i])
    value = time[0]+(time[2]/60)
    num_con = f"{value:.2f}"
    num_con = float(num_con)
    return num_con



if __name__ == "__main__":
    main()

