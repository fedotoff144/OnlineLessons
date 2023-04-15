import java.util.TreeMap;

public class file_02 {
    public static void main(String[] args) {
        /*
         * TreeMap
         * ключевая особенность в том что происходит упорядочивание по ключу
         * 
         */
        TreeMap<Integer, String> tree = new TreeMap<>();
        tree.put(1, "one");
        tree.put(2, "two");
        tree.put(3, "three");
        System.out.println(tree); // {1=one, 2=two, 3=three}
        System.out.println(tree.descendingKeySet()); // [3, 2, 1]
        System.out.println(tree.values()); // [one, two, three]
        System.out.println(tree.descendingMap()); // {3=three, 2=two, 1=one}
    }
}
