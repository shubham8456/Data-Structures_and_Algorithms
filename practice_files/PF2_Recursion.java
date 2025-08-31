public class PF2_Recursion {

  public static void main(String[] args) {
    int num = 8;

    int result1 = factorial(num);
    int result2 = fibonacci(num);
    System.out.println(String.format("The factorial of %d is %d", num, result1));
    System.out.println(String.format("The %dth number in fibonacci sequence is: %d", num, result2));
    printArray();
  }

  private static int factorial(int num) {
    if (num == 0)
      return 1;
    else
      return num * factorial(num - 1);
  }

  private static int fibonacci(int num) {
    if (num == 0)
      return 0;
    else if (num == 1)
      return 1;
    else
      return fibonacci(num - 1) + fibonacci(num - 2);
  }
  
  private static void printArray() {
    int[] arr = { 1, 2, 3, 4, 5 };

    int counter = 0;
    print(arr, counter);
  }

  private static void print(int[] arr, int counter) {
    if (counter == arr.length)
      System.out.println("\n");
    else {
      System.out.print(String.format("%d ", arr[counter]));
      print(arr, counter + 1);
    }
  }
}

// Given an array of integers, print all elements of the array using recursion.
