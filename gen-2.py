def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5
        if result > 100:
            break

values = infinite_sequence()
