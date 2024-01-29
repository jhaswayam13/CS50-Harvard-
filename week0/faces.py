def main():
    #🙁
    #🙂
    user_input=input("Enter your rant or happiness: ")
    emotification(user_input)

def emotification(change):
   replacements={":)":"🙂", ":(":"🙁"}
   for old, new in replacements.items():
    change = change.replace(old, new)
    print(change)







main()
