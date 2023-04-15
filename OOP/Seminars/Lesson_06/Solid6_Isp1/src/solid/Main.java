package solid;

import solid.isp.InternetPaymentService;
import solid.isp.TerminalPaymentService;

public class Main {
    public static void main(String[] args) {
        InternetPaymentService internetService = new InternetPaymentService();
        internetService.payWebMoney(10);
        internetService.payPhoneNumber(5);
        internetService.payCreditCard(15);

        TerminalPaymentService terminalService = new TerminalPaymentService();
        terminalService.payWebMoney(10);
        terminalService.payCreditCard(15);
    }
}
