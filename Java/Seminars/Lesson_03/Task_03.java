import java.util.ArrayList;
import java.util.Collections;

public class Task_03 {
    public static void main(String[] args) {
        /*
         * создать два списка и совместить их
         */

        ArrayList<String> arrayFirst = new ArrayList<>();
        arrayFirst.add("Erth");
        arrayFirst.add("Mars");
        arrayFirst.add("Lune");
        arrayFirst.add("Jupyter");
        arrayFirst.add("Venere");
        System.out.println(arrayFirst);

        ArrayList<String> arraySeecond = new ArrayList<>();
        arraySeecond.add("one");
        arraySeecond.add("two");
        arraySeecond.add("three");
        // arraySeecond.add("four");
        // arraySeecond.add("five");
        System.out.println(arraySeecond);

        Collections.copy(arrayFirst, arraySeecond); // первый список заменили на второй
        System.out.println(arrayFirst);
        // если списка не равны то меняется часть списка

        Collections.reverse(arraySeecond);
        System.out.println(arraySeecond);

        ArrayList<String> newArr = (ArrayList<String>) arrayFirst.clone(); // при клонировании нужно явно указывать тип
        System.out.println(newArr);
        
        ArrayList<Object> arrayThird = new ArrayList<>();
        arrayThird.add("one");
        arrayThird.add("two");
        arrayThird.add("three");
        System.out.println(arrayThird);

    }
}
