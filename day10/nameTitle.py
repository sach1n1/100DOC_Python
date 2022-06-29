def format_name(fname, lname):
    """Returns formatted name when provided with
    a first name and last name"""
    first_name = fname.title()
    last_name = lname.title()
    return f"{first_name} {last_name}"

first = input("Enter first name:")
second = input("Enter last name:")

print(f"The formatted name is {format_name(first, second)}")
