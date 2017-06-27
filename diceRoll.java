import java.util.Random;

public class diceRoll{
  public static void main(String[] args) {

    Random rand = new Random();

    int  n = rand.nextInt(98) + 1;

    System.out.println(n);
  }
}
