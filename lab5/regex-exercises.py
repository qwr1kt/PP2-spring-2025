import re 


with open("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab5/row2.txt") as f:
    data = f.read()


print("Task 1")
matches = re.findall("ab*", data)
print(matches)

print("\nTask 2")
matches2 = re.findall("a.bb|abbb", data)
print(matches2)

print('\nTask 3')
matches3 = re.findall("[a-z]+_[a-z]+", data)
print(matches3)

print('\nTask 4')
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)

print('\nTask 5')
matches = re.findall(r"^a.*b$", data)
print(matches)

print("\nTask 6")
matches=re.sub(r"[., ]",':',data)
print(matches)

print("\nTask 7")
def snake_to_camel(snake_str):
    camel_case = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)
    return camel_case
print(snake_to_camel(data))

print("\nTask 8")
text = "HelloWorldPythonProgramming"
split_text = re.split(r'(?=[A-Z])', text)
split_text = [word for word in split_text if word]
print(split_text)

print("\nTask 9")
text = "InsertSpacesBetweenWordsStartingWithCapital"
spaced_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(spaced_text)

print("\nTask 10")
text = "mustardCheeseDoubleBurger"
def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
print(camel_to_snake(text))