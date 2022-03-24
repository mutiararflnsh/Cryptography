text = "label"
flag_value = ""

for i in text:
    flag_value += chr(ord(i)^13)

print(flag_value)