# C-LOOK Disk Scheduling
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
print("Order (C-LOOK):", end=" ")

# Move right first
for r in right:
    print(r, end=" ")
    total += abs(r - current)
    current = r

# Jump directly to smallest on left (if any)
if len(left) > 0:
    total += abs(current - left[0])
    current = left[0]
    # Serve left side in ascending order
    for r in left:
        print(r, end=" ")
        if r != current:
            total += abs(r - current)
            current = r
print("\nTotal Head Movement (C-LOOK):", total)
