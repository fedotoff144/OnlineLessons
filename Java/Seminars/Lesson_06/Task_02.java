package Lesson_06;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Task_02 {
    /*
     * Напишите метод, который заполнит массив из 1000 элементов случайными цифрами
     * от 0 до 24.
     */

    /*
     * создайте метод,в который перпедайте заполненный выше массив и с помощью Set
     * вычислите процент уникальных
     * значений в данном массиве и верните его в виде числа с плавающей запятой
     * для вычисления процента используйте формулу
     * процент уникальных чисел = число уникальных чисел * 100 / на общее количество
     * чисел в массиве.
     */
    public static void main(String[] args) {
        
        System.out.println(getPercentUniqueValues(initArray()) + "%");
    }

    public static Integer[] initArray() {
        Integer[] arr = new Integer[1000];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 25);
        }
        return arr;
    }

    public static double getPercentUniqueValues(Integer[] array) {
        Set<Integer> hs = new HashSet<>(Arrays.asList(array));
        double res = hs.size() / 10;
        return res;
    }
}
