def left(i: int) -> int:
    return i*2 + 1

def right(i: int) -> int:
    return (i*2 + 1) +1

def father(i: int) -> int:
    return int((i-1)//2)

def swipe(dataset: list[list], major_index: int, minor_index: int):
    aux = dataset[major_index]
    dataset[major_index] = dataset[minor_index]
    dataset[minor_index] = aux