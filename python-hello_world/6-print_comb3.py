for i in range(10):
    for j in range(i + 1, 10):
        if i < 9:
            print(f"{i}{j:02}, ", end="")
        else:
            print(f"{i}{j:02}")
