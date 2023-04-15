import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class file_03 {
    public static void main(String[] args) {
        try {
            String pathProject = System.getProperty("user.dir");
            String pathFile = pathProject.concat("/File.txt");
            File File = new File(pathFile);
            if (File.createNewFile()) {
                System.out.println("file.created");
            } else {
                System.out.println("file.existed");
            }
        } catch (Exception e) {
            System.out.println("catch");
        } finally {
            System.out.println("finally");
        }

        String line = "empty";
        try {
            String pathProj = System.getProperty("user.dir");
            String pathF = pathProj.concat("/file.txt");
            File file = new File(pathF);
            if (file.createNewFile()) { // false-файл уже есть, true-файл создастся
                System.out.println("file.created");
            } else {
                BufferedReader bufReader = new BufferedReader(new FileReader(file));
                System.out.println("file existed");
                line = bufReader.readLine();
                bufReader.close();
            }
        } catch (Exception e) {
            System.out.println("catch");
        } finally {
            System.out.println(line);
        }

        // isHidden(): возвращает истину, если каталог или файл является скрытым
        // length(): возвращает размер файла в байтах
        // lastModified(): возвращает время последнего изменения файла или каталога
        // list(): возвращает массив файлов и подкаталогов, которые находятся в каталоге
        // listFiles(): возвращает массив файлов и подкаталогов, которые находятся
        // в определенном каталоге
        // mkdir(): создает новый каталог
        // renameTo(File dest): переименовывает файл или каталог
        // lastModified(): возвращает время последнего изменения
        // файла или каталога

        String pathP = System.getProperty("user.dir");
        String pathDir = pathP.concat("/files");
        File dir = new File(pathDir);
        System.out.println(dir.getAbsolutePath());
        if(dir.mkdir()){
            System.out.println("+");
        } else {
            System.out.println("-");
        }
        for(String fname : dir.list()){
            System.out.println(fname);
        }
    }
}
