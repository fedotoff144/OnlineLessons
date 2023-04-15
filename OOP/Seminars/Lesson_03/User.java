package Seminars.Lesson_03;

public class User implements Comparable<User> {
    private String firstName;
    private String lastName;
    private int age;
    private static Sorter sort;
    private Personal personal = new Personal(new User[]{});

    

    public Personal getPersonal() {
        return personal;
    }

    public static void setSorter(Sorter sort){
        User.sort = sort;
    }

    /** Construcors */
    public User(String firstName, String lastName, int age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
    public User(String firstName, String lastName, int age, User[] personal) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.personal = new Personal(personal);
    }

    public User() {
        this.firstName = "";
        this.lastName = "";
        this.age = 0;
    }
    /**Methods */
    @Override
    public String toString() {
        return "User {" + "firstName: " + firstName + "'\' lastName: " + lastName + "'\' age: " + age + "}";
    }

    // @Override
    // public int compareTo(User o) {
    // return this.age - o.age;
    // }
    @Override
    public int compareTo(User o) {
        return sort.Compare(this, o);
        // int conditionFirstName = firstName.compareTo(o.firstName);
        // if (conditionFirstName != 0) {
        //     return firstName.compareTo(o.firstName);
        // }

        // int conditionLastName = lastName.compareTo(o.lastName);
        // if (conditionLastName != 0) {
        //     return conditionLastName;
        // }
        
        // return this.age - o.age;
    }
    public static  abstract class Sorter{
        public abstract int Compare(User u1, User u2);
    }
    public static class SorterFirstName extends Sorter{
        @Override
        public int Compare(User u1, User u2) {
            return u1.firstName.compareTo(u2.firstName);
        }
    }
    public static class SorterLastName extends Sorter{
        @Override
        public int Compare(User u1, User u2) {
            return u1.lastName.compareTo(u2.lastName);
        }
    }
}
