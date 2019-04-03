class Solution:
    def sortedSquares(self, A):
        pos, len_arr, ret = 0, len(A), []
        for i in range(len_arr):
            if A[i] >= 0:
                pos = i
                break
        index, post_index = pos - 1, pos

        while index >= 0 or post_index < len_arr:
            if index >= 0:
                if post_index < len_arr and -A[index] <= A[post_index]:
                    ret.append(A[index] ** 2)
                    index -= 1
                elif post_index == len_arr:
                    ret.append((A[index] ** 2))
                    index -= 1
            if post_index < len_arr:
                if index >= 0 and -A[index] >= A[post_index]:
                    ret.append(A[post_index] ** 2)
                    post_index += 1
                elif index < 0:
                    ret.append(A[post_index] ** 2)
                    post_index += 1
        return ret

if __name__ == "__main__":
    J = [-4,-1,0,3,10]
    res = Solution().sortedSquares(J)
    print(res)
