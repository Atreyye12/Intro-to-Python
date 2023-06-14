introstring = input("Enter your introduction: ")
character_count = 0
word_count = 0
for i in introstring:
    character_count = character_count + 1
    if (i==' '):
        word_count = word_count + 1
print("number of words", word_count)   
print("number of characters", character_count)