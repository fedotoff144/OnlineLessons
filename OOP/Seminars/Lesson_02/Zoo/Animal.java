package Seminars.Lesson_02.Zoo;

import Seminars.Lesson_02.Zoo.Radio.Sayable;

public abstract class Animal implements Sayable {

    private String name;

    protected Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public abstract String feed();

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        if (this instanceof Runable) {
            str.append("speed run: " + ((Runable) this).getSpeedRun());
        }
        if (this instanceof Flyable) {
            str.append("speed fly: " + ((Flyable) this).getSpeedFly());
        }
        return String.format(str + "%s eating %s", this.name, this.feed());
    }
}
