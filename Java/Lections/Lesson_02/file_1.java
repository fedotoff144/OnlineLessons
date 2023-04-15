import java.lang.module.ModuleDescriptor.Builder;

public class file_1 {
    public static void main(String[] args) {
        // Время выполнения программы ниже 41000ms
        String str = "";
        for (int i = 0; i < 1_000_000; i++) {
            str += "+";
        }

        // Время выполнения программы ниже 9ms
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1_000_000; i++) {
            sb.append("+");
        }
        // Много преобразований используем StringBuilder
        // Много изменений используем String

        // программы полностью
        var s = System.currentTimeMillis();
        // String str = "";
        StringBuilder sb1 = new StringBuilder();
        for (int i = 0; i < 1_000_000; i++) {
            // str += "+";
            sb1.append("+");
        }
        System.out.println(System.currentTimeMillis() - s);
        // System.out.println(str);
        // System.out.println(sb);

        // concat(): объединение строк
        // valueOf(): преобразует Object в строковое представление (завязан на
        // toString())
        // join(): объединяет набор строк в одну с учетом разделителя
        // charAt(): получение символа по индексу
        // indexOf(): первый индекс вхождения подстроки
        // lastIndexOf(): последний индекс вхождения подстроки
        // startsWith()/endsWith(): определяет, начинается/заканчивается ли строка с
        // подстроки
        // replace(): замена одной подстроки на другую
        // trim(): удаляет начальные и конечные пробелы
        // substring(): возвращает подстроку, см.аргументы
        // toLowerCase()/toUpperCase(): возвращает новую строку в нижнем/верхнем
        // регистре
        // сompareTo(): сравнивает две строки
        // equals(): сравнивает строки с учетом регистра
        // equalsIgnoreCase(): сравнивает строки без учета регистра
        // regionMatches(): сравнивает подстроки в строках

        String[] name = { "А", "р", "т", "е", "м" };
        String sk = "Артем ка";
        System.out.println(sk.toLowerCase());
        System.out.println(String.join("", name));
        System.out.println(String.join("", "А", "р", "т", "е", "м"));

    }
}