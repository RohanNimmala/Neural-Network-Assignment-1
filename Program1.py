def fullname(first_name, last_name):
    return first_name + " " + last_name


def string_alternative(full_name):
    return full_name[::2]

def main():
    first_name = "Rohan"
    last_name = "Reddy"

    full_name = fullname(first_name, last_name)
    result = string_alternative(full_name)

    print("Full Name:",full_name)

    print("Processed string:", result)

if __name__ == "__main__":
    main()
