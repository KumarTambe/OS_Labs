# LOOK Disk Scheduling
requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
left = []
right = []
for r in requests:
    if r < head:
        left.append(r)
    else:
        right.append(r)
left.sort()
right.sort()
total = 0
current = head
print("Order (LOOK):", end=" ")

# Move right first (only till last request)
for r in right:
    print(r, end=" ")
    total += abs(r - current)
    current = r
# Then move left (till smallest request)
for r in reversed(left):
    print(r, end=" ")
    total += abs(current - r)
    current = r
print("\nTotal Head Movement (LOOK):", total)
