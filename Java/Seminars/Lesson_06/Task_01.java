package Lesson_06;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;

public class Task_01 {
    public static void main(String[] args) {
        /*
         * Создайте HashSet заполните его числами (1,2,3,2,4,5,6,3)
         * распечатайте содержимое данного множества
         */
        System.out.println(new HashSet<>(Arrays.asList(1, 2, 3, 2, 4, 5, 6, 3)));

        /*
         * Создайте LinkedHashSet заполните его числами (1,2,3,2,4,5,6,3)
         * распечатайте содержимое данного множества
         */
        System.out.println(new LinkedHashSet<>(Arrays.asList(1, 2, 3, 2, 4, 5, 6, 3)));

        /*
         * Создайте TreeSet заполните его числами (1,2,3,2,4,5,6,3)
         * распечатайте содержимое данного множества
         */
        System.out.println(new TreeSet<>(Arrays.asList(1, 2, 3, 2, 4, 5, 6, 3)));

    }

}
