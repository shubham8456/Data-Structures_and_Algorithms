// https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150

import java.util.Scanner;

public class MaxProfit {
  public static void main(String[] args) {
    int[] prices = getInput();
    int result = maxProfit(prices);
    System.out.println(result);
  }

  private static int maxProfit(int[] arr) {
    int l = 0;
    int r = 1;
    int maxProfit = 0;

    while (r < arr.length) {
      if (arr[l] < arr[r]) {
        int buy = arr[l];
        int sell = arr[r];
        maxProfit = Math.max(maxProfit, sell - buy);
      }
      else {
        l = r;
      }
      r = r + 1;
    }

    return maxProfit;
  }

  private static int[] getInput() {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the elements in the array, separated by space:  ");
    String input = sc.nextLine();
    sc.close();

    String[] stringArray = input.trim().split("\\s+");
    int[] arr = new int[stringArray.length];

    for (int i = 0; i < stringArray.length; i++) {
      arr[i] = Integer.parseInt(stringArray[i]);
    }

    return arr;
  }
}
