school = input("What is the name of your high school? ")
if len(school.split()) < 2:
    print("Name of school should be more than two words")
else:
    school = school.replace(" ","...")
print(school)
