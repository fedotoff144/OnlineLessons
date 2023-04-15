import java.io.File;

public class file_02 {
    public static void main(String[] args) {
        // try {
        // Код, в котором может появиться ошибка
        // } catch (Exception e) {
        // Обработка, если ошибка случилась
        // }
        // finally {
        // Код, который выполнится в любом случае
        // }

        
        String pathProg = System.getProperty("user.dir");
        String pathFiles = pathProg.concat("/files.txt");
        File f3 = new File(pathFiles);
        System.out.println(f3.getAbsolutePath());
        // /home/artemfedotov/Education/Online/Java/Lesson_02/file.txt

        try {
            String pathProject = System.getProperty("user.dir");
            String pathFile = pathProject.concat("/file.txt");
            File f = new File(pathFile);
            System.out.println("Try");
        } catch (Exception e) {
            System.out.println("Catch");
        } finally {
            System.out.println("Finally");
        }
    }
}
