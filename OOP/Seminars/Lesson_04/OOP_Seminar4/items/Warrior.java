package items;

import armors.Armor;
import weapons.Weapon;

import java.util.Random;

public abstract class Warrior<T extends Weapon, V extends Armor> {
    private String name;
    protected T weapon;
    protected V shield;
    protected V helmet;
    protected V chainmail;
    protected Random rnd = new Random();
    private int healthPoint;


    public Warrior(String name, T weapon, V helmet, V chainmail, V shield) {
        this.name = name;
        this.weapon = weapon;
        this.helmet = helmet;
        this.chainmail = chainmail;
        this.shield = shield;
        healthPoint = 100;
    }

    public int getHealthPoint() {
        return healthPoint;
    }

    public void reduceHealthPoint(int damage) {

        this.healthPoint -= damage ;
    }

    public int hitDamage(Warrior enemy) {
        int damage = rnd.nextInt(weapon.damage());
        enemy.reduceHealthPoint(damage);
        return damage;
    }

    public int getMaxDamage() {
        return weapon.damage();
    }

    public int getMinArmor(){
        int res = helmet.protection();
        if (chainmail.protection() < res){
            res = chainmail.protection();
        }
        if (shield.protection() < res){
            res = shield.protection();
        }
        return res;
    }

    @Override
    public String toString() {
        return String.format("Воин %s вооружен %s %d единиц здоровья", name, weapon, healthPoint);
    }
}
