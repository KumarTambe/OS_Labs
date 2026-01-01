# C-SCAN Disk Scheduling
requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
disk_size = 200   # tracks 0 to 199
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
print("Order (C-SCAN):", end=" ")
# Move right first
for r in right:
    print(r, end=" ")
    total += abs(r - current)
    current = r
# Go to end of disk
total += abs((disk_size - 1) - current)
current = disk_size - 1
# Jump to 0
total += abs(current - 0)
current = 0
# Then serve left side (from small to large)
for r in left:
    print(r, end=" ")
    total += abs(r - current)
    current = r
print("\nTotal Head Movement (C-SCAN):", total)
