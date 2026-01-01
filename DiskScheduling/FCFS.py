# FCFS Disk Scheduling
requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
total = 0
current = head

print("Order (FCFS):", end=" ")
for r in requests:
    print(r, end=" ")
    total += abs(r - current)
    current = r
print("\nTotal Head Movement (FCFS):", total)
