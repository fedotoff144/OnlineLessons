package Seminars.Lesson_02.Zoo.Predator;

public class Alligator extends Predator {
    
    public Alligator(String name){
        super(name);
    }

    @Override
    public String say() {
        return "Rrr";
    }
    
}
