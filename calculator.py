

exp = input("Enter Expression: ")

parts = []
num_str = ''

for char in exp:
    if char.isdigit() or char == '.':
        num_str += char
        
    else:
        parts.append(num_str)
        parts.append(char)
        num_str = ''
        
if num_str:
    parts.append(num_str)
        
x = float(parts[0])
op = parts[1]
if len(parts) == 3:
    
    y = float(parts[2])
        
    if op == '+':
        print(f"{x}{op}{y} = {x + y}")
        
    elif op == '-':
        print(f"{x}{op}{y} = {x - y}")
    
    elif op == '*':
        print(f"{x}{op}{y} = {x * y}")
    
    elif op == '/':
        if y == 0:
            print("Can't Dividing 0!")
        else:    
            print(f"{x}{op}{y} = {x / y}")
        
    else:
        print("Invalid operator!")
else:
    print("Invalid expression!")
    
        