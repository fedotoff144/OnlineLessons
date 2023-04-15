package solid;

import solid.srp.Point;
import solid.srp.Square;
import solid.srp.SquareCalculate;
import solid.srp.SquareView;

public class Main {
    public static void main(String[] args) {
        int side = 5;
        int scale = 1;
        Square square = new Square(new Point(1,1), 5);
        System.out.printf("Площадь фигуры: %d \n", new SquareCalculate(side).getArea());
        new SquareView(side, scale).draw();
    }
}
