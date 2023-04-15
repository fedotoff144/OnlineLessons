package Seminars.Lesson_02.Zoo.Herbivores;

public class Cow extends Herbivores{
    
    public Cow(String name){
        super(name);
    }
    @Override
    public String say() {
        return "Mouu";
    }
    
}
