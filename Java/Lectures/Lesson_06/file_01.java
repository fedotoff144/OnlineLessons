package Lesson_06;

import java.util.HashSet;
import java.util.Set;

public class file_01 {
    public static void main(String[] args) {
        /*
         * Set
         * ● Коллекции, содержащие уникальные элементы.
         * ● Быстрая работа с данными.
         * ● «Основан» на Map’ах без пары.
         * ● Порядок добавления не хранится.
         */

        /*
         * HashSet
         * isEmpty() – проверка на пустоту.
         * add(V) – добавление элемента в коллекцию.
         * remove(V) – удаление элемента из коллекцию.
         * contains(V) – проверка на включение элемента в коллекции.
         * clear() – удаление всех элементов коллекции.
         * size() – возвращает количество элементов коллекции.
         */

        Set<Integer> set = new HashSet<>();
        set.add(1);
        set.add(12);
        set.add(123);
        System.out.println(set.contains(12)); // true
        set.add(null);
        System.out.println(set.size()); // 4
        System.out.println(set); // [null, 1, 123, 12]
        set.remove(1); // remove 1
        for (var item : set) {
            System.out.println(item);
        }
        set.clear();
        System.out.println(set); // []

     
    }
}
