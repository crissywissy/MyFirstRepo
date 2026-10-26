def hanoi(n, start, end, middle):
    if n == 1:
        print("Move disk 1 from", start, "to", end)
        return

    hanoi(n - 1, start, middle, end)

    print("Move disk", n, "from", start, "to", end)

    hanoi(n - 1, middle, end, start)

// test with 3 towers
n = 3
hanoi(n, "A", "C", "B")