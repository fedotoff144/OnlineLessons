package Seminars.Lesson_02.Zoo.Herbivores;

import Seminars.Lesson_02.Zoo.Flyable;
import Seminars.Lesson_02.Zoo.Runable;

public class Duck extends Herbivores implements Flyable, Runable {
    private int flySpeed = 15;
    private int flyHigh = 5;
    private int speedRun = 10;

    public Duck(String name) {
        super(name);
    }

    @Override
    public String say() {
        return "Krya-krya";
    }

    public int getSpeedFly() {
        return this.flySpeed;
    }

    public int getHigh() {
        return this.flyHigh;
    }

    public int getSpeedRun() {
        return this.speedRun;
    }
}
