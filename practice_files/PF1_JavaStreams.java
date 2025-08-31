import java.util.*;
import java.util.stream.*;

public class PF1_JavaStreams {

  public static void main(String[] args) {
    removeEmptyStringsFromArray();
  }

  public static void removeEmptyStringsFromArray() {
    List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");
    List<String> filtered = strings.stream()
                              .filter(string -> !string.isEmpty())
                              .collect(Collectors.toList());
    System.out.println();


    strings.stream().filter(string -> !string.isEmpty()).forEach(System.out::println);
                              // .collect(Collectors.toList());
  }
}
