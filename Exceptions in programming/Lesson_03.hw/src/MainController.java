import java.io.FileWriter;
import java.io.IOException;

public class MainController {
    private MainView view;

    public MainController(MainView view) {
        this.view = view;
    }

    public void run() {
        String[] data = view.getData();

        String lastName = data[0].toUpperCase();
        String firstName = data[1].toUpperCase();
        String surname = data[2].toUpperCase();
        String dateOfBirth = data[3];
        String phoneNumber = data[4];
        String gender = data[5].toUpperCase();

        Person person = new Person(lastName, firstName, surname, dateOfBirth, phoneNumber, gender);

        try {
            FileWriter fileWriter = new FileWriter(lastName + ".txt", true);
            fileWriter.write(person.getLastName() + " "
                    + person.getFirstName() + " "
                    + person.getSurname() + " "
                    + person.getDateOfBirth() + " "
                    + person.getPhoneNumber() + " "
                    + person.getGender() + "\n");
            fileWriter.close();
            System.out.println("Данные успешно записаны в файл: " + person.getLastName() + ".txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}