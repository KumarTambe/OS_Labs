# Worst Fit
blocks = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
allocation = [-1] * len(process)

for i in range(len(process)):
    worst = -1
    for j in range(len(blocks)):
        if process[i] <= blocks[j]:
            if worst == -1 or blocks[j] > blocks[worst]:
                worst = j
    if worst != -1:
        allocation[i] = worst
        blocks[worst] -= process[i]
        
print("Process -> Block")
for i in range(len(process)):
    if allocation[i] != -1:
        print(f"P{i+1} -> B{allocation[i]+1}")
    else:
        print(f"P{i+1} -> Not Allocated")
