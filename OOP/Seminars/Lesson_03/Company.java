package Seminars.Lesson_03;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Company implements Iterable<User>{
    User BigBoss;

    public Company(User bigBoss) {
        BigBoss = bigBoss;
    }

    private List<User> getColectUser(User user){
        List<User> result = new ArrayList<>();
        result.add(user);
        for(User item:user.getPersonal()){
            result.addAll(getColectUser(item));
        }
        return result;
    }

    @Override
    public Iterator<User> iterator() {
        return getColectUser(BigBoss).iterator();
    }
}
