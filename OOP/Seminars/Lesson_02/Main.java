package Seminars.Lesson_02;

import java.util.List;

import Seminars.Lesson_02.Zoo.*;
import Seminars.Lesson_02.Zoo.Herbivores.Cow;
import Seminars.Lesson_02.Zoo.Herbivores.Duck;
import Seminars.Lesson_02.Zoo.Herbivores.Goat;
import Seminars.Lesson_02.Zoo.Predator.Alligator;
import Seminars.Lesson_02.Zoo.Predator.Lion;
import Seminars.Lesson_02.Zoo.Radio.Radio;
import Seminars.Lesson_02.Zoo.Radio.Sayable;

public class Main {
    public static void main(String[] args) {

        List<Animal> animalList = List.of(
                new Alligator("Gena"),
                new Lion("Simba"),
                new Cow("Burenka"),
                new Goat("Koza"),
                new Duck("DonaldDuck"));

        Zoo zoo = new Zoo(animalList, new Radio());

        for (Sayable animal : zoo.getSayable()) {
            System.out.print(((Animal) animal).getName() + ": ");
            System.out.println(animal.say());
        }
        System.out.println("--------------------------");
        for (Runable animal : zoo.getRunable()) {
            System.out.println(((Animal) animal).getName());
            System.out.println(((Animal) animal).say());
            System.out.println(" speed: " + animal.getSpeedRun() + "\n");
        }
        System.out.println("--------------------------");
        for (Flyable animal : zoo.getFlyable()) {
            System.out.println(((Animal) animal).getName());
            System.out.println(((Animal) animal).say());
            System.out.println("speed: " + animal.getSpeedFly());
            System.out.println(" high: " + animal.getHigh() + "\n");
        }
        System.out.println("--------------------------");
        System.out.println(zoo.getRunChempion());
        System.out.println(zoo.getFlyChempion());

    }
}