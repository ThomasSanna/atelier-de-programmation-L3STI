package tests;

import classes.Adresse;
import classes.Personne;

public class TestQuestion1 {
  public static void main(String[] args) {
    // Création de deux objets Adresse
    Adresse adresse1 = new Adresse("123 Rue Principale", "Paris", 75000);
    Adresse adresse2 = new Adresse("456 Rue Secondaire", "Lyon", 69000);

    // Création de deux objets Personne
    Personne personne1 = new Personne("Dupont", "Jean", 30, adresse1);
    Personne personne2 = new Personne("Martin", "Luc", 25, adresse2);

    // Affichage des informations des personnes
    personne1.afficher();
    personne2.afficher();

    // Test de la méthode plusAgeeQue
    Personne plusAgee = personne1.plusAgeeQue(personne2);
    System.out.println("La personne la plus âgée est : " + plusAgee);

    // Test de la méthode statique plusAgee
    Personne plusAgeeStatique = Personne.plusAgee(personne1, personne2);
    System.out.println("La personne la plus âgée (méthode statique) est : " + plusAgeeStatique);

    // Test de la méthode statique personneEqual
    boolean sontEgales = Personne.personneEqual(personne1, personne2);
    System.out.println("Les deux personnes sont-elles égales ? " + sontEgales);

    // Affichage du nombre total de personnes créées
    System.out.println("Nombre total de personnes créées : " + Personne.getNbPersonnes());
  }
}
