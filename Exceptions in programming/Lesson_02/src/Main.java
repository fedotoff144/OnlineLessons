import java.io.*;

public class Main {
    final static int lenghtConst = 2;

    public static void main(String[] args) {

        try {
            String[][] content = readFile("D:\\GeekBrains\\OnlineLessons\\Exceptions in programming\\Lesson_02\\src\\test.txt");
            SwapQuestion(content);
            for (int i = 0; i < content.length; i++) {
                for (int j = 0; j < content[i].length; j++) {
                    System.out.print(content[i][j]);
                }
                System.out.println();
            }
            FileWrite(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void FileWrite(String[][] inArray) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("D:\\GeekBrains\\OnlineLessons\\Exceptions in programming\\Lesson_02\\src\\testOut.txt"));
            for (int i = 0; i < inArray.length; i++) {
                StringBuilder temp = new StringBuilder();
                for (int j = 0; j < inArray[i].length; j++) {
                    if (inArray[i][j].equals("")) break;
                    temp.append(inArray[i][j]);
                }
                temp.append("\n");
                writer.write(temp.toString());
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String[][] SwapQuestion(String[][] inArray) {
        for (int i = 0; i < inArray.length; i++) {
            for (int j = 0; j < inArray[0].length; j++) {
                if (inArray[i][j] == null) {
                    inArray[i][j] = "";
                }
                if (inArray[i][j].equals("?")) {
                    inArray[i][j] = "" + (j - 1);
                }
            }
        }
        return inArray;
    }

    public static String[][] readFile(String fileName) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(fileName));
        String line = "";
        String ls = System.getProperty("line.separator");
        int lenghtFirst = 0;
        int lenghtSecond = -1;
        while ((line = reader.readLine()) != null) {
            lenghtFirst++;
            if (lenghtSecond < line.length()) {
                lenghtSecond = line.length();
            }
        }
        reader.close();
        reader = new BufferedReader(new FileReader(fileName));

        String[][] data = new String[lenghtFirst][lenghtSecond + lenghtConst];
        for (int i = 0; i < lenghtFirst; i++) {
            if ((line = reader.readLine()) != null) {
                for (int j = 0; j < line.length(); j++) {

                    data[i][j] = "" + line.charAt(j);
                }
            }

        }

        reader.close();
        return data;
    }

}