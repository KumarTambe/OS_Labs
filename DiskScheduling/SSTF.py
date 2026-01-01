# SSTF Disk Scheduling
requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
total = 0
current = head
done = [False] * len(requests)
print("Order (SSTF):", end=" ")

for _ in range(len(requests)):
    min_dist = 9999
    index = -1
    for i in range(len(requests)):
        if not done[i]:
            dist = abs(requests[i] - current)
            if dist < min_dist:
                min_dist = dist
                index = i
    done[index] = True
    total += min_dist
    current = requests[index]
    print(current, end=" ")
print("\nTotal Head Movement (SSTF):", total)
