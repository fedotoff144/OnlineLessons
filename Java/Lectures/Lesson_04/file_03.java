import java.util.Deque;
import java.util.LinkedList;

public class file_03 {
    public static void main(String[] args) {
        /*
         * Deque
         * Линейная коллекция, которая поддерживает вставку и удаление
         * элементов на обоих концах.
         */

        Deque<Integer> deque = new LinkedList<>();
        deque.addFirst(1);
        deque.addLast(9);
        deque.removeFirst();
        deque.removeLast();
        deque.offerFirst(2); // has Last
        deque.pollFirst(); // has Last
        deque.getFirst(); // has Last
        deque.peekFirst(); // has Last
        
    }
}
