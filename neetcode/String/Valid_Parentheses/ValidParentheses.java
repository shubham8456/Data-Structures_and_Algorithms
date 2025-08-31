// https://leetcode.com/problems/valid-parentheses
// https://neetcode.io/problems/validate-parentheses?list=neetcode150

import java.util.Scanner;
import java.util.Stack;

public class ValidParentheses {
  public static void main(String[] args) {
    String str = getInput();
    boolean result = validateParentheses(str);
    System.out.println(result);
  }

  private static boolean validateParentheses(String str) {
    Stack<Character> stack = new Stack<>();

    for (char c : str.toCharArray()) {
      if (isOpenParentheses(c)) {
        stack.push(c);
      } else if (isCloseParentheses(c)) {
        if (stack.isEmpty() || stack.pop() != complementOf(c)) {
          return false;
        }
      }
    }

    return stack.isEmpty();
  }

  private static char complementOf(char c) {
    switch (c) {
      case ')': return '(';
      case '}': return '{';
      case ']': return '[';
      default: return '\0';
    }
  }

  private static boolean isOpenParentheses(char c) {
    return c == '(' || c == '{' || c == '[';
  }

  private static boolean isCloseParentheses(char c) {
    return c == ')' || c == '}' || c == ']';
  }

  private static String getInput() {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a string with parentheses: ");
    String str = sc.nextLine();
    sc.close();

    return str;
  }
}
