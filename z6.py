import itertools as it

def iter_from(start, maximum=100):
    for elem in it.count(start):
        if elem > maximum:
            break
        yield elem
        

def repeat(iterable, max_times=10):
    times = 0
    for elem in it.cycle(iterable):
        if times > max_times:
            break
        times += 1
        yield elem

