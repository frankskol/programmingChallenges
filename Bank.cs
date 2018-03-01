using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
public class Bank{
    public int count = 0;
    public Account[] accounts = new Account[100];
    public int createAccount(Customer owner, double overdraftLimit){
        if (count < 100){
            accounts[count] = new Account(count, overdraftLimit, owner);
            count++;
            return (count-1);
        }
        else{
            return -1;
        }
    }
    public bool deposit(int accountNo, double amount){
        if (accountNo <= 100 && accountNo >=0 && accountNo <= count){
            accounts[accountNo].deposit(amount);
            return true;
        }
        else{
            return false;
        }
    }
    public bool withdraw(int accountNo, double amount){
        if (accountNo <= 100 && accountNo >=0 && accounts[accountNo].kontoStand - amount >= 0 - accounts[accountNo].uberziehungsRahmen && accountNo < count){
            accounts[accountNo].withdraw(amount);
            return true;
        }
        else{
            return false;
        }
    }
    public bool transfer(int fromAccountNo, int toAccountNo, double amount){
        if (fromAccountNo <= 100 && fromAccountNo >=0 && fromAccountNo <= count && accounts[fromAccountNo].kontoStand - amount >= 0 - accounts[fromAccountNo].uberziehungsRahmen ){
            if(toAccountNo <= 100 && toAccountNo >=0 && toAccountNo <= count){
                accounts[fromAccountNo].withdraw(amount);
                accounts[toAccountNo].deposit(amount);
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
    public double getAccountBalance(int accountNo){
        return accounts[accountNo].getBalance();
    }
    public double getBalance(){
        double sum = 0;
        for (int i = 0; i < count; i++){
            sum += accounts[i].getBalance();
        }
        return sum;
    }
    public void printAccounts(){
        Console.WriteLine("-------------\nBankauszug\n-------------");
        for (int i = 0; i < count; i++){
            Console.WriteLine("Kontonummer: " + accounts[i].kontoNummer);
            Console.WriteLine("Kontoinhaber: " + accounts[i].inhaber.name);
            Console.WriteLine("Adresse: " + accounts[i].inhaber.addresse);
            Console.WriteLine("Telefonnummer: " + accounts[i].inhaber.telefonNr);
            Console.WriteLine("Kontostand: " + accounts[i].kontoStand);
            Console.WriteLine("Ueberziehungsrahmen: " + accounts[i].uberziehungsRahmen);
            Console.WriteLine("---------------------------------------");
        }
        Console.WriteLine("Bilanzsumme: \n" + this.getBalance() + "\n---------------------------------------");
    }
    public void printAccount(string customerName){
        Console.WriteLine("-------- Konten von \"" + customerName +"\" --------" );
        for (int i = 0; i < count; i++){
            if (accounts[i].inhaber.name.IndexOf(customerName) != -1){
                Console.WriteLine("Kontonummer: " + accounts[i].kontoNummer);
                Console.WriteLine("Kontoinhaber: " + accounts[i].inhaber.name);
                Console.WriteLine("Adresse: " + accounts[i].inhaber.addresse);
                Console.WriteLine("Telefonnummer: " + accounts[i].inhaber.telefonNr);
                Console.WriteLine("Kontostand: " + accounts[i].kontoStand);
                Console.WriteLine("Ueberziehungsrahmen: " + accounts[i].uberziehungsRahmen);
                Console.WriteLine("---------------------------------------");
            }
        }

    }
}
