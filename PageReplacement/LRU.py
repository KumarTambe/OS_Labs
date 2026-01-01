# LRU Page Replacement (Simple)
pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = []
size = 3
faults = 0
print("Page -> Frames")

for p in pages:
    if p not in frames:
        if len(frames) == size:
            frames.pop(0)   # remove least recently used
        frames.append(p)
        faults += 1
    else:
        frames.remove(p)
        frames.append(p)    # make it most recently used
    print(p, "->", frames)

print("Total Page Faults:", faults)