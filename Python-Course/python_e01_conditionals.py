#Topic: Conditionals. if elif else and or/and operator.

is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You neither male nor tall")

# if is_male and is_tall:
#     print("You are a male or tall or both")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You neither male nor tall")