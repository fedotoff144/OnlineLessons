package Lesson_06;

import java.util.Arrays;
import java.util.TreeSet;

public class file_03 {
    public static void main(String[] args) {
        /*
         * TreeSet
         * ● В основе HashMap.
         * ● Упорядочен по возрастанию.
         * ● null’ов быть не может.
         */
        var x = new TreeSet<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7));
        var y = new TreeSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 1));
        System.out.println(x); // [1, 2, 3, 4, 5, 6, 7]
        System.out.println(y); // [1, 2, 3, 5, 7, 11, 13]
        System.out.println(x.headSet(4)); // [1, 2, 3]
        System.out.println(x.tailSet(4)); // [4, 5, 6, 7]
        System.out.println(x.subSet(3,5)); // [3, 4]
        System.out.println(x.contains(1)); // true

    }
}
