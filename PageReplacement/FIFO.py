# FIFO Page Replacement
pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = [None, None, None]
page_faults = 0
pointer = 0
print("Page -> Frames")

for p in pages:
    if p not in frames:
        frames[pointer] = p
        pointer = (pointer + 1) % len(frames)
        page_faults += 1
        print(p, " -> ", frames)

print("\nTotal Page Faults (FIFO):", page_faults)