// https://leetcode.com/problems/two-sum/
// https://neetcode.io/problems/two-integer-sum?list=neetcode150

import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
  public static void main(String[] args) {
    Object[] userInput = getUserInput();
    int[] nums = (int[]) userInput[0];
    int target = (int) userInput[1];

    int[] indices = findIndices(nums, target);
    System.out.println("Indices: " + Arrays.toString(indices));
  }

  private static int[] findIndices(int[] arr, int target) {
    HashMap<Integer, Integer> differenceFirstIndexHash = new HashMap<>();
    differenceFirstIndexHash.put(target - arr[0], 0);

    for (int i = 1; i < arr.length; i++) {
      if (differenceFirstIndexHash.containsKey(arr[i])) {
        printHashMap(differenceFirstIndexHash);
        int firstIndex = differenceFirstIndexHash.get(arr[i]);
        return new int[] {firstIndex, i};
      }
      else {
        int difference = target - arr[i];
        differenceFirstIndexHash.put(difference, i);
      }
    }

    return new int[] {};
  }

  private static Object[] getUserInput() {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter the array of numbers separated by a space: ");
    String[] arrItems = sc.nextLine().split(" ");

    System.out.print("Enter the target sum: ");
    int target = sc.nextInt();

    sc.close();

    int[] arr = new int[arrItems.length];
    for (int i = 0; i < arrItems.length; i++) {
      arr[i] = Integer.parseInt(arrItems[i]);
    }

    return new Object[] {arr, target};
  }

  private static void printHashMap(HashMap<Integer, Integer> map) {
    for( Integer key : map.keySet() ) {
      System.out.println("Key: " + key + ", Value: " + map.get(key));
    }
  }
}
