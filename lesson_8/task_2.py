# Creating a dictionary

def make_country(country, capital):
    my_dict = {}
    my_dict[country] = capital
    print(list(my_dict.values()))

make_country("Ukraine", "Kyiv")