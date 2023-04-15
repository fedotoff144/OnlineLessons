public class Task_04 {
    public static void main(String[] args) {
        // Дан массив двоичных чисел, например [1,1,0,1,1,1], вывести максимальное
        // количество подряд идущих 1.

        int incount = 0;
        int rescount = 0;
        int[] arr = new int[] { 1, 1, 0, 1, 1, 1 };

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1) {
                incount++;
            } 
            else {
                if (incount > rescount) {
                    rescount = incount;
                    incount = 0;
                }
            }
            System.out.println(rescount);
        }
        
        // int incounter = 0;
        // int rescounter = 0;
        // int i = 0;
        // int[] arr = new int[] {1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1}; 
        // while (i < arr.length){
        //     if (arr[i] == 1){
        //         incounter++;
        //     }
        //     if (arr[i] != 1 || i == arr.length-1){
        //         if (incounter > rescounter){
        //             rescounter = incounter;
        //             incounter = 0;
        //         }
        //     }
        //     i++;
        // }
        // System.out.println(rescounter);
    }
}
