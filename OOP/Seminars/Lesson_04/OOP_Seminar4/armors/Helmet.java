package armors;

import java.util.Random;

public class Helmet implements Armor{
    @Override
    public int protection() {
        return rnd.nextInt(3);
    }

    @Override
    public String toString() {
        return String.format("Воинский шлем с защитой %d", protection());
    }
}
