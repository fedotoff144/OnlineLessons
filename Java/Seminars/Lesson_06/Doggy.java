package Lesson_06;

public class Doggy {
    String name;
    int age;
    String color;
    String gender;
    int id;

    static int count = 0;

    Doggy(String name, int age, String color, String gender, int id) {
        this.name = name;
        this.age = age;
        this.color = color;
        this.gender = gender;
        this.id = count + 1;
    }

    public void doggyWash() {
        System.out.println(this.name + " wash");
    }

    public void doggyRun() {
        System.out.println(this.name + " run");
    }

    public void doggyPlay() {
        System.out.println(this.name + " play");
    }

    public static void getCount() {
        System.out.println("you have - " + count + " dogs");
    }

    @Override
    public String toString() {
        return "dog #%d, name-%s, age %d, color %s, gender %s".format(this.id, this.name, this.age, this.color,
                this.gender);
    }
}
