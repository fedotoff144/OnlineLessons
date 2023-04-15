package Lesson_06;

public class Worker {
    int id;
    int salary;
    String firstName;
    String lastName;

    @Override
    public String toString() {
        return String.format("id: %d, salary: %d, firstName: %s, lastName: %s", id, salary, firstName, lastName);
    }

    public boolean equals(Object o) {
        var t = (Worker) o;
        return id == t.id && firstName == t.firstName;
    }

    @Override
    public int hashCode() {
        return id;
    }
}
