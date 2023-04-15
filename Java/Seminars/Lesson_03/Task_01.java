import java.util.ArrayList;

public class Task_01{
    /*
     * Напишите программу по озданию нового списка массива
     * добавьте некоторые элементы и распечатайте коллкекции
     */
    public static void main(String[] args) {
        ArrayList<String> colors = new ArrayList<>();
        colors.add("black");
        colors.add("green");
        colors.add("red");
        colors.add("blue");
        colors.add("brown");

        colors.add(1, "yellow"); // добавление элемента
        colors.add(4, "pink"); // добавление элемента

        System.out.println(colors);

        colors.set(0, "white"); //  замена 0 элемента
        colors.remove(2); // удаление элемента по индексу

        for(String item:colors){System.out.print(item + " ");}
        System.out.println();

        System.out.println(colors.get(2)); // получение определенных элементов по их индексу
        System.out.println(colors.get(4)); // получение определенных элементов по их индексу

    }
}