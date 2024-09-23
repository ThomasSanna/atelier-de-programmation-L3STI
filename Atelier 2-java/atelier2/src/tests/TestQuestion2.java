package tests;

import classes.Adresse;
import classes.Employe;
import classes.Manager;
import classes.Personne;
import classes.Secretaire;

public class TestQuestion2 {
  public static void main(String[] args) {
    // Création de deux objets Adresse
    Adresse adresse1 = new Adresse("123 Rue Principale", "Paris", 75000);
    Adresse adresse2 = new Adresse("456 Rue Secondaire", "Lyon", 69000);

    // Création de quatre objets Personne
    Personne personne1 = new Personne("Dupont", "Jean", 30, adresse1);
    Personne personne2 = new Personne("Martin", "Luc", 25, adresse2);
    Personne personne3 = new Personne("Nommeur", "Marie", 40, adresse1);
    Personne personne4 = new Personne("Print", "Alban", 18, adresse1);
    
    Employe employe1 = Employe.createEmploye(personne1, 1022.0, "2022-03-22");
    Employe employe2 = Employe.createEmploye(personne2, 1500.0, "2020-05-30");
    Employe employe3 = Employe.createEmploye(personne3, 1000.0, "2023-01-01");
    Employe employe4 = Employe.createEmploye(personne4, 1000.0, "2023-12-31");

    // Affichage des informations des employés
    System.out.println(employe1);
    System.out.println(employe2);
    System.out.println(employe3);
    System.out.println(employe4);

    // Création d'un manager
    Manager manager1 = new Manager(employe3);
    System.out.println(manager1.getSalaire());

    // Création d'un secrétaire
    Secretaire secretaire1 = new Secretaire(employe1);
    System.out.println(secretaire1);

    // Ajout de managers au secrétaire
    secretaire1.ajouterManager(manager1);
    System.out.println("Salaire après ajout de manager1 : " + secretaire1.getSalaire());

    // Création et ajout d'un autre manager
    Manager manager2 = new Manager(employe2);
    secretaire1.ajouterManager(manager2);
    System.out.println("Salaire après ajout de manager2 : " + secretaire1.getSalaire());

    // Retrait d'un manager
    secretaire1.retirerManager(manager1);
    System.out.println("Salaire après retrait de manager1 : " + secretaire1.getSalaire());

    // Test de la limite de managers
    Manager manager3 = new Manager(employe4);
    secretaire1.ajouterManager(manager3);
    secretaire1.ajouterManager(manager1); // Réajout de manager1
    secretaire1.ajouterManager(manager2); // Réajout de manager2
    secretaire1.ajouterManager(manager3); // Réajout de manager3
    System.out.println("Salaire après tentative d'ajout de plus de 5 managers : " + secretaire1.getSalaire());
  }
}