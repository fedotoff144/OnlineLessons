package Seminars.Lesson_02.Zoo;

import java.util.ArrayList;
import java.util.List;

import Seminars.Lesson_02.Zoo.Radio.Sayable;

public class Zoo {
    List<Animal> animalsList = new ArrayList<>();
    Sayable radio;

    public Zoo(List<Animal> animal, Sayable sayableObj) {
        this.radio = sayableObj;
        animalsList.addAll(animal);
    }

    public void addAnimal(Animal animal) {
        animalsList.add(animal);
    }

    public void addAnimal(List<Animal> animal) {
        animal.addAll(animal);
    }

    public List<Animal> getAnimalList() {
        return animalsList;
    }

    public List<Sayable> getSayable() {
        List<Sayable> sayableList = new ArrayList<>();
        for (Animal animal : this.animalsList) {
            sayableList.add(animal);
        }
        sayableList.add(this.radio);
        return sayableList;
    }

    public List<Runable> getRunable() {
        List<Runable> runableList = new ArrayList<>();
        for (Animal animal : this.animalsList) {
            if (animal instanceof Readable) {
                runableList.add((Runable) animal);
            }
        }
        return runableList;
    }

    public List<Flyable> getFlyable() {
        List<Flyable> flyableList = new ArrayList<>();
        for (Animal animal : this.animalsList) {
            if (animal instanceof Flyable) {
                flyableList.add((Flyable) animal);
            }
        }
        return flyableList;
    }

    public Animal getRunChempion() {
        List<Runable> runners = getRunable();
        Runable runChempion = runners.get(0);
        for (Runable r : runners) {
            if (runChempion.getSpeedRun() < r.getSpeedRun()) {
                runChempion = r;
            }
        }
        return (Animal) runChempion;
    }

    public Animal getFlyChempion() {
        List<Flyable> flyers = getFlyable();
        Flyable flyChempion = getFlyable().get(0);
        for (Flyable f : flyers) {
            if (flyChempion.getSpeedFly() < f.getSpeedFly()) {
                flyChempion = f;
            }
        }
        return (Animal) flyChempion;
    }
}
