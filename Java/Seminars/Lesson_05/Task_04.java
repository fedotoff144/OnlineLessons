package Lesson_05;

// import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class Task_04 {
    public static void main(String[] args) {
        /*
         * Дана строка. Напишите метод, который отсортирует слова в строке по длине с
         * помощью TreeMap
         * Строки с одинаковой длиной не должны потеряться
         */
        String str = "слова в Строке по длине с помощью";
        System.out.println(getSortedIncludesWords((mapSplitAndSort(str))));
    }

    public static Map<Integer, String> mapSplitAndSort(String str) {
        Map<Integer, String> map = new TreeMap<>();
        for (String i : str.split(" ")) {
            map.put(i.hashCode(), i);
        }
        System.out.println(map);
        return map;
    }

    public static String getSortedIncludesWords(Map<Integer, String> map) {
        return String.join(" ", map.values());
    }
}
