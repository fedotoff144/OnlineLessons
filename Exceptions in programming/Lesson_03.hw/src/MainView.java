import java.util.Scanner;

public class MainView {
    private Scanner scanner;

    public MainView() {
        scanner = new Scanner(System.in);
    }

    public String[] getData() {
        String[] data;
        while (true) {
            System.out.println("Введите следующие данные, разделенные пробелом: Фамилия Имя Отчество Дата рождения Номер телефона Пол");
            String input = scanner.nextLine();

            data = input.split("\\s+");

            if (data.length == 6) {
                if(validData(data))
                    break;
            } else {
                System.out.println("Ошибка: Неверное количество введенных данных");
            }
        }
        return data;
    }

    public boolean validData(String[] data){
        boolean result = true;
        for(int i=0;i<=2;i++){
            if(!data[i].toUpperCase().matches("^[a-zA-Z]+$")){
                System.out.println(data[i] + " - используйте только буквы");
                result = false;
            }
        }
        if(!data[3].matches("^(0[1-9]|[12][0-9]|3[01])\\.(0[1-9]|1[0-2])\\.(19|20)\\d{2}$")){
            System.out.println(data[3] + " - не соответствует формату заполнения даты рождения");
            result = false;
        }
        if(!data[4].matches("\\d+")){
            System.out.println(data[4] + " - используйте только цифры");
            result = false;
        }
        if(data[5].length()==1){
            if(!data[5].equalsIgnoreCase("M") && !data[5].equalsIgnoreCase("F")){
                System.out.println(data[5] + " - используйте только латинские буквы M/F");
                result = false;
            }
        }else {
            System.out.println(data[5] + " - длина должна быть равна 1");
            result = false;
        }
        return result;
    }
    // Other methods for user input and output
}