// https://leetcode.com/problems/longest-consecutive-sequence/
// https://neetcode.io/problems/longest-consecutive-sequence?list=blind75

class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        int longest = 0;

        for (Integer num : numSet) {
            // Only start counting if num is the start of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int length = 1;
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
