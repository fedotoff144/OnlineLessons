import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class file_01 {
    public static void main(String[] args) {
        /*
         * HashMap
         * 
         * Map – это множество коллекций, работающих с данными
         * по принципу <Ключ / Значение>.
         * Ключевые особенности:
         * ● допускаются только уникальные ключи, значения могут повторяться;
         * ● помните про null значения*;
         * ● ускоренная обработка данных;
         * ● порядок добавления не запоминается.
         * В HashMap элементы располагаются как угодно и могут
         * менять свое положение.
         */

        Map<Integer, String> map = new HashMap<>();
        Map<Integer, String> map1 = new HashMap<>(9); // размер класса
        Map<Integer, String> map2 = new HashMap<>(9, 1.0f); // коэф при котором происходит увеличение класса
        
        map.put(1, "one");
        map.put(2, "two");
        map.put(3, "three");
        map.put(31, "three one");
        System.out.println(map.get(31)); // three one
        map.put(null, "!null");
        System.out.println(map.containsValue("two")); // true
        map.put(8, null);
        System.out.println(map.keySet()); // [null, 1, 2, 3, 8, 31]
        // System.out.println(map.remove(3));
        System.out.println(map.values()); // [!null, one, two, three, null, three one]
        map.put(null, null);
        System.out.println(map); // {null=null, 1=one, 2=two, 3=three, 8=null, 31=three one}

        for(var item:map.entrySet()){
            System.out.printf("[%d : %s]\n", item.getKey(), item.getValue());
        }

        /*
         * put(K,V) – добавить пару если или изменить значение,если ключ имеется.
         * putIfAbsent(K,V) – произвести добавление если ключ не найден.
         * get(K) - получение значения по указанному ключу.
         * remove(K) – удаляет пару по указанному ключу.
         * containsValue(V) – проверка наличия значения.
         * containsKey(V) – проверка наличия ключа.
         * keySet() – возвращает множество ключей.
         * values() – возвращает набор значений.
         */

    }
}