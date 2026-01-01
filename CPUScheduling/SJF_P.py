# SJF Preemptive
bt = [7, 4, 1]  # Burst times
rt = bt.copy()
wt = [0, 0, 0]
time = 0
completed = 0

while completed < len(bt):
    i = rt.index(min([x for x in rt if x > 0]))
    rt[i] -= 1
    time += 1
    if rt[i] == 0:
        wt[i] = time - bt[i]
        completed += 1

print("Process | BT | WT | TAT")
for i in range(len(bt)):
    print(i+1, "      |", bt[i], "|", wt[i], "|", bt[i] + wt[i])