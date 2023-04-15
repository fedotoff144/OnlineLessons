public class fileOne {
    public static void main(String[] args) {
        // BASIC
        System.out.println("This is good!");
        short num = 10; // 10
        String msg = "And again Hi World";
        int salary = 150_000; // 150000
        System.out.println(num);
        System.out.println(msg);
        System.out.println(salary);
        float mass = 82.5f; // 82.5 'f' писать обязательно
        double pi = 3.1415d; // 3.1415 'D' or 'd' не обязательно
        // double в два раза больше чем float
        System.out.println(mass);
        System.out.println(pi);
        char ch = '1';
        System.out.println(Character.isDigit(ch)); // true
        ch = 'a';
        System.out.println(Character.isDigit(ch)); // false
        boolean flag1 = 123 <= 124;
        System.out.println(flag1); // true
        boolean flag2 = 123 >= 124;
        System.out.println(flag2); // false

        // условное OR ||, условное AND &&, равенство ==, инверсия NOT !
        // побитовые операторы |, &, ^
        // ^ Возвращает true, если один и только один из операндов равен true.
        // Возвращает false, если оба операнда равны true или false. По сути, возвращает
        // true, если операнды — разные.
        // | Возвращает true если хотя бы один из операндов равен true.
        // || То же самое, что и |, но если оператор слева является true, оператор
        // возвращает true без проверки второго операнда.
        // & Возвращает true если оба операнда равны true.
        // && То же самое, что и &, но если операнд, находящийся слева от & является
        // false, данный оператор возвращает false без проверки второго операнда.

        // Дизъюнкцией n высказываний называется предложение вида , которое ложно тогда
        // и только тогда,
        // когда ложны все составляющие его высказывания.

        boolean flag3 = flag1 ^ flag2;
        System.out.println(flag3); // | дизъюнкция, ^ строгая дизьюнкция
        // Конъюнкцией n высказываний называется предложение вида , которое истинно
        // тогда и только тогда,
        // когда истинны все составляющие его высказывания.
        
        boolean flag4 = flag1 & flag2; // &
        System.out.println(flag4);

        // Неявная типизация
        var a = 123; //123
        System.out.println(a);
        var b = 123.456; //123.456
        System.out.println(b);
        System.out.println(getType(a)); //Integer
        System.out.println(getType(b)); //Double
        b = 1022; //1022
        System.out.println(b); // 1022
        //d = "mistake";
        //error: incompatible types:
        //String cannot be converted to double


    }
    static String getType(Object o){
        return o.getClass().getSimpleName();
    }

}