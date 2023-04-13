# This simple code will demonstrate how to pass the data between functions
# Dated: 13th April 2023

def biodata():
    name = "Harry"
    city = "London"
    pin_no = 1234

    return name, city, pin_no


def print_biodata():
    name, city, pin_no = biodata()
    print(name)
    print(city)
    print(pin_no)


biodata()
print_biodata()
