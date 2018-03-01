public class Customer{
  public int kundenNummer;
  public string name;
  public string addresse;
  public string telefonNr;
  public Customer(){
    this.kundenNummer = 0;
    this.telefonNr = "";
    this.name = "";
    this.addresse = "";
  }
  public Customer(int kunde, string telefon, string nameKunde, string addresseKunde){
    this.kundenNummer = kunde;
    this.telefonNr = telefon;
    this.name = nameKunde;
    this.addresse = addresseKunde;
  }
}

