import java.util.Stack;

public class file_04 {
    public static void main(String[] args) {
        /*
         * Stack представляет собой обработку данных по принципу LIFO.
         * Расширяет Vector пятью операциями, которые позволяют рассматривать
         * вектор как стек.
         */

        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(12);
        stack.push(123);
        System.out.println(stack.pop()); // 123
        System.out.println(stack.pop()); // 12
        System.out.println(stack.pop()); // 1

        /*
         * Stack и Vector не рекомендованы
         * к использованию
         */
    }
}
