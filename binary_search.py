array = [0, 1, 2, 3, 11, 15, 26, 37, 58, 79]
n = 58

def binary_search(array,n):
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2  
        if array[mid] == n:
            print(array[mid])
            return  
        elif array[mid] < n:
            print("Go to right side")
            start = mid + 1 
        else:
            print("Go to left side")
            end = mid - 1  

binary_search(array,n)

























# array = [0, 1, 2, 3, 11, 15, 26, 37, 58, 79]
# n = 58

# def binary_search(array,n,mid):
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start + end) // 2  
#         if array[mid] == n:
#             print(array[mid])
#             return  
#         elif array[mid] < n:
#             print("Go to right side")
#             return binary_search(array,n,mid+1)
#         else:
#             print("Go to left side")
#             return binary_search(array,n,mid-1)
# binary_search(array,n,mid)