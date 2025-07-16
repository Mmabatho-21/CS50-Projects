def convert(string):
    #string = "Hey there :), I have sad news for you :("
    string = string.replace(":)","🙂").replace(":(","🙁")
    return string
print(convert("Hey there :), I have sad news for you :("))

def main():
    user_input = input("Type your response here: ")
    # whatever their input is will be converted (so the emojis placed there will be replaced and saved as the result)
    result = convert(user_input)
    print(result)
main()
