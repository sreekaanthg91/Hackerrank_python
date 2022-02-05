def average(array):
    # your code goes here
    array_set=set(array)
    sum_arr=sum(set(array))
    num_heights=len(set(array))
    # sum=0
    # for i in array_st:
    #     sum+=i
        
    result=sum_arr/num_heights
    return result
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)