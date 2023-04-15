package solid.lsp;

public class AbstractOrder {
    protected int qnt;
    protected int price;

    public AbstractOrder(int qnt, int price){
        this.qnt = qnt;
        this.price = price;
    }
    @Override
    public String toString() {
        return String.format("Количество = %d, Цена = %d", qnt, price);
    }
}
