public class Account{
  public int kontoNummer;
  public double kontoStand;
  public double uberziehungsRahmen;
  public Customer inhaber;
  public Account(int konto, double uberziehung, Customer inh){
    this.kontoNummer = konto;
    this.uberziehungsRahmen = uberziehung;
    this.inhaber = inh;
    this.kontoStand = 0;
  }
  public Account(){
    this.kontoNummer = 0;
    this.uberziehungsRahmen = 0;
    this.kontoStand = 0;
  }
  public double getBalance(){
    return this.kontoStand;
  }
  public void deposit(double amount){
    this.kontoStand += amount;
  }
  public bool withdraw(double amount){
    if (this.kontoStand - amount >= 0 - this.uberziehungsRahmen ){
      this.kontoStand -= amount;
      return true;
    }
    else{
      return false;
    }
  }
}