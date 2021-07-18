# 1D Dynamic Programming Problems

### 70. Climbing Stairs

Fib. Define first several steps and using iterations and state transformation function to searching the results.

        def climbStairs(self, n: int) -> int:
            if n<=2:
                return n
            prevv = 1
            prev = 2
            curr = 0

            for i in range(2,n):
                curr = prev+prevv

                prevv = prev
                prev = curr
            return curr

### 198. House Robber

CORE: choose whether take the dp[i-1] or dp[i-2]+nums[i-1] dp denotes the money stolen from previous houses

    public int rob(int[] nums) {
        int[] dp=new int[nums.length+1];

        dp[1]=nums[0];

        for(int i=2;i<nums.length+1;i++){
             // CORE
            dp[i] = Math.max(dp[i-1],dp[i-2]+nums[i-1]);
        }
        return dp[dp.length-1];
    }

### 300. Longest Increasing Subsequence

Subsequence: do not need to be continuous

    def lengthOfLIS(self, nums: List[int]) -> int:
        comp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    // CORE
                    comp[i] = max(comp[j] + 1,comp[i])

        return max(comp)

### 413. Arithmetic Slices

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dps = [0 for i in range(len(nums))]
        for i in range(2,len(nums)):
            if nums[i-1]-nums[i-2]==nums[i]-nums[i-1]:
                dps[i]=dps[i-1]+1
        return sum(dps)

### 1137. N-th Tribonacci Number

Fib + hashtable

    public int tribonacci(int n) {
        int[] ini = new int[]{0,1,1};
        for(int i=3;i<n+1;i++){
             // CORE
            ini[i%3]=ini[0]+ini[1]+ini[2];
        }
        return ini[n%3];
    }

# 2D Dynamic Programming Problems

### 64. Minimum Path Sum

the ini_matrix is used to calculate the current amount of steps. Very easy question.

        def minPathSum(self, grid: List[List[int]]) -> int:

            ini_matrix=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]

            for i in range(len(grid)):
                for j in range(len(grid[0])):

                    if i==0 and j==0:
                        ini_matrix[0][0]=grid[0][0]
                    elif i==0 :
                        ini_matrix[i][j]=ini_matrix[i][j-1]+grid[i][j]
                    elif j==0:
                        ini_matrix[i][j]=ini_matrix[i-1][j]+grid[i][j]
                    else:
                        ini_matrix[i][j] = min(ini_matrix[i-1][j],ini_matrix[i][j-1])+grid[i][j]
            print(ini_matrix)
            return ini_matrix[-1][-1]

