# STRING INDEXING IN PYTHON
# String indexing is a way to access individual characters in a string using their position (index).
# In Python, string indexing starts at 0, which means the first character of the string is at index 0, 
# the second character is at index 1, and so on. 

# e.g   
# name = "Laureate"   
# print(name[0])   # L
# print(name[1])   # a
# print(name[2])   # u
# print(name[3])   # r
# print(name[4])   # e
# print(name[5])   # a
# print(name[6])   # t
# print(name[7])   # e
# print(name[8])   # IndexError: string index out of range

credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[0])   # 1
print(credit_card_number[::4])   # 1234 
print(credit_card_number[5:9])   # 5678
print(credit_card_number[10:14])   # 9012   
print(credit_card_number[15:19])   # 3456   
print(credit_card_number[::2]) 

last_digits = credit_card_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")
 
#  REVERSE
credit_card_number = credit_card_number[::-1]
print(credit_card_number)