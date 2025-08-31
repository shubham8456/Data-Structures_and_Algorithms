// https://leetcode.com/problems/product-of-array-except-self
// https://neetcode.io/problems/products-of-array-discluding-self?list=blind75

class ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zeroCount = 0;


        for (int num : nums) {
            if (num != 0) {
                product *= num;
            } else {
                zeroCount++;
                if (zeroCount > 1) {
                    // More than one zero means all results are zeroes
                    return new int[nums.length];
                }
            }
        }

        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (zeroCount == 1) {
                // If exactly one zero, only index with zero gets the value of product
                res[i] = (nums[i] == 0) ? product : 0;
            } else {
                res[i] = product / nums[i];
            }
        }

        return res;
    }
}  
