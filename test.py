line = [["aa","bb","cc"],["11","22","33","44"],["!!","@@"]]

n = len(line)

queue = [[[],0]]
ans = []
while queue:
    cur,level = queue.pop(0)
    if level == n:
        ans.append(cur)
    else:
        for s in line[level]:
            queue.append([cur + [s],level+1])
            
            
print(ans)