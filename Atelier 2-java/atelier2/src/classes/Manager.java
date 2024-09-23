package classes;

/**
 * La classe Manager représente un employé avec des responsabilités de gestion.
 * Elle hérite de la classe Employe et ajoute des fonctionnalités spécifiques aux managers.
 */
public class Manager extends Employe {
  private Secretaire secretaire;
  public double BONUS_SALAIRE_PAR_AN_POURCENTAGE = 0.5;

  /**
   * Constructeur de la classe Manager.
   * 
   * @param employe L'employé à promouvoir en tant que manager.
   */
  public Manager(Employe employe) {
    super(employe.getPersonne(), employe.getSalaire(), employe.getDateEmbauche());
    this.ajouterSalaireBonus();
  }

  /**
   * Ajoute un bonus au salaire du manager en fonction de son ancienneté.
   */
  private void ajouterSalaireBonus() {
    int nbAnnees = this.calculAnnuite();
    this.augmenterLeSalaire(BONUS_SALAIRE_PAR_AN_POURCENTAGE * nbAnnees);
  }

  /**
   * Définit le secrétaire associé au manager.
   * 
   * @param secretaire Le secrétaire à associer.
   */
  public void setSecretaire(Secretaire secretaire) {
    this.secretaire = secretaire;
  }

  /**
   * Obtient le secrétaire associé au manager.
   * 
   * @return Le secrétaire associé.
   */
  public Secretaire getSecretaire() {
    return this.secretaire;
  }

  /**
   * Retourne une représentation sous forme de chaîne de caractères du manager.
   * 
   * @return Une chaîne de caractères représentant le manager.
   */
  public String toString() {
    return super.toString() + " Il est manager.";
  }
}