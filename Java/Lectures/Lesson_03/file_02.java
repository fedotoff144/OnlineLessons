package Lesson_03;

public class file_02 {
    public static void main(String[] args) {
        int[] a = new int[] { 1, 2 };
        int[] b = new int[3];
        System.arraycopy(a, 0, b, 0, a.length);

        for (int i : a) { System.out.printf("%d ", i);}
        System.out.println();
        for (int j : b) { System.out.printf("%d ", j);}
    }
}
