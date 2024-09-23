package classes;
public class Manager extends Employe{
  private Secretaire secretaire;
  public double BONUS_SALAIRE_PAR_AN_POURCENTAGE = 0.5;

  public Manager(Employe employe) {
    super(employe.getPersonne(), employe.getSalaire(), employe.getDateEmbauche());
    this.ajouterSalaireBonus();
  }

  private void ajouterSalaireBonus() {
    int nbAnnees = this.calculAnnuite();
    this.augmenterLeSalaire(BONUS_SALAIRE_PAR_AN_POURCENTAGE * nbAnnees);
  }

  public void setSecretaire(Secretaire secretaire) {
    this.secretaire = secretaire;
  }

  public Secretaire getSecretaire() {
    return this.secretaire;
  }

  public String toString() {
    return super.toString() + " Il est manager.";
  }
}
