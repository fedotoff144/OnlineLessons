package weapons;

public class Bow implements Weapon{
    private int distance = 30;

    public int getDistance(){
        return distance;
    }


    @Override
    public int damage() {
        return 50;
    }

    @Override
    public String toString() {
        return String.format("Лук, дальность стрельбы %d, урон %d", distance, damage());
    }
}
