package classes;
import java.util.ArrayList;

public class Secretaire extends Employe {
  private ArrayList<Manager> managers = new ArrayList<>();
  private static final double BONUS_SALAIRE_PAR_MANAGER = 0.1;

  public Secretaire(Employe employe) {
    super(employe.getPersonne(), employe.getSalaire(), employe.getDateEmbauche());
  }

  private void recalculerSalaireBonus() {
    double bonusTotal = managers.size() * BONUS_SALAIRE_PAR_MANAGER;
    double nouveauSalaire = getSalaireDeBase() + bonusTotal;
    setSalaire(nouveauSalaire);
  }

  public void ajouterManager(Manager manager) {
    if (this.managers.size() < 5) {
      this.managers.add(manager);
      manager.setSecretaire(this);
      recalculerSalaireBonus();
    } else {
      System.out.println("Le nombre maximum de managers est atteint.");
    }
  }

  public void retirerManager(Manager manager) {
    if (this.managers.contains(manager)) {
      this.managers.remove(manager);
      manager.setSecretaire(null);
      recalculerSalaireBonus();
    } else {
      System.out.println("Le manager n'est pas associé à cette secrétaire.");
    }
  }

  public String toString() {
    return super.toString() + " Il est secrétaire.";
  }
}