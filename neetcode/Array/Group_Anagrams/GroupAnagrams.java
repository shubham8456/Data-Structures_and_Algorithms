// https://leetcode.com/problems/group-anagrams
// https://neetcode.io/problems/anagram-groups?list=blind75

class GroupAnagrams {

  public List<List<String>> groupAnagrams(String[] strs) {
    HashMap<String,List<String>> map = new HashMap<>();

    for(String str : strs) {
      char[] ch = str.toCharArray();
      Arrays.sort(ch);
      String sortedWord = new String(ch);
      if(!map.containsKey(sortedWord))
        map.put(sortedWord, new ArrayList<>());
      map.get(sortedWord).add(str);
    }
    return new ArrayList<>(map.values());
  }
}
