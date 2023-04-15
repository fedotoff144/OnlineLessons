package armors;

public class ChainMail implements Armor{
    @Override
    public int protection() {
        return rnd.nextInt(5);
    }

    @Override
    public String toString() {
        return String.format("Кольчуга из чешуи дракона с защитой %d", protection());
    }
}
