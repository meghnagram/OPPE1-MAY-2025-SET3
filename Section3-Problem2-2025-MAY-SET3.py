

n = int(input())
d = [
   (k,int(v))
   for k,v in [input().split(":") for i in range(n)]
]
max_len = max(map(lambda x: len(x[0]), d))
for k,v in d:
   print(f"{{:>{max_len}}}:{{}}".format(k,"#"*v))
   # Alternate method
   # print(f"{' '*(max_len-len(k))}{k}:{'#'*v}")


# #Another Problem
# n=int(input())

# m=[]

# for i in range(n):
#     m.append(input())
    
# max=0
# for i in range(n):
#     l=[]
#     l= m[i].split(':')
#     a=len(l[0])
#     if a>max:
#         max=a
    
# for i in range(n):
#     l=[]
#     l= m[i].split(':')
#     print(f"{l[0]:>{max}}:",end='')
#     for k in range(int(l[1])):
#         print('#',end='')
#     print()
    
# Horizontal Bar Chart
# Given a set of key-value pairs, where each key is a string (representing a category) and the value is an integer (representing a count). Your task is to generate a horizontal bar chart using the # character, with the following formatting:

# Each line should contain the key, followed by a colon :, and then a number of # characters equal to the corresponding count.
# The keys should be right-aligned based on the length of the longest key, so that the colons : are vertically aligned in the output.
# Input Format

# The input consists of:

# An integer n — the number of key-value pairs.
# Followed by n lines, each containing a string key and an integer value separated by a colon (:), with no spaces.
# Output Format

# Print n lines where each line contains:

# The key, right-aligned to match the longest key.
# A colon :
# A sequence of # characters equal to the corresponding value.
# Example

# Input

# 6
# apple:10
# banana:5
# plum:6
# cherry:3
# dates:8
# strawberry:15
# Output

#      apple:##########
#     banana:#####
#       plum:######
#     cherry:###
#      dates:########
# strawberry:###############

