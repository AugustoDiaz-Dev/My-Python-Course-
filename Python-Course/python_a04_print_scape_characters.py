#Topic: Escape characters.

string_with_double_quotes_escape = "We have a \"huge\" amount of posibilities."
print(string_with_double_quotes_escape)

single_quote_escape = 'It\'s my cat'
print(single_quote_escape) 

backslash_escape = "This will insert one \\ (backslash)."
print(backslash_escape) 

new_line_escape = "This will create\n a new line"
print(new_line_escape)

carriage_return_escape = "Hello\rWorld!"
print(carriage_return_escape) 

tab_escape = "This is a\t tab effect!"
print(tab_escape) 

#This is the way to erase one character (backspace):
backspace_escape = "Hello \bWorld!"
print(backspace_escape) 

#If backslash is followed by three integers will result in a octal value:
octal_value_escape = "\110\145\154\154\157"
print(octal_value_escape) 

#A backslash followed by an 'x' and a hex number represents a hex value:
hex_value_escape = "\x48\x65\x6c\x6c\x6f"
print(hex_value_escape) 


