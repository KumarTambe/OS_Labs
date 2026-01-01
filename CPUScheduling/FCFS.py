# FCFS CPU Scheduling
bt = [4, 3, 5]  # Burst times
wt = [0, 0, 0]  # Waiting time

for i in range(1, len(bt)):
    wt[i] = wt[i-1] + bt[i-1]
    
print("Process | BT | WT | TAT")
for i in range(len(bt)):
    print(i+1, "      |", bt[i], "|", wt[i], "|", bt[i] + wt[i])
