import java.util.LinkedHashMap;
import java.util.Map;

public class file_03 {
    public static void main(String[] args) {
        /*
         * LinkedHashMap
         * «Старший брат» коллекции HashMap, который все помнит…
         * Помнит порядок добавления элементов ➜ более медлительный
         */
        Map<Integer, String> linkmap = new LinkedHashMap<>();
        linkmap.put(1,"one");
        linkmap.put(2,"two");
        linkmap.put(3,"three");
        System.out.println(linkmap);
        
    }
}
