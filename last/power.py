import sys
from time import time,clock
# 冒泡
def bubbleSort(arr):
    start=clock()
    tem=[]
    tem.append(arr)
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            tem.append(arr.copy())
    end=clock()
    return arr,tem,end-start

def bubb(arr):
    a,b,c=bubbleSort(arr)
    kj = '稳定性：好'
    nj = '辅助内存：不需要借用其他辅助内存（未改进） 空间复杂度：O（1） 时间复杂度：O(n**2)'
    return a,b,c,kj,nj
# 快速排序
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1
quickSort_tem=[]
def quickSort(arr, left=None, right=None,):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    quickSort_tem.append(arr.copy())
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def quick(arr):
    global quickSort_tem
    quickSort_tem = []
    s=clock()
    a=quickSort(arr)
    e=clock()
    kj = '稳定性：差'
    nj = '辅助内存：不需要借用其他辅助内存 平均时间复杂度：O（nlog(n)）最优情况下空间复杂度为：O(logn)  最差空间复杂度为：O( n )'
    return a,quickSort_tem,e-s,kj,nj

# 归并排序
merge_tem=[]
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));

    merge_tem.append(result.copy())
    return result


def mergeSort(arr):
    s=clock()
    tem=[]
    import math
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]

    return merge(mergeSort(left), mergeSort(right))


def me(arr):
    global merge_tem
    merge_tem = []
    a=clock()
    c=mergeSort(arr)
    e=clock()
    kj = '稳定性：好'
    nj = '最优时间复杂度,最差时间复杂度,平均时间复杂度:O( nlogn )  时间复杂度:O(nlogn)'
    return c,merge_tem,e-a,kj,nj

# 选择排序
def selectionSort(arr):
    tem=[]
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        tem.append(arr.copy())
    return arr,tem

def sel(arr):
    s=clock()
    a,b=selectionSort(arr)
    e=clock()
    kj = '稳定性：差'
    nj = '时间复杂度是O(n^2) '
    return a,b,e-s,kj,nj


# 希尔排序
def shellSort(arr):
    tem=[]
    import math
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
            tem.append(arr.copy())
        gap = math.floor(gap / 3)
    return arr,tem
def shel(arr):
    s=clock()
    a,b=shellSort(arr)
    e=clock()
    kj = '稳定性：差'
    nj = '时间复杂度是：O（nlogn）～O（n2）'
    return a,b,e-s,kj,nj


# 插入
def insertionSort(arr):
    tem=[]
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
        tem.append(arr.copy())
    return arr,tem
def ins(arr):
    s=clock()
    a,b=insertionSort(arr)
    e=clock()
    kj = '稳定性：好'
    nj = '时间复杂度是O(n^2)'
    return a,b,e-s,kj,nj


# 计数排序
def countingSort(arr, maxValue):
    tem=[]
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
            tem.append(arr.copy())
    return arr,tem

def count(arr,max):
    s=clock()
    a,b=countingSort(arr,max)
    e=clock()
    kj = '稳定性：好'
    nj = '时间复杂度是Θ(n+k)'
    return a,b,e-s,kj,nj


# 基数
def radix(arr):
    tem=[]
    digit = 0
    max_digit = 1
    max_value = max(arr)
    # 找出列表中最大的位数
    while 10 ** max_digit < max_value:
        max_digit = max_digit + 1

    while digit < max_digit:
        temp = [[] for i in range(10)]
        for i in arr:
            # 求出每一个元素的个、十、百位的值
            t = int((i / 10 ** digit) % 10)
            temp[t].append(i)

        coll = []
        for bucket in temp:
            for i in bucket:
                coll.append(i)

        arr = coll
        digit = digit + 1
        tem.append(arr.copy())

    return arr,tem

def jishu(arr):
    s=clock()
    a,b=radix(arr)
    e=clock()
    kj = '稳定性：好'
    nj = '时间复杂度为O(nlog(r)m)'
    return a,b,e-s,kj,nj


# 堆排序
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    tem=[]
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
        tem.append(arr.copy())
    return arr,tem
def dui(arr):
    s=clock()
    a,b=heapSort(arr)
    e=clock()
    kj = '稳定性：差'
    nj = '时间复杂度为 Ο(nlogn) 空间复杂度为常数：O(1)'
    return a,b,e-s,kj,nj

# 桶排序
def bucketSort(nums):
    tem=[]
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1
        # 存储排序好的元素
    sort_nums = []

    for j in range(len(bucket)):
        n = bucket[j]
        if n != 0:
            for _ in range(n):

                sort_nums.append(j)
            tem.append(sort_nums.copy())
    return sort_nums,tem
def bu(arr):
    s=clock()
    a,b=bucketSort(arr)
    e=clock()
    kj = '稳定性：好'
    nj = '时间复杂度为 O(m+n)。这是一个非常快的排序方法。'
    return a,b,e-s,kj,nj

def k(str,arr,n):
    if str=='冒泡排序':
        return bubb(arr)
    if str=='快速排序':
        return quick(arr)
    if str=='归并排序':
        return me(arr)
    if str=='选择排序':
        return sel(arr)
    if str=='希尔排序':
        return shel(arr)
    if str=='插入排序':
        return ins(arr)
    if str=='计数排序':
        return count(arr,n)
    if str=='基数排序':
        return jishu(arr)
    if str=='堆排序':
        return dui(arr)
    if str=='桶排序':
        return bu(arr)
