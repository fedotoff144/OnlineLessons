public class Main {
    public static void main(String[] args) {
        MainView view = new MainView();
        MainController controller = new MainController(view);
        controller.run();
    }
}