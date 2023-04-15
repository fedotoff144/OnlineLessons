import java.util.Scanner;

public class Task_02 {
    public static void main(String[] args) {
        // Написать программу, которая запросит пользователя ввести <Имя> в консоли.
        // Получит введенную строку и выведет в консоль сообщение “Привет, <Имя>!”

        Scanner scn = new Scanner(System.in);
        System.out.println("Enter our name: ");
        String username = scn.nextLine();
        System.out.println("Hello " + username + "!");
        scn.close();
    }
}
