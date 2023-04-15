import java.util.ArrayDeque;

public class Task_02 {
    public static void main(String[] args) {
        // очередь из объектов Person
        ArrayDeque<Person> people = new ArrayDeque<Person>();
        people.addFirst(new Person("Tom"));
        people.addLast(new Person("Nick"));
        // перебор без извлечения
        for(Person p : people){

        System.out.println(p.getName());
        }
    }
}
class Person{
    public String name;
    public Person(String value){
        name = value;
    }
    String getName(){
        return name;
    }
}
