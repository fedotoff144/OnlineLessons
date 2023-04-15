import java.io.IOException;
import java.util.logging.*;

public class file_04 {
    public static void main(String[] args) throws IOException {
        // Логирование

        // Использование
        // Logger logger = Logger.getLogger()
        // Уровни важности
        // INFO, DEBUG, ERROR, WARNING и др.
        // Вывод
        // ConsoleHandler info = new ConsoleHandler();
        // log.addHandler(info);
        // Формат вывода: структурированный, абы как*
        // XMLFormatter, SimpleFormatter

        // Ввыод лога в консоль
        Logger logger = Logger.getLogger(file_04.class.getName());
        ConsoleHandler ch = new ConsoleHandler();
        logger.addHandler(ch);
        // SimpleFormatter sFormat = new SimpleFormatter();
        // ch.setFormatter(sFormat);
        XMLFormatter xmlForm = new XMLFormatter();
        ch.setFormatter(xmlForm);
        logger.log(Level.WARNING, "Тестовое логгирование 1");
        logger.info("Тестовое логгирование 2");


        // Сохранение лога в файл
        Logger log = Logger.getLogger(file_04.class.getName());
        FileHandler fh = new FileHandler("log.xml");
        log.addHandler(fh);
        XMLFormatter xmlform = new XMLFormatter();
        fh.setFormatter(xmlform);
        logger.log(Level.WARNING, "Test 1");
        logger.info("Test 2");

    }
}
