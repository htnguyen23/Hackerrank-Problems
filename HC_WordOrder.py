# Enter your code here. Read input from STDIN. Print output to STDOUT

buffer = input()
n = int(buffer)
word_dic = {}
for times in range(n):
    buffer = input()
    if not buffer in word_dic:
        word_dic[buffer] = 0
    word_dic[buffer] += 1

word_dic_values = word_dic.values()
ret_str = str(len(word_dic_values)) + "\n"
for val in word_dic_values:
    ret_str = ret_str + str(val) + " "

print(ret_str)