// https://neetcode.io/problems/duplicate-integer?list=neetcode150

import java.util.HashMap;
import java.util.Scanner;

public class CheckDuplicates {

  // private static final int[] arr = {1, 2, 3, 4, 5, 5, 6, 7};

  public static void main(String[] args) {
    int[] arr = getArrayInput();
    boolean result = checkDuplicate(arr);
    System.out.println(result);
  }

  private static boolean checkDuplicate(int[] nums) {
    HashMap<Integer, Integer> numOccurenceMap = new HashMap<>();

    for ( int i = 0; i < nums.length; i++ ) {
      if (numOccurenceMap.containsKey(nums[i])) {
        printHashMap(numOccurenceMap);
        return true;
      }
      else {
        numOccurenceMap.put(nums[i], 1);
      }
    }

    printHashMap(numOccurenceMap);
    return false;
  }

  private static int[] getArrayInput() {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter integers separated by space:");

    String inputLine = scanner.nextLine();
    String[] stringNumbers = inputLine.trim().split("\\s+");
    scanner.close();

    int[] numbers = new int[stringNumbers.length];
    for (int i = 0; i < stringNumbers.length; i++) {
      numbers[i] = Integer.parseInt(stringNumbers[i]);
    }

    return numbers;
  }

  private static void printHashMap(HashMap<Integer, Integer> hashMap) {
    for (Integer key : hashMap.keySet()) {
      System.out.println(key + " : " + hashMap.get(key));
    }
  }
}
