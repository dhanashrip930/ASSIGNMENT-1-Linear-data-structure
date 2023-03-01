 # Write a program to find all pairs of an integer array whose sum is equal to a given number
def sum_pairs(array , num , sum):
    for i in range(num):
        for j in range(i+1 , num):
            if array[i] + array[j] == sum:
                print("(",array[i],",",array[j],")",sep = "")
                
                
                
# drive the code
array = [5, 6, 4, 5, 1, 9, 3, 7, 2, 8]
num = len(array)
sum = 10


sum_pairs(array, num, sum)