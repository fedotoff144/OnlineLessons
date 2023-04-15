package Seminars.Lesson_03;

import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        
        User.setSorter(new User.SorterLastName());

        User[] BillKlinton = new User[]{new User("Monika", "Levinsky", 45),
                            new User("Monika", "Levinsky", 45),
        };
        
        User[] users = new User[] { new User("Bill", "Klinton", 50, BillKlinton),
                new User("Bill", "Gatse", 90),
                new User("Tom", "Kruz", 51),
                new User("Joe", "Baeden", 190),
                new User("Chipolino", "Rodaria", 9) };

        Personal personal = new Personal(users);

        for (User user : personal) {
            System.out.println(user);
        }

        List<User> myUsers = personal.ToList();
        Collections.sort(myUsers);
        System.out.println("---------------------------------");
        for (User user : myUsers) {
            System.out.println(user);
        }
        User Boss = new User("Alex", "Makedonsky", 50, users);

        Company company = new Company(Boss);
        System.out.println("---------------------------------");
        // for (User user : company) {
        //     System.out.println(user);
        // }
        company.forEach(item->System.out.println(item));
    }

}
