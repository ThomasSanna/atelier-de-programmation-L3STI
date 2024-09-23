package classes;
import java.util.ArrayList;

/**
 * La classe Secretaire représente un employé avec des responsabilités de secrétariat.
 * Elle hérite de la classe Employe et ajoute des fonctionnalités spécifiques aux secrétaires.
 */
public class Secretaire extends Employe {
  private double salaireDeBase;
  private ArrayList<Manager> managers = new ArrayList<>();
  private static final double BONUS_SALAIRE_PAR_MANAGER = 0.1;

  /**
   * Constructeur de la classe Secretaire.
   * 
   * @param employe L'employé à promouvoir en tant que secrétaire.
   */
  public Secretaire(Employe employe) {
    super(employe.getPersonne(), employe.getSalaire(), employe.getDateEmbauche());
    this.salaireDeBase = employe.getSalaire();
  }

  /**
   * Recalcule le salaire du secrétaire en fonction du nombre de managers associés.
   */
  private void recalculerSalaireBonus() {
    double pourcentage = managers.size() * BONUS_SALAIRE_PAR_MANAGER;
    double nouveauSalaire = getSalaireDeBase() * (1 + pourcentage / 100);
    setSalaire(nouveauSalaire);
  }

  /**
   * Ajoute un manager au secrétaire.
   * 
   * @param manager Le manager à ajouter.
   */
  public void ajouterManager(Manager manager) {
    if (this.managers.size() < 5) {
      if (this.managers.contains(manager)) { // Vérifie si le manager est déjà associé
        System.out.println("Le manager " + manager.getNom() + " est déjà associé à cette secrétaire.");
      } else {
        this.managers.add(manager);
        manager.setSecretaire(this);
        recalculerSalaireBonus();
      }
    } else {
      System.out.println("Le nombre maximum de managers est atteint.");
    }
  }

  /**
   * Retire un manager du secrétaire.
   * 
   * @param manager Le manager à retirer.
   */
  public void retirerManager(Manager manager) {
    if (this.managers.contains(manager)) {
      this.managers.remove(manager);
      manager.setSecretaire(null);
      recalculerSalaireBonus();
    } else {
      System.out.println("Le manager n'est pas associé à cette secrétaire.");
    }
  }

  /**
   * Augmente le salaire de base du secrétaire.
   * 
   * @param pourcentage Le pourcentage d'augmentation.
   */
  public void augmenterLeSalaire(double pourcentage) {
    double montantAjout = 1 + (pourcentage / 100);
    this.salaireDeBase *= montantAjout;
    recalculerSalaireBonus();
  }

  /**
   * Obtient le salaire de base du secrétaire.
   * 
   * @return Le salaire de base.
   */
  private double getSalaireDeBase() {
    return this.salaireDeBase;
  }

  /**
   * Retourne une représentation sous forme de chaîne de caractères du secrétaire.
   * 
   * @return Une chaîne de caractères représentant le secrétaire.
   */
  public String toString() {
    return super.toString() + " Il est secrétaire.";
  }
}