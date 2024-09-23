package classes;
import java.time.LocalDate;
import java.time.Period;

public class Employe extends Personne {
  private double salaireDeBase;
  private double salaire;
  private String dateEmbauche;

  protected Employe(Personne personne, double salaire, String dateEmbauche) {
    // if (age <= 16 || age >= 65) {
    //   throw new IllegalArgumentException("L'âge doit être supérieur à 16 et inférieur à 65.");
    // }
    super(personne.getNom(), personne.getPrenom(), personne.getAge(), personne.getAdresse());
    this.salaire = salaire;
    this.salaireDeBase = salaire;
    this.dateEmbauche = dateEmbauche;
  }

  public static Employe createEmploye(Personne personne, double salaire, String dateEmbauche) {
    if (personne.getAge() <= 16 || personne.getAge() >= 65) {
      System.out.println("L'âge doit être supérieur à 16 et inférieur à 65.");
      return null;
    } else {
      return new Employe(personne, salaire, dateEmbauche);
    }
  }

  public void augmenterLeSalaire(double pourcentage) {
    double montantAjout = 1 + (pourcentage/100);
    this.salaire *= montantAjout;
  }

  public int calculAnnuite() {
    LocalDate date = LocalDate.parse(this.dateEmbauche);
    LocalDate dateAujourdhui = LocalDate.now();
    Period period = Period.between(date, dateAujourdhui);
    return period.getYears();
  }

  public double getSalaire() {
    return this.salaire;
  }
  public double getSalaireDeBase() {
    return this.salaireDeBase;
  }
  public String getDateEmbauche() {
    return this.dateEmbauche;
  }
  public Personne getPersonne() {
    return new Personne(this.getNom(), this.getPrenom(), this.getAge(), this.getAdresse());
  }
  public void setSalaire(double salaire) {
    this.salaire = salaire;
  }

  public String toString() {
		return this.getNom() + " (" + this.getAge() + " ans), a un salaire de " + this.salaire + ". Employé le " + dateEmbauche + ".";
	}

}
