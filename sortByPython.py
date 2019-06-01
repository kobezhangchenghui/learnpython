#冒泡排序
def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    return lis

#插入排序
def insert_sort(lis):
    for i in range(1,len(lis)):
        for j in range(i, 0, -1):
            if lis[j] < lis[j-1]:
                lis[j],lis[j-1] = lis[j-1],lis[j]
            else:
                break
    return lis


#快速排序
def quick_sort(lis):
    if len(lis) <= 1:
        return lis
    else:
        key = lis[0]
        low = []
        big = []
        for i in lis[1:]:
            if i < key:
                low.append(i)
            else:
                big.append(i)
    return quick_sort(low) + [key] + quick_sort(big)


if __name__ == "__main__":
    lista = [10,3,5,8,4,1,6,7]
    print("The result of bubble_sort is %s" % bubble_sort(lista))
    print("The result of insert_sort is %s" % insert_sort(lista))
    print("The result of quick_sort is %s" % quick_sort(lista))