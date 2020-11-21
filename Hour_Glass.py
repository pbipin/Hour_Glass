"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com
101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10
To print the largest (maximum) hourglass sum found in a 6X6 2D array A.
"""
def hourglass_sum(arr):
    sum_list = []
    for i in range(len(arr)):
        if(i<(len(arr)-2)):
            for j in range(len(arr[i])):
                if(j<(len(arr[i])-2)):
                    top_row = arr[i][j]+arr[i][j+1]+arr[i][j+2]
                    middle_row = arr[i+1][j+1]
                    bottom_row = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                    sum_list.append(top_row+middle_row+bottom_row)
    
    sum_list.sort()   
    print(sum_list[-1]) 


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    hourglass_sum(arr)
