// https://leetcode.com/problems/valid-palindrome
// https://neetcode.io/problems/is-palindrome?list=neetcode150

import java.util.Scanner;

public class Palindrome {
  public static void main(String[] args) {
    String input = getInput();
    boolean isPalindrome = isPalindrome(input);
    System.out.println("The string " + input + " is a palindrome: " + isPalindrome);
  }

  private static boolean isPalindrome(String input) {
    int i = 0;
    int j = input.length() - 1;

    while (i < j) {
      if (!Character.isLetterOrDigit(input.charAt(i))) {
        i++;
        continue;
      }
      if (!Character.isLetterOrDigit(input.charAt(j))) {
        j--;
        continue;
      }

      if (Character.toLowerCase(input.charAt(i)) != Character.toLowerCase(input.charAt(j))) {
        return false;
      }

      i++;
      j--;
    }

    return true;
  }

  private static String getInput() {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a string: ");
    String inputString = sc.nextLine();
    sc.close();

    return inputString; 
  }
}
