public class fileSix {
    public static void main(String[] args) {
        // Циклы
        // цикл while;
        // цикл do while;
        // цикл for; и его модификация for in

        int val = 321;
        int count = 0;
        while (val != 0) {
        val /= 10;
        count++;
        }
        System.out.println(count);

        do {
        val /= 10;
        count++;
        } while (val != 0);
        System.out.println(count);

        int s = 0;
        for (int i = 0; s < 5; i++) {
        s += 1;
        }
        System.out.println(s);

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();

        // for работает только с коллекцией
        int arr[] = new int[5];
        for (int item : arr) {
            System.out.printf("%d", item);
        }
        System.out.println();
    }
}
