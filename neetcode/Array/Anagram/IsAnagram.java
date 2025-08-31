// https://leetcode.com/problems/valid-anagram
// https://neetcode.io/problems/is-anagram?list=neetcode150

import java.util.HashMap;
import java.util.Scanner;

public class IsAnagram {

  public static void main(String[] args) {
    String[] strArray = getStringInput();
    boolean result = isAnagram(strArray[0], strArray[1]);
    System.out.println(result);
  }

  private static boolean isAnagram(String str1, String str2) {
    if (str1.length() != str2.length()) {
      return false;
    }

    HashMap<String, Integer> charMap1 = createHashMap(str1);
    HashMap<String, Integer> charMap2 = createHashMap(str2);

    return charMap1.equals(charMap2);
  }

  private static HashMap<String, Integer> createHashMap(String str) {
    HashMap<String, Integer> charMap = new HashMap<>();

    for ( int i = 0; i < str.length(); i++ ) {
      String key = str.charAt(i) + "";
      if (charMap.containsKey(key)) {
        charMap.put(key, charMap.get(key) + 1);
      }
      else {
        charMap.put(key, 1);
      }
    }

    System.out.println("HashMap for string: " + str);
    printHashMap(charMap);
    return charMap;
  }

  private static void printHashMap(HashMap<String, Integer> hashMap) {
    for (String key : hashMap.keySet()) {
      System.out.println(key + " : " + hashMap.get(key));
    }
  }

  private static String[] getStringInput() {
    Scanner scanner = new Scanner(System.in);

    System.out.print(" Enter first string:  ");
    String firstString = scanner.nextLine();

    System.out.print("Enter second string:  ");
    String secondString = scanner.nextLine();
    
    scanner.close();

    String[] inputStrings = new String[2];
    inputStrings[0] = firstString;
    inputStrings[1] = secondString;

    return inputStrings;
  }
}
