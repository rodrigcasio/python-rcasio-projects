# Reading files examples

# --- 1. using .read() 
# --- 2. with num argument .read(num)
# --- 3. using .read(num) multiple times, continues the rest of the charcaters

with open('./example1.txt', 'r') as file:
    file_content = file.read()

print(f"Is '{file}' is closed: {file.closed}")

print(file_content)

print('---')

with open('./example1.txt', 'r') as file2:
    print(file2.read(4))

print(f"Is {file2} closed: {file2.closed}")

print('---')

with open('./example1.txt', 'r') as file3:
    print(file3.read(4))
    print(file3.read(4))
    print(file3.read(10))

print(f"Is {file3} closed: {file3.closed}")

print('+++++')
# -- 1. using .readline() method 
# -- 2. using it multiple times
# -- 3. .readline(num) with argument (it does not read past the end of line)

with open('./example1.txt', 'r') as file4:
    print(f"First line: {file4.readline()}")

print(f"Is {file4} closed: {file4.closed}")
print('---')

with open('./example1.txt', 'r') as file5:
    print(f"First line: {file5.readline()}")
    print(f"Second line: {file5.readline()}")
    print(f"Third line: {file5.readline()}")
print('---')

with open('./example1.txt', 'r') as file6:
    print(file6.readline(6))   # does not read past the end of the line
    print(file6.read(20))


print('+++++')
# --  1. using a loop to iterate through the list (placing i as num of iteration)

with open('./example1.txt', 'r') as file7:
    i = 0
    for line in file7:
        print(f"Iteration {str(i)}: {line}")
        i += 1


print('+++++')
# -- 1. using .readlines() method to store all the lines within a list

with open('./example1.txt', 'r') as file8:
    fileContent = file8.readlines()
    print("Full list ---> ", fileContent)
print('---')

print(file8.closed)
print('---')

print(fileContent[0])
print(fileContent[1])
print(fileContent[2])
print(fileContent[3])





