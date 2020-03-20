'''
Variable
=========================
Variables are containers for storing data values.

Rule to Declare variable
=========================
1) Variable names can contain only letters numbers and underscores
2) Space are not allowed in variable but underscore can be used
3) Avoid using Python keyword and function name as variable
4) Variable names are case-sensitive (age, Age and AGE are three different variables)

'''

""" 
Most commonly used function in string operation are
    len() # to determine the string length
    title() # make uppercase first character of each word
    upper() # convert string to upper case
    strip() # Remove space 
    lstrip() # Remove space form left side
    rstrip() # Remove space form right side
    split() # split string and return it in list types
    join() # method takes all item in an iterable and join them into one string
    count() # count string character
    replace()
    startwith()
"""
first_name = "Hello"  # string variable with double quotes ""

# print(first_name)
last_name = 'World'  # string variable with single quotes ''
strvar = "the quick brown fox jumps over the lazy dog"
# print(strvar.title()) #instead of title user other string function.

# print(first_name + ' ' +  last_name) #string concatenation.
# print(last_name)
""" 
Most commonly used function in Number operation are to convert one type to another type
    int()
    float()
    complex()
    random()
    range() 
    str()

"""
# number = 1234  # integer type variable
# print(float(number))
# number = 123.44  # now number become float type variable

# print(number)
# number = 2j
# print(type(number)) # type function used to get the data typed
# number = 21
# # text = "we are living in " + number + "th century"
# text = "we are living in "+ str(number)+"th century"
# print(text)

""" 
Most commonly used function in string operation which return boolean output
    isalpha()
    isalnum()
    isdecimal()
    isdigit()
    isidentifier()
    islower()
    isnumeric()
    isprintable()
    istitle()
"""
num = "123"
print(num.isidentifier())  # try other function to get the difference output
