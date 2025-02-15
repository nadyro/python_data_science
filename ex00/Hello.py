ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List
ft_list[1] = "World!"

# Tuple
list_tuple = list(ft_tuple)
list_tuple[1] = "France!"
ft_tuple = tuple(list_tuple)

# Sets
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
