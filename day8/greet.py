def greet():
    print("Hello\n"
          "How are you?\n"
          "Isn't it nice today?")


def greet_with_name(name):
    print(f"Hello {name}\n"
          f"How are you? {name}\n")

def greet_with(name, location):
    print(f"Hello {name}\n"
          f"Wat is it like in {location}?\n")

#greet()
#greet_with_name("John")
greet_with("John","Glastonbury")
