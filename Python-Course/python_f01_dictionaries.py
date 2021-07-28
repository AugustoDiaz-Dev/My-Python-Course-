#Topic: Dictionaries.

#Key and value. You can use whatever you want as key as long as it has an "unique" identifier.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    }

print(monthConversions["Nov"])
print(monthConversions.get("Dec")) #With .get you can pass a default value as you can see in the following example.
print(monthConversions.get("Luv", "Not a valid key.")) #You can write down what you want as fallback.