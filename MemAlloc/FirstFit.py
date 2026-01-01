# First Fit
blocks = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
allocation = [-1] * len(process)

for i in range(len(process)):
    for j in range(len(blocks)):
        if process[i] <= blocks[j]:
            allocation[i] = j
            blocks[j] -= process[i]
            break
        
print("Process -> Block")
for i in range(len(process)):
    if allocation[i] != -1:
        print(f"P{i+1} -> B{allocation[i]+1}")
    else:
        print(f"P{i+1} -> Not Allocated")