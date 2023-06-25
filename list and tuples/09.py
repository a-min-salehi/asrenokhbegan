def bi_search(n_list, n):
    if len(n_list) == 0:
        return False

    mid = len(n_list) // 2
    if n_list[mid] == n:
        return True

    if n_list[mid] > n:
        return bi_search(n_list[:mid], n)
    else:
        return bi_search(n_list[mid + 1:], n)
