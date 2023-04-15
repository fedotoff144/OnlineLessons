package solid.lsp;

public class Order extends AbstractOrder implements Orderable{
    public Order(int qnt, int price) {
        super(qnt, price);
    }
    @Override
    public int getAmount() {
        return qnt * price;
    }

}
