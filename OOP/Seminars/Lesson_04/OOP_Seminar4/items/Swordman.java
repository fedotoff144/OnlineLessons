package items;

import armors.Armor;
import armors.ChainMail;
import armors.Helmet;
import armors.Shield;
import weapons.Sword;

public class Swordman extends Warrior<Sword, Armor>{

    public Swordman(String name, Sword weapon, Helmet helmet, ChainMail chainMail, Shield shield){
        super(name, weapon, helmet, chainMail, shield);

    }

    @Override
    public String toString() {
        return super.toString() + "Специализация - мечник";
    }
}
