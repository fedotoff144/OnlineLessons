public class fileFive {
    // Область видимости переменных

    // У переменных существует понятие «область видимости».
    // Если переменную объявили внутри некоторого блока фигурных скобок { },
    // то снаружи этого блока переменная будет недоступна

    static void sayHi() {
        System.out.println("say Hi!");
    }

    static int sum(int a, int b) {
        return a + b;
    }

    static double factor(int n) {
        if (n == 1)
            return 1;
        return n * factor(n - 1);
    }

    public static void main(String[] args) {

        sayHi();
        System.out.println(sum(5, 4));
        System.out.println(factor(5));

        // Управляющие конструкции. Условный оператор

        int a = 10;
        int b = 20;
        int c;
        if (a > b) {
            c = a;
        } else {
            c = b;
        }
        System.out.println(c);

        int q = 10;
        int w = 20;
        int e = 0;
        if (q > w) e = q;
        if (w > q) e = w;
        System.out.println(e);

        int v = 12;
        int s = 112;
        int min = v > s ? v : s; // если условие верно то вывод v, если нет то s
        System.out.println(min);


        // Оператор выбора или быдлокодинг)

        int opsw = 2;
        String text = "";
        switch (opsw) {
            case 1: text = "is good!";
                break;
            case 2: text = "is not good!";
                break;
            default: text = "is very bad...";
                break;
        }
        System.out.println(text);
    }
}
