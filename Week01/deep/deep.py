question = input("What is the answer to the Great Question of Life, the universe and Everything? ")
q = question.strip().lower()
if q.isdigit() and int(q.strip()) == (42):
    print("Yes")
elif q == "forty-two" or q == "forty two":
    print("Yes")
else:
    print("No")
