# Priority Scheduling (Non-preemptive)
bt = [5, 3, 8]
pr = [2, 1, 3]
wt = [0, 0, 0]

# Sort based on priority
process = list(zip(pr, bt))
process.sort()
for i in range(1, len(process)):
    wt[i] = wt[i-1] + process[i-1][1]
    
print("PR | BT | WT | TAT")
for i in range(len(process)):
    print(process[i][0], "|", process[i][1], "|", wt[i], "|", wt[i] + process[i][1])
