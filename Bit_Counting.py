def count_bits(n):
    int_ = abs(n)
    twice_list = []
    while int_ !=0:
        k = (int_%2)
        int_ = int(int_/2)
        twice_list.append(k)
    return sum(twice_list)
