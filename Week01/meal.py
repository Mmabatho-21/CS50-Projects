def main():
    time = input("Enter the current time: ")
    hours = convert(time)
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60
if __name__ == "__main__":
    main()
