def main():
    user_input=input("kindly Enter In Camel Case Without Spaces: ")
    str_L=snake_case(user_input)
def snake_case(camel_case):
    N=[]
    for index,letter in enumerate(camel_case):
            #list of indices of all the capital letters in user_input
        if letter.isupper():
            N.append(camel_case.index(letter))




    L=list(camel_case)
    correction=0
    for indices in N:
        if indices!=0:

            L.insert(indices+correction,"_")
            correction+=1
    str_L = ''.join(L)
    str_L=str_L.lower()
    print(str_L)
    return str_L
main()
