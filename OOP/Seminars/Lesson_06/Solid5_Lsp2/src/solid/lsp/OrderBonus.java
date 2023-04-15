package solid.lsp;

public class OrderBonus extends AbstractOrder implements Orderable{

    public OrderBonus(int qnt, int price) {
        super(qnt, price);
    }

    @Override
    public int getAmount() {
        return 0;
    }
}
