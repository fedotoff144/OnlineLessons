package Lesson_05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task_02 {
    public static void main(String[] args) {
        /*
         * дана последовательност чисел, необходимо вернуть число совпадающих пар в этой
         * последовательности
         * пример 1: In arr = [1, 2] Out: 0
         * пример 2 In arr = [1, 1, 2] Out: 1
         * пример 3 In arr = [1, 1, 1, 2, 2] Out: 4
         */
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2));
        System.out.println(getNumberOfCouple(list));

    }

    public static Integer getNumberOfCouple(List<Integer> list) {
        int count = 0;
        for (int i = 0; i < list.size(); i++) {
            for (int j = i + 1; j < list.size(); j++) {
                if (list.get(i) == list.get(j)) {
                    count++;
                }
            }
        }
        return count;
    }
}
