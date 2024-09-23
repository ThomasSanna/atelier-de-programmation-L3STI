package classes;
import java.time.LocalDate;
import java.time.Period;

/**
 * La classe Employe représente un employé avec un salaire et une date d'embauche.
 * Elle hérite de la classe Personne.
 */
public class Employe extends Personne {
  private double salaire;
  private String dateEmbauche;

  /**
   * Constructeur de la classe Employe.
   * 
   * @param personne La personne à promouvoir en tant qu'employé.
   * @param salaire Le salaire de l'employé.
   * @param dateEmbauche La date d'embauche de l'employé.
   */
  protected Employe(Personne personne, double salaire, String dateEmbauche) {
    super(personne.getNom(), personne.getPrenom(), personne.getAge(), personne.getAdresse());
    this.salaire = salaire;
    this.dateEmbauche = dateEmbauche;
  }

  /**
   * Crée un employé en vérifiant l'âge.
   * 
   * @param personne La personne à promouvoir en tant qu'employé.
   * @param salaire Le salaire de l'employé.
   * @param dateEmbauche La date d'embauche de l'employé.
   * @return Un objet Employe si l'âge est valide, sinon null.
   */
  public static Employe createEmploye(Personne personne, double salaire, String dateEmbauche) {
    if (personne.getAge() <= 16 || personne.getAge() >= 65) {
      System.out.println("L'âge doit être supérieur à 16 et inférieur à 65.");
      return null;
    } else {
      return new Employe(personne, salaire, dateEmbauche);
    }
  }

  /**
   * Augmente le salaire de l'employé.
   * 
   * @param pourcentage Le pourcentage d'augmentation.
   */
  public void augmenterLeSalaire(double pourcentage) {
    double montantAjout = 1 + (pourcentage / 100);
    this.salaire *= montantAjout;
  }

  /**
   * Calcule l'ancienneté de l'employé.
   * 
   * @return Le nombre d'années d'ancienneté.
   */
  public int calculAnnuite() {
    LocalDate date = LocalDate.parse(this.dateEmbauche);
    LocalDate dateAujourdhui = LocalDate.now();
    Period period = Period.between(date, dateAujourdhui);
    return period.getYears();
  }

  /**
   * Obtient le salaire de l'employé.
   * 
   * @return Le salaire de l'employé.
   */
  public double getSalaire() {
    return this.salaire;
  }

  /**
   * Obtient la date d'embauche de l'employé.
   * 
   * @return La date d'embauche de l'employé.
   */
  public String getDateEmbauche() {
    return this.dateEmbauche;
  }

  /**
   * Obtient la personne associée à cet employé.
   * 
   * @return Un objet Personne représentant l'employé.
   */
  public Personne getPersonne() {
    return new Personne(this.getNom(), this.getPrenom(), this.getAge(), this.getAdresse());
  }

  /**
   * Définit le salaire de l'employé.
   * 
   * @param salaire Le salaire de l'employé.
   */
  public void setSalaire(double salaire) {
    this.salaire = salaire;
  }

  /**
   * Retourne une représentation sous forme de chaîne de caractères de l'employé.
   * 
   * @return Une chaîne de caractères représentant l'employé.
   */
  public String toString() {
    return this.getNom() + " (" + this.getAge() + " ans), a un salaire de " + this.salaire + ". Employé le " + dateEmbauche + ".";
  }
}