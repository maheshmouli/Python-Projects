#Kanden's Algorithm
#Using this we can find the maximum contigous sub array with linear time complexity--- O(n)


def maxSubArraySum(a, size):
      
    max_curr = 0
    max_global = 0
      
    for i in range(0, size):
        max_curr = max(a[i], max_curr+ a[i])
        if max_curr > max_global:
            max_global = max_curr
          
        # Do not compare for all elements. Compare only   
        # when  max_ending_here > 0
              
    return max_global

if __name__=="__main__":
    a = [-2, 3, 2, -1, -3, 4, 5,-2]
    print ("Maximum contiguous sum is", maxSubArraySum(a, len(a)))