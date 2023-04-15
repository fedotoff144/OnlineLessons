package Lesson_06;

import java.util.ArrayList;
import java.util.Arrays;

public class Task_03 {
    /*
     * Продумайте структуру класса Бульдожка. Какие поля и методы будут актуальны
     * для приложения, которое является
     * а) информационной системой ухода за ней
     * б) архивом выставки бульдожков
     * в) информационной системой Театра бульдожек имени Дарахвелидзе
     */
    public static void main(String[] args) {
        Doggy dog1 = new Doggy("Stuf", 5, "black", "male");
        Doggy dog2 = new Doggy("Eva", 3, "white", "women");
        dog1.doggyPlay();
        dog1.doggyWash();
        Doggy.getCount();
        List<Doggy> doglist = new ArrayList<>(Arrays.asList(dog1,dog2));
        System.out.println(doglist);
    }
}
