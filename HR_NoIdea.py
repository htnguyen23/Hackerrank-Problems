# # get n and m (input line 1), and delcare array sizes respectively
# # get array elem (input line 2)
# # get A elem (input line 3)
# # get B elem (input line 4)
# # iterate through array and adjust happiness points based on what set the array elem belongs to

happiness = 0
lines = []
for i in range(0,4):
    lines.append(input().strip())
#print(lines)

in_arr = lines[1].split(" ")
A = lines[2].split(" ")
B = lines[3].split(" ")
A_dic = {}
for a in A:
    A_dic[a] = 0
B_dic = {}
for b in B:
    B_dic[b] = 0

for num in in_arr:
    if num in A_dic:
        happiness += 1
    elif num in B_dic:
        happiness -= 1

print(happiness)

# happiness = 0
# lines = []
# buffer = ""
# for i in range(0, 4):
#     buffer = input().strip()
#     lines.append(buffer)
# #print(lines)

# in_arr = lines[1].split(" ")
# A = {}
# for i in range(0, len(lines[2]), 2):
#     A[lines[2][i]] = 0
# B = {}
# for i in range(0, len(lines[3]), 2):
#     B[lines[3][i]] = 0


# for num in in_arr:
#     if num in A:
#         happiness += 1
#     elif num in B:
#         happiness -= 1

# print(happiness)

