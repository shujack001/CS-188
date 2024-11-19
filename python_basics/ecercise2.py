def quicksort(lst):
    if len(lst) <= 1:
        return lst
    smaller = [x for x in lst[1:] if x < lst[1]]
    larger = [x for x in lst[1:] if x >= lst[1]]
    return quicksort(smaller) + [lst[0]] + quicksort(larger)

if __name__ == "__main__":
    print(quicksort([1, 3, 4, 5, 2, 1, 2, 3]))