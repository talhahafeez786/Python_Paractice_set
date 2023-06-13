letter = '''Dear <|Name|>
Your are Selected!
<|Date|>'''
name = input("Enter the Name")
date = input("Enter Date")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)