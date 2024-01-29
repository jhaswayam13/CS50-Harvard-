deep_question=input("What is the answer to the Great Question of Life, the Universe and Everything?: ")
deep_question=deep_question.lower().strip()


list=["42","forty two","forty-2","forty-two"]
if deep_question in list:

    print("yes")
else:
    print("No")
