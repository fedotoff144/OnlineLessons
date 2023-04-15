package Seminars.Lesson_02.Zoo.Predator;

import Seminars.Lesson_02.Zoo.Animal;

public abstract class Predator extends Animal {

    public Predator(String name){
        super(name);
    }
    @Override
    public String toString() {
        return super.toString();
    }

    @Override
    public String feed() {
        return "meat";
    }
    
}
