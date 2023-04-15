package Lesson_03;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class file_05 {
    public static void main(String[] args) {
        int day = 6;
        int month = 1;
        int year = 1987;
        Integer[] date = { day, month, year };
        List<Integer> d = Arrays.asList(date);
        System.out.println(d); // [6, 1, 1987]

        StringBuilder days = new StringBuilder("06");
        StringBuilder months = new StringBuilder("01");
        StringBuilder years = new StringBuilder("1987");
        StringBuilder[] dates = { days, months, years };
        List<StringBuilder> ds = Arrays.asList(dates);
        System.out.println(ds);
        dates[1] = new StringBuilder("99"); // значение меняем в массиве но меняется и коллекция
        System.out.println(ds);

        /*
         * clear() – очистка списка
         * toString() – «конвертация» списка в строку
         * Arrays.asList – преобразует массив в список
         * containsAll(col) – проверяет включение всех элементов из col
         * removeAll(col) – удаляет элементы, имеющиеся в col
         * retainAll(col) – оставляет элементы, имеющиеся в col
         * toArray() – конвертация списка в массив Object’ов
         * toArray(type array) – конвертация списка в массив type
         * List.copyOf(col) – возвращает копию списка на основе имеющегося
         * List.of(item1, item2,...) – возвращает неизменяемый список
         */

        Character value = null;
        List<Character> list1 = List.of('S', 'e', 'r', 'g', 'e', 'y');
        System.out.println(list1);
        // list1.remove(1); // immutable - java.lang.UnsupportedOperationException
        List<Character> list2 = List.copyOf(list1);

        Character value1 = null;
        List<Character> lists = new ArrayList<Character>();
        lists.add('S');
        lists.add('e');
        lists.add('r');    
        System.out.println(lists);
        lists.remove(1); // при таком написании ошибок нет
        System.out.println(lists);
        List<Character> listk = List.copyOf(lists);
    }
}
