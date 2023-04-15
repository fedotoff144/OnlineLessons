package Lesson_06;

import java.util.Arrays;
import java.util.HashSet;

public class file_02 {
    public static void main(String[] args) {
        /*
         * addAll(Coll) – объединение множеств.
         * retainAll(Coll) – пересечение множеств.
         * removeAll(Coll) – разность множеств.
         */
        var a = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7));
        var b = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17));
        var c = new HashSet<Integer>(a);
        c.addAll(b);
        var d = new HashSet<Integer>(a);
        d.retainAll(b);
        var e = new HashSet<Integer>(a);
        e.removeAll(b);
        System.out.println(a);// [1, 2, 3, 4, 5, 6, 7]
        System.out.println(b);// [17, 2, 3, 5, 7, 11, 13]
        System.out.println(c);// [1, 17, 2, 3, 4, 5, 6, 7, 11, 13]
        System.out.println(d);// [2, 3, 5, 7]
        System.out.println(e);// [1, 4, 6]
        boolean res = a.addAll(b);
        System.out.println(res); // true

        /*
         * ﬁrst()
         * last()
         * headSet(E)
         * tailSet(E)
         * subSet(E1, E2)
         */
    }
}
