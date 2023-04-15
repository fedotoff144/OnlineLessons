package solid.srp;

public class SquareView {
    private int side;
    private int scale;
    private int  scaledSide;

    public SquareView(int side, int scale) {
        this.side = side;
        this.scale= scale;
        scaledSide = side * scale;
    }

    public void draw() {
        printHorizontalBorder();
        printVerticalBorder();
        printHorizontalBorder();
    }

    private void printVerticalBorder() {
        System.out.println();
        for (int i = 0; i < scaledSide - 2; i++) {
            System.out.print("* ");
            for (int j = 1; j < scaledSide - 1; j++) {
                System.out.print("  ");
            }
            System.out.println("*");
        }
    }

    private void printHorizontalBorder() {
        for (int i = 0; i < scaledSide; i++) {
            System.out.print("* ");
        }
    }
}
