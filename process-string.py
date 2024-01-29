# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

phrase = str(input("Enter the string: "))
print("".join(x*2 if x != " " else x for x in phrase))

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyz"
range = input("Enter a range of letter (e.g, a-z): ")
strt, end  = range.split("-")
if range.istitle(): 
    res_upper = ''. join([chr for chr in alphabet.upper() if chr >= strt and chr <= end])
    print("user_range : " + str(res_upper))
else: 
    print("user_range : " ,str(''. join([chr for chr in alphabet.lower() if chr >= strt and chr <= end])))



# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")
# print(user_range)
