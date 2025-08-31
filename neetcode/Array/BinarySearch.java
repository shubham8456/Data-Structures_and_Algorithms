// https://neetcode.io/problems/binary-search?list=neetcode150

import java.util.Scanner;

public class BinarySearch {
  public static void main(String[] args) {
    Object[] userInput = getUserInput();
    int[] numbers = (int[])userInput[0];
    int target = (int) userInput[1];

    int index = binarySearch(numbers, target);
    System.out.println(String.format("Index: %d", index));
  }

  private static int binarySearch(int[] arr, int k) {
    int i = 0;
    int j = arr.length - 1;

    while (i <= j) {
      int mid = (i + j) / 2;
      if (k < arr[mid]) {
        j = mid - 1;
      } else if (k > arr[mid]) {
        i = mid + 1;
      } else {
        return mid;
      }
    }

    return -1;
  }

  private static Object[] getUserInput() {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter the array of numbers separated by a space: ");
    String[] arrItems = sc.nextLine().trim().split("\\s+");

    System.out.print("Enter the number to search: ");
    int target = sc.nextInt();

    sc.close();

    int[] arr = new int[arrItems.length];
    for (int i = 0; i < arrItems.length; i++) {
      arr[i] = Integer.parseInt(arrItems[i]);
    }

    return new Object[] {arr, target};
  }
}
