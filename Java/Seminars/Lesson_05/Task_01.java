package Lesson_05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task_01 {
    public static void main(final String[] args) {
        // дана последовательность чисел, необходимо вернуть сумму уникальных чисел
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9, 7, 9));
        System.out.println("Сумма уникальных чисел: " + getSumOfUniqueValues(list));

    }

    public static Integer getSumOfUniqueValues(List<Integer> list) {
        int sum = 0;
        for (int item : list) {
            if (list.indexOf(item) == list.lastIndexOf(item)) {
                sum += item;
            }
        }
        return sum;
    }
}
