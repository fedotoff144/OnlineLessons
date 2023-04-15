import java.util.ArrayDeque;

public class Task_01{
    public static void main(String[] args) {
        ArrayDeque<String> states = new ArrayDeque<>();
        states.add("Vladimirskaya obl"); // элемент добавили в конец
        states.addFirst("Moscow"); // элемент добавили в начало
        states.addLast("Bryanskaya obl"); // элемент добавили в конец
        states.add("Kirovscaya obl"); // элемент доавили в конец

        System.out.println(states.getFirst()); // Moscow
        System.out.println(states.getLast()); // Kirovscaya obl

        while(states.peek() != null){
            System.out.println(states.pop());
        }
    }
}