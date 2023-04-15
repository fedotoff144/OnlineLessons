import java.util.Hashtable;
import java.util.Map;

public class file_04 {
    public static void main(String[] args) {
        /*
         * HashTable
         * «Устаревший брат» коллекции HashMap,
         * который не знает про null
         */

        Map<Integer, String> ht = new Hashtable<>();
        ht.put(1, "one");
        ht.put(2, "two");
        ht.put(3, "three");
        System.out.println(ht); // {3=three, 2=two, 1=one}
        // ht.put(null, "four"); // // java.lang.NullPointerException
    }
}
