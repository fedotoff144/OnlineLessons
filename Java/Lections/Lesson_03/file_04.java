package Lesson_03;

import java.util.ArrayList;
import java.util.List;

public class file_04 {
    public static void main(String[] args) {
        /*
         * List – пронумерованный набор элементов.
         * Пользователь этого интерфейса имеет точный контроль над тем,
         * где в списке вставляется каждый элемент.
         * Пользователь может обращаться к элементам по их целочисленному
         * индексу (позиции в списке) и искать элементы в списке.
         * к листу относится:
         * ArrayList, LinkedList (Vector, Stack – устаревшие)
         */
        ArrayList list = new ArrayList();
        list.add(2809);
        list.add("string line");
        for (Object o : list) {
            System.out.println(o);
        } // видим предупреждения но вывод происходит

        ArrayList list2 = new ArrayList();
        list2.add(21);
        list2.add("321");
        for (Object o : list2) {System.out.println(o);} // видим предупреждения но вывод происходит

        ArrayList<Integer> list1 = new ArrayList<Integer>();
        list1.add(12);
        list1.add(123);
        for (Object o : list1) {System.out.println(o);} // предупреждений нет так как указываем тип

        /*
         * не обязательно второй раз указывать тип после =
         * ArrayList<Integer> list1 = new ArrayList<Integer>();
         * ArrayList<Integer> list2 = new ArrayList<>();
         * ArrayList<Integer> list3 = new ArrayList<>(10); - хранилище под 10 элементов
         * ArrayList<Integer> list4 = new ArrayList<>(list3);
         */

         

        /*
         * add(args) – добавляет элемент в список ( в т.ч. на нужную позицию)
         * get(pos) – возвращает элемент из списка по указанной позиции
         * indexOf(item) – первое вхождение или -1
         * lastIndexOf(item) – последнее вхождение или -1
         * remove(pos) – удаление элемента на указанной позиции и его возвращение
         * set(int pos, T item) – gjvtoftn значение item элементу, который находится
         * на позиции pos
         * void sort(Comparator) – сортирует набор данных по правилу
         * subList(int start, int end) – получение набора данных от позиции start до end
         */
    }
}
