#y3nlox

if __name__ == '__main__':
    print('Enter the lenght of your array.')
    n = int(input())
    print('Enter an integer separated with ',' ')
    maps = map(int, input().split())
    arr = list(maps)
    print(arr)
    for i in range(0,n-1):
        li = 0
        i = li
        if(i <= n - 1):
            if(arr[li]-arr[i+1] < 0):
                largest = arr[i+1]
                largestIndex = i+1
            elif(arr[li] - arr[i+1] == 0):
                largest = arr[i+1]
                largestIndex = i+1
            elif(arr[li] - arr[i+1] > 0):
                largest = arr[i]
                largestIndex = i
    print(largest)
