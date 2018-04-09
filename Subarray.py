def subarray(arr):

    max1 = 0   # stores maximum sum sub-array found so far
    max2 = 0   # stores maximum sum of sub-array ending at current position
    end = 0    #stores end-points of maximum sum sub-array found so far
    Start = 0     
    beg = 0       #stores starting index of a positive sum sequence

    for i in range (0, len(arr)):
        max2 = max2 + arr[i]
        if(max2<0):
            max2 = 0
            beg = i+1

        if(max1<max2):
            max1 = max2
            Start = beg
            end = i


    print(max1)
    print(arr[Start: end+1])

ab = [2,-2,3] #input array
subarray(ab)
