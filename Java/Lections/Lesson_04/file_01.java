import java.util.LinkedList;
import java.util.Queue;

public class file_01{
    public static void main(String[] args) {
        /*
         * LinkedList нужен для небольшого количества
         * элементов, в которых операции добавления\удаления
         * встречаются чаще операций чтения.
         */
        
        Queue<Integer> queue = new LinkedList<Integer>(); // работает по принципу FIFO
        queue.add(1);
        queue.add(5);
        queue.add(9);
        queue.add(13);

        System.out.println(queue); // [1, 5, 9, 13]
        queue.remove();
        System.out.println(queue); // [5, 9, 13]
        queue.remove();
        System.out.println(queue); // [9, 13]
        int item = queue.remove();
        queue.add(item); // удаляет и добавляет элемент 
        System.out.println(queue); // [13, 9]
        queue.offer(100);
        System.out.println(queue); // [13, 9, 100]
        queue.poll();
        System.out.println(queue); // [9, 100]
        queue.element();
        queue.peek();
        queue.remove(100);
        System.out.println(queue);

    }
}