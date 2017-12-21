sal = 10000


def main():
    hike = sal + 3000
    return f"your new salary is {hike}"


def externalHike():
    hike = sal + 1000
    return f"your new salary is {hike}"


if __name__ == "__main__":
    a = main()
    print(a)
else:
    a = externalHike()
    print(a)
