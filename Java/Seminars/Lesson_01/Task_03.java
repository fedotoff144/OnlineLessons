import java.util.Scanner;

public class Task_03 {
    public static void main(String[] args) {
        // В консоли запросить имя пользователя. В зависимости от текущего времени,
        // вывести приветствие вида
        // "Доброе утро, <Имя>!", если время от 05:00 до 11:59
        // "Добрый день, <Имя>!", если время от 12:00 до 17:59;
        // "Добрый вечер, <Имя>!", если время от 18:00 до 22:59;
        // "Доброй ночи, <Имя>!", если время от 23:00 до 4:59

        Scanner scn = new Scanner(System.in);
        System.out.println("Enter our name: ");
        String username = scn.nextLine();
        System.out.println("Enter hour: ");
        String hour = scn.nextLine();
        System.out.println("Enter minutes: ");
        String minutes = scn.nextLine();
        int hours = Integer.parseInt(hour);
        int minute = Integer.parseInt(minutes);

        if (hours >= 5 && hours < 12) {
            System.out.println(username + "Good morning! Time now is " + hours + " : " + minute);
        }
        if (hours >= 12 && hours < 18) {
            System.out.println(username + "Good afternoon! Time now is " + hours + " : " + minute);
        }
        if (hours >= 18 && hours < 23) {
            System.out.println(username + "Good evening! Time now is " + hours + " : " + minute);
        }
        if (hours >= 23 || hours < 5) {
            System.out.println(username + "Good night! Time now is " + hours + " : " + minute);
        }
        scn.close();

    }
}
