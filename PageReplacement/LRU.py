# LRU Page Replacement
pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = [None,None,None]
page_faults = 0

print("Page -> Frames")

for p in pages:
    if p not in frames:
        if len(frames) < 3:
            frames.append(p)
        else:
            frames.pop(0)
            frames.append(p)
        page_faults += 1
    else:
        frames.remove(p)
        frames.append(p)
    print(p, " -> ", frames)
print("\nTotal Page Faults (LRU):", page_faults)
