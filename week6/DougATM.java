// Importing java scanner object
import java.util.Scanner;

public class DougATM {
	
	// Fields used throughout the class
	private double balance;
	private final double fee = 0.5;

	public static void main(String[] args) {
		
		DougATM account = new DougATM();
		
		// Scanner Object Creation
		Scanner scan = new Scanner(System.in);
		int s;
		// Asks for balance
		System.out.print("Please input your starting balence: ");
		account.setBalance(scan.nextDouble());
		// Processes withdrawal 
		while (true) {
		
			System.out.println("How much would you like to withdraw?");
			account.withdrawal(scan.nextDouble());
		
			System.out.println("Would you like to process another transaction? 1)Yes 2)No");
			s = scan.nextInt();
		
			if (s == 2) {
			
			break;
			
			} else if (s != 1 && s != 2) {
			
			System.out.println("Invalid Response");
			
			}

		}

	}
	
	public void withdrawal(double w) {
	
		if ((w + fee <= balance) && (w % 5 == 0)) {
			// Sets balence
			balance = balance - fee - w;
			// Prints out confirmation
			System.out.println("Tranaction Succesful!");
			System.out.printf("Withdrawal Amount: $%3.2f\n", w);

		} else if (w % 5 == 0) {
		
			System.out.println("Transaction Unsuccessful");
			System.out.println("Please Withdraw in Multiples of 5");
		
		} else {
		
			System.out.println("Transaction Unsuccessful");
			System.out.println("You do not have enough money withdraw");
		
		}
		
		System.out.printf("Current Balance: $%3.2f\n", balance);
	}
	
	public void setBalance(double b){
	
		balance = b;
	
	}

}
