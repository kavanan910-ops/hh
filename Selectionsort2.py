def selection_sort(a):
    n=len(a)
    for i in range(n-2):
        min=i
        for j in range(i+1,n-1):
            if a[j]<a[min]:
                a[j],a[min]=a[min],a[j]
import time
a=[10,3,2,6,4,9,42]
start=time.time()
selection_sort(a)
print("Sort the elements are:",a)
end=time.time()
print("Run time of the program is:",end-start)
