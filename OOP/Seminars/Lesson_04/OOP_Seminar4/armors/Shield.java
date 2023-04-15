package armors;

public class Shield implements Armor{
    @Override
    public int protection() {
        return rnd.nextInt(7);
    }

    @Override
    public String toString() {
        return String.format("Щит квадратный металлический с защитой %d", protection());
    }
}
