import java.util.ArrayList;
import java.util.Collections;

public class Task_02 {
    public static void main(String[] args) {
        /*
         * найти элемент в списке и если он есть то вывести его в терминал
         * если  нет оповестить что такого элемента нет
         * отсортировать список
         */

         ArrayList<String> colors = new ArrayList<>();
         colors.add("black");
         colors.add("green");
         colors.add("red");
         colors.add("blue");
         colors.add("brown");

         System.out.println(colors);

         if(colors.contains("red")){
            System.out.println("Element found");
         } else{
            System.out.println("Element not found");
         }
         Collections.sort(colors); // сортировка списка
         System.out.println(colors);
    }
    
}
