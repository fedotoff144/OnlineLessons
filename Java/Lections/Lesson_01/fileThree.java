public class fileThree {
    public static void main(String[] args) {
        // Классы - обертки
        /*
         * Примитив Обертка
         * int      Integer
         * short    Short
         * long     Long
         * byte     Byte
         * float    Float
         * double   Double
         * char     Character
         * boolean  Boolean
         */
        System.out.println(Integer.MAX_VALUE); // 2147483647
        System.out.println(Integer.MIN_VALUE); // -2147483648

        // Массивы
        int[] arr = new int[10];
        System.out.println(arr.length);
        int[] array = new int[] { 1, 2, 3, 4, 5, 6, 77, 66, 55 };
        System.out.println(array.length);

        int[] arr1[] = new int[4][4]; // [m][n] m-rows, n-columns
        for (int[] line : arr1) {
            for (int item : line) {
                System.out.printf("%d", item); // %d задается целочисленное число
            }
            System.out.println();
        }
        System.out.println();

        int[][] arr2 = new int[3][5]; // [m][n] m-rows, n-columns
        for (int i = 0; i < arr2.length; i++) {
            for (int j = 0; j < arr2[i].length; j++) {
                System.out.printf("%d", arr2[i][j]); // %d задается целочисленное число
            }
            System.out.println();
        }
                // Преобразования
        /*
        *       char->         ->float
        *byte->short->int->long->double
        *                ->double
        *                ->float
        */
        int it = 123;
        double d = it;
        System.out.println(it);//123
        System.out.println(d);//123.0
        d = 3.1415; it = (int)d;
        System.out.println(d);//3.1415
        System.out.println(it);//3
        d = 3.9999; it = (int)d;
        System.out.println(d);//3.9999
        System.out.println(it);//3
        byte b = Byte.parseByte("123");
        System.out.println(b);//123
        b = Byte.parseByte("1234");//NumberFormatException: Value out of range
        System.out.println(b);
    }
}
