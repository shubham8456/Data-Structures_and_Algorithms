// https://leetcode.com/problems/top-k-frequent-elements
// https://neetcode.io/problems/top-k-elements-in-list?list=blind75

class TopKElements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
 
        for (int num : nums) {
            if ( !map.containsKey(num) ) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num) + 1);
            }
        }

        List<int []> arr = new ArrayList<>();
        for ( Map.Entry<Integer, Integer> entry : map.entrySet() ) {
            arr.add( new int[]{ entry.getValue(), entry.getKey() });
        }
        arr.sort((a,b) -> b[0] - a[0]);

        int[] arr1 = new int[k];
        for ( int i=0; i<k; i++ ) {
            arr1[i] = arr.get(i)[1];
        }

        return arr1;
    }
}
