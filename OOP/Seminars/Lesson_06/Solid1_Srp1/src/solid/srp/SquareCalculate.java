package solid.srp;

public class SquareCalculate {
    private int side;

    public SquareCalculate(int side) {
        this.side = side;
    }

    public int getArea() {
        return side * side;
    }
}
