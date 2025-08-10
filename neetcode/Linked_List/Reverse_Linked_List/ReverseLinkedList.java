// https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150

/**
 * Run instructions for this java class
 * cd .. to 'Linked_List' dir
 * javac MyCustomSinglyLinkedList/ListNode.java Reverse_Linked_List/ReverseLinkedList.java
 * java Reverse_Linked_List.ReverseLinkedList
 */

package Reverse_Linked_List;

import MyCustomSinglyLinkedList.ListNode;
import java.util.Scanner;
import java.util.Arrays;


public class ReverseLinkedList {
  public static void main(String[] args) {
    ListNode head = createLinkedListOnUserInputAndReturnHead();
    head = reverseLinkedList(head);
  }

  private static ListNode reverseLinkedList(ListNode head) {
    ListNode current = head;
    ListNode prevNode = null;

    while ( current != null ) {
      ListNode nextNode = current.next;
      current.next = prevNode;
      prevNode = current;
      current = nextNode;
    }
    printLinkedList(prevNode);

    return prevNode;
  }

  private static ListNode createLinkedListOnUserInputAndReturnHead() {
    String[] linkedListItemsValuesStringArray = getUserInput();
    int[] linkedListItemsValuesIntegerArray = stringToInteger(linkedListItemsValuesStringArray);
    ListNode head = createLinkedList(linkedListItemsValuesIntegerArray);
    printLinkedList(head);

    return head;
  }

  private static ListNode createLinkedList(int[] arr) {
    ListNode head = new ListNode(arr[0]);
    ListNode current = head;

    for ( int i = 1; i < arr.length; i++ ) {
      ListNode newNode = new ListNode(arr[i]);
      current.next = newNode;
      current = current.next;
    }

    return head;
  }

  private static String[] getUserInput() {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the linked list items' values: ");
    String userInput = sc.nextLine();
    sc.close();

    return userInput.trim().split("\\s+");
  }

  private static int[] stringToInteger(String[] strArray) {
    int[] intArray = new int[strArray.length];

    int index = 0;
    for (String str : strArray) {
      intArray[index] = Integer.parseInt(str);
      index ++;
    }

    return intArray;
  }

  private static void printLinkedList(ListNode head) {
    ListNode current = head;
    int k = 0;

    while (current != null) {
      k += 1;
      System.out.println(String.format("List[%d] = %d", k, current.val));
      current = current.next;
    }
  }
}
