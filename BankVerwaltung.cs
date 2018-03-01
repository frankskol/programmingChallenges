using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace BankVerwaltung{
    class BankVerwaltung{
        public static void Main(string[] args){
            Bank raiffeisen = new Bank();
            string taste = "\n";
            string name;
            string address;
            int count = 0;
            string telefon;
            double rahmen;
            Customer[] customers = new Customer[100];
            int result;
            int kontoNr;
            double betrag;
            int vonKonto;
            int nachKonto;
            bool durchgefuehrt;
            while (taste != "q" ){
              Console.WriteLine("\n**************Bankverwaltung**************");
              Console.WriteLine("Kunde und Bankkonto anlegen ............ a");
              Console.WriteLine("Konto suchen ........................... s ");
              Console.WriteLine("Einzahlen .............................. e ");
              Console.WriteLine("Beheben ................................ b ");
              Console.WriteLine("Ueberweisung taetigen .................. t ");
              Console.WriteLine("Uebersicht drucken ..................... d ");
              Console.WriteLine("Beenden ................................ q ");
              Console.Write("Welche Menueoption? [a|s|e|b|t|d|q]:  ");
              taste = Console.ReadLine();
              switch (taste){
              case "a":
                  Console.WriteLine("\n*** Anlegen von Kunde und Konto *** ");
                  Console.Write("Kundenname: ");
                  name = Console.ReadLine();
                  Console.Write("Addresse: ");
                  address = Console.ReadLine();
                  Console.Write("Telefonnummer: ");
                  telefon = Console.ReadLine();
                  Console.Write("Ueberziehungsrahmen: ");
                  rahmen = Double.Parse(Console.ReadLine());
                  if (count < 100){
                  customers[count] = new Customer(raiffeisen.count, telefon, name, address);
                  result = raiffeisen.createAccount(customers[count], rahmen);
                  count++;
                  }
                  else{
                      result = raiffeisen.createAccount(customers[count], rahmen);
                  }
                  if (result != -1){
                      Console.WriteLine("Kontoinhaber   und   Konto   (#" + result + ") erfolgreich angelegt! ");
                  }
                  else{
                      Console.WriteLine("Konto konnte nicht erstellt werden! ");
                  }
                  break;
              case "b":
                  Console.WriteLine("*** Behebung taetigen ***");
                  Console.Write("Kontonummer: ");
                  kontoNr = Convert.ToInt32(Console.ReadLine());;
                  Console.Write("Behebungsbetrag: ");
                  betrag = Double.Parse(Console.ReadLine());
                  durchgefuehrt = raiffeisen.withdraw(kontoNr, betrag);
                  if (durchgefuehrt) Console.WriteLine("Behebung erfolgreich durchgefuehrt!");
                  else Console.WriteLine("Behebung konnte nicht durchgefuehrt werden!");
                    break;
              case "e":
                  Console.WriteLine("*** Einzahlung taetigen ***");
                  Console.Write("Kontonummer: ");
                  kontoNr = Convert.ToInt32(Console.ReadLine());
                  Console.Write("Einzahlungsbetrag: ");
                  betrag = Double.Parse(Console.ReadLine());
                  durchgefuehrt = raiffeisen.deposit(kontoNr, betrag);
                  if (durchgefuehrt) Console.WriteLine("Einzahlung erfolgreich durchgefuehrt!");
                  else Console.WriteLine("Einzahlung konnte nicht durchgefuehrt werden!");
                  break;
              case "d":
                  if(raiffeisen.count == 0) Console.WriteLine("Keine Konten!");
                  else raiffeisen.printAccounts();
                  break;
              case "s":
                  Console.WriteLine("*** Konto suchen *** ");
                  Console.Write("Name des Kunden: ");
                  name = Console.ReadLine();
                  if (raiffeisen.count == 0) Console.WriteLine("Keine Kunden!");
                  else raiffeisen.printAccount(name);
                  break;
              case "t":
                  Console.WriteLine("\n*** Ueberweisung taetigen *** ");
                  Console.Write("Von Kontonummer: ");
                  vonKonto = Convert.ToInt32(Console.ReadLine());;
                  Console.Write("Auf Kontonummer: ");
                  nachKonto = Convert.ToInt32(Console.ReadLine());
                  Console.Write("\nBetrag: ");
                  betrag = Double.Parse(Console.ReadLine());
                  durchgefuehrt = raiffeisen.transfer(vonKonto, nachKonto, betrag);
                  if (durchgefuehrt) Console.WriteLine("Ueberweisung erfolgreich durchgefuehrt!");
                  else Console.WriteLine("Ueberweisung konnte nicht durchgefuehrt werden!");
                  break;
               default:
                    Console.WriteLine("\n*** Keine gueltige Taste gedrückt *** ");
                    break;
              }
            }
        }
    }
}