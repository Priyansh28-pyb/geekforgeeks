#Rotate Array Clockwise


class Solution:
    def rotateclockwise(self, arr, k):
       
        n = len(arr)
        if n == 0:
            return arr

        k %= n
        if k == 0:
            return arr

        def reverse(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # reverse whole array
        reverse(0, n - 1)
        # reverse first k elements (these were the last k of original array)
        reverse(0, k - 1)
        # reverse remaining n-k elements
        reverse(k, n - 1)

        return arr
