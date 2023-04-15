package Lesson_05;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Task_03 {
    public static void main(String[] args) {
        /*
         * дан массив путей, где пути [i] = ["City A", "City B"], означает что существует прямой путь, идущий от "City A" до "City B"
         * Верните город назначения, то есть город без какого либо пути, ведущего в другой город.
         * Пример 1: [["Москва", "Самара"], ["Курск", "Пенза"], ["Самара", "Курск"]] Output: Пенза
         * Пример 2: ["Москва", "Самара"] Output: Самара
         */
        Map<String, String> cityes = new HashMap<>();
        cityes.put("Москва", "Самара");
        cityes.put("Курск", "Пенза");
        cityes.put("Самара", "Курск");

        System.out.println(getFinalyCity(cityes));
    }
    public static String getFinalyCity(Map<String, String> arr){
        List<String> tmp = new ArrayList<>(arr.values());
        for(String item:tmp){
            if(arr.containsKey(item)){
                continue;
            }
            return item;
        }
        return "Такого города нет";
    }
}
