import java.util.Scanner;

public class teste {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Entre quantas strings entrar: ");
		int num = entrada.nextInt();
		String[] numbers = new String[num];
		for(int index = 0; index < numbers.length; index++){
			numbers[index] = entrada.nextLine();
		}
		for(int index = 0; index < numbers.length; index++){
			System.out.println(numbers[index]);
		}
	}
}
