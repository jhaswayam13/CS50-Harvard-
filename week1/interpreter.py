def main():
    parameters=input("enter in x y z format(as per the instructions): ")
    print("the answer to r query is:",arithmetic(parameters))
def arithmetic(values):
    values=values.strip().split(" ")
    values=list(values)
    for i in range(0,3,2):
        values[i]=float(values[i])
    if values[1]=="+":
        return (values[0]+values[2])
    elif values[1]=="-":
        return (values[0]-values[2])
    elif values[1]=="*":
        return (values[0]*values[2])
    elif values[1]=="/":
        try:
            return (values[0]/values[2])
        except ZeroDivisionError:
            print("Cannot divide by zero!!! Please retry")
    else:
        print("the input format does not follows as per the instructions. Sure to check only one spaces between the values ")





main()
