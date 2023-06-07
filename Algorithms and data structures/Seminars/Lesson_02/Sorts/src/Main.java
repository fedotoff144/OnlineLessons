import java.util.Date;

public class Main {
    public static void MergeSort(int Array[]) {
        MergeSort(Array, 0, Array.length - 1);
    }

    final static int buf[] = new int[100000];
    public static void MergeSort(int Array[], int Left, int Right){
        if(Right - Left == 0){
            return;
        }
        int Mid = (Right + Left) / 2;
        MergeSort(Array, Left, Mid);
        MergeSort(Array, Mid + 1, Right);

        //int buf[] = new int[Array.length];
        int i = Left, j = Mid + 1, k = Left;

        while(i <= Mid && j <= Right){
            if(Array[i] < Array[j]){
                buf[k] = Array[i];
                k++;
                i++;
            }else{
                buf[k] = Array[j];
                k++;
                j++;
            }
        }

        while(i <= Mid){
            buf[k] = Array[i];
            k++;
            i++;
        }

        while(j <= Right){
            buf[k] = Array[j];
            k++;
            j++;
        }

        for(int q=Left; q<=Right; q++){
            Array[q] = buf[q];
        }
    }

    public static void insertSort(int Array[]){
        for(int i = 0; i < Array.length; i++){
            int pos = i;
            for(int j = i + 1; j < Array.length; j++){
                if(Array[j] < Array[pos]){
                    pos = j;
                }
            }
            if(pos != i){
                int temp = Array[i];
                Array[i] = Array[pos];
                Array[pos] = temp;
            }
        }
    }


    public static void bubbleSorter(int Array[]){     //МЕТОД ПУЗЫРЬКОВОЙ СОРТИРОВКИ
        for (int out = Array.length - 1; out >= 1; out--){  //Внешний цикл
            for (int in = 0; in < out; in++){       //Внутренний цикл
                if(Array[in] > Array[in + 1]) {               //Если порядок элементов нарушен
                    int dummy = Array[in];     //во временную переменную помещаем первый элемент
                    Array[in] = Array[in + 1];       //на место первого ставим второй элемент
                    Array[in + 1] = dummy;
                }//вызвать метод, меняющий местами
            }
        }
    }

    public static void test(){
        int Array[] = new int[100000];
        for(int i = 0; i < 100000; i++)
            Array[i] = (int)(Math.random() * 10000);

        int Array2[] = new int[100000];
        for(int i=0; i<100000; i++){
            Array2[i] = Array[i];
        }

        int Array3[] = new int[100000];
        for(int i=0; i<100000; i++){
            Array3[i] = Array[i];
        }

        Date start = new Date();
        bubbleSorter(Array);
        Date end = new Date();
        long time0 = end.getTime() - start.getTime();

        start = new Date();
        insertSort(Array);
        end = new Date();
        long time1 = end.getTime() - start.getTime();

        start = new Date();
        MergeSort(Array2);
        end = new Date();
        long time2 = end.getTime() - start.getTime();

        System.out.printf("time0: %d, time1: %d, time2: %d", time0, time1, time2);
    }

    public static Integer binSearch(int Array[], int value){
        int Left = 0, Right = Array.length - 1;
        while(Right - Left > 1){
            int Mid = (Left + Right) / 2;
            if(value > Array[Mid])
                Left = Mid;
            else
                Right = Mid;
        }
        if(Array[Left] == value)
            return Left;
        if(Array[Right] == value)
            return Right;
        return null;
    }

    public static void main(String[] args) {
//        int Array[] = new int[5];
//        for(int i = 0; i < 5; i++)
//            Array[i] = 5 - i;
//
//        for(int i : Array)
//            System.out.println(i);
//
//        //insertSort(Array);
//        MergeSort(Array);
//
//        for(int i : Array)
//            System.out.println(i);
        //test();

        int Array[] = new int[100000];
        for(int i = 0; i < 100000; i++)
            Array[i] = (int)(Math.random() * 10000);

        MergeSort(Array);

        System.out.println(binSearch(Array, 9));
        System.out.println(binSearch(Array, -1));
    }
}
