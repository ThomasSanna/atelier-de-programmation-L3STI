package tests;

import classes.Adresse;
import classes.Employe;
import classes.Manager;
import classes.Personne;

public class TestQuestion2 {
  public static void main(String[] args) {
    // Création de deux objets Adresse
    Adresse adresse1 = new Adresse("123 Rue Principale", "Paris", 75000);
    Adresse adresse2 = new Adresse("456 Rue Secondaire", "Lyon", 69000);

    // Création de deux objets Personne
    Personne personne1 = new Personne("Dupont", "Jean", 30, adresse1);
    Personne personne2 = new Personne("Martin", "Luc", 25, adresse2);
    Personne personne3 = new Personne("Nommeur", "Marie", 40, adresse1);
    Personne personne4 = new Personne("Print", "Alban", 18, adresse1);
    
    Employe employe1 = Employe.createEmploye(personne1, 1022.0, "2022-03-22");
    Employe employe2 = Employe.createEmploye(personne2, 1500.0, "2020-05-30");
    Employe employe3 = Employe.createEmploye(personne3, 1000.0, "2023-01-01");
    Employe employe4 = Employe.createEmploye(personne4, 1000.0, "2023-12-31");

    // Affichage des informations des personnes
    System.out.println(employe1);
    System.out.println(employe2);
    System.out.println(employe3);
    System.out.println(employe4);

    System.out.println(employe3.getSalaire());

    Manager manager1 = new Manager(employe3);
    System.out.println(manager1.getSalaire());
  }
}
