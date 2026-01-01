# Round Robin CPU Scheduling
bt = [5, 4, 2]  # Burst times
tq = 2          # Time quantum
rt = bt.copy()
wt = [0, 0, 0]
time = 0

while True:
    done = True
    for i in range(len(bt)):
        if rt[i] > 0:
            done = False
            if rt[i] > tq:
                time += tq
                rt[i] -= tq
            else:
                time += rt[i]
                wt[i] = time - bt[i]
                rt[i] = 0
    if done:
        break

print("Process | BT | WT | TAT")
for i in range(len(bt)):
    print(i+1, "      |", bt[i], "|", wt[i], "|", bt[i] + wt[i])
