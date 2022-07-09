# "AAABABB"
# "AA"
# "ABBBBBBBAAA"

colors = "ABBBBBBBAAA"
A_count =0
B_count = 0
A_delete_count = 0
B_delete_count = 0

for i in range(0,len(colors)):
    if colors[i] == 'A':
        A_count += 1
        B_count = 0
        if A_count >= 3:
            A_delete_count +=1
    
    elif colors[i] == 'B':
        A_count = 0
        B_count += 1
        if B_count >= 3:
            B_delete_count +=1

if A_delete_count > B_delete_count:
    print(True)
else:
    print(False)