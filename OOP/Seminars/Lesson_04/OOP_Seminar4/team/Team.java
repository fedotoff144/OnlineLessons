package team;

import items.DistanceAttacker;
import items.Warrior;

import java.util.ArrayList;
import java.util.List;

public class Team<T extends Warrior>{
    private List<T> team = new ArrayList<>();
    private String teamName;

    public Team(String teamName){
        this.teamName = teamName;
    }

    public Team<T> addWarrior(T warrior){
        team.add(warrior);
        return this;
    }

    public int getMaxDistance(){
        int distance = 0;
        for (T item: team){
            if(!(item instanceof DistanceAttacker)){
                continue;
            }
            DistanceAttacker temp = (DistanceAttacker) item;
            if (temp.getDistance() > distance){
                distance = temp.getDistance();
            }
        }
        return distance;
    }

    public int getTeamDamage(){
        int res = 0;
        for (T item: team){
            res += item.getMaxDamage();
        }
        return res;
    }
    public int getMinArmor(){
        int res = team.get(0).getMinArmor();
        for (int i = 1; i < team.size(); i++){
            if (team.get(i).getMinArmor() < res){
                res = team.get(i).getMinArmor();
            }
        }
        return res;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (T item: team){
            sb.append(item.toString() + "\n");
        }

        return String.format("Команда %s нанесет максимальный урон %d атакует на дистанции %d. Самая слабая броня команды %d", teamName, getTeamDamage(), getMaxDistance(), getMinArmor());
    }
}
