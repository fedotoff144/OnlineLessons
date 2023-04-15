package Lesson_03;

public class file_03 {
    static int[] AddItem(int[] array, int item){
        int length = array.length;
        int[] temp = new int[length +1];
        System.arraycopy(array, 0, temp, 0, length);
        temp[length] = item;
        return temp;
    }
    public static void main(String[] args) {
        int[] a = new int[] {1, 2};
        for(int i : a){System.out.printf("%d ", i);}
        System.out.println();
        a = AddItem(a, 3);
        a = AddItem(a, 4);
        for(int i : a){System.out.printf("%d ", i);}
        
    }
    
}
