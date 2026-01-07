

n = int(input())
indices = set(map(int, input().split()))

todo_list = []
for i in range(n):
    line = input()
    if i in indices:
        line = line.replace('[ ]', '[x]', 1)
    print(line)

# #Another Method


# n=int(input())
# task=[]
# t=input()
# task=t.split()

# for i in range(len(task)-1,-1,-1):
#     if 0<= int(task[i]) <n:
#         pass
#     else:
#         task.pop(i)
        
# s=''
        
# for i in range(n):
#     a=input()
#     ind=a.index('[')
#     if str(i) in task:
#         s=a[0:ind+1]+'x'+a[ind+2::]
#     else:
#         s=a
#     print(s)

#   Update Todo List Based on Given Indices
# Given a todo list formatted as multiple lines, where each todo item is represented as - [ ] item. Your task is to mark the todo items as completed based on the indices provided in the first line of the input. The completed items should be marked with - [x].

# NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

# Input Format
# The first line contains the number of items in the todo list
# The second line contains a space-separated list of indices (0-based) indicating which items in the todo list should be marked as completed.
# The subsequent lines contain the todo list items.
# Output Format
# Print the updated todo list with the specified items marked as completed.
# Example
# Input

# 3
# 0 2
# - [ ] Buy groceries
# - [ ] Read a book
# - [ ] Write code
# Output

# - [x] Buy groceries
# - [ ] Read a book
# - [x] Write code
# Input

# 3
# 1 3 4
# - [ ] Go to the gym
# - [ ] Cook dinner
# - [ ] Clean the house
# Output

# - [ ] Go to the gym
# - [x] Cook dinner
# - [ ] Clean the house
# Note
# If an index is out of the range of the todo list items, it should be ignored.

        
        
        
