package classes;
public class Adresse {
  private String rue;
  private String ville;
  private int codePostal;
  
  public Adresse(String rue, String ville, int codePostal) {
    this.rue = rue;
    this.ville = ville;
    this.codePostal = codePostal;
  }
  
  public Adresse() {
    this("", "", 0);
  }
  
  public void setRue(String rue) {
    this.rue = rue;
  }
  
  public void setVille(String ville) {
    this.ville = ville;
  }
  
  public void setCodePostal(int codePostal) {
    this.codePostal = codePostal;
  }
  
  public void afficher() {
    System.out.println("Rue : " + this.rue + "\nVille : " + this.ville + "\nCode postal : " + this.codePostal);
  }
  
  public String toString() {
    return this.rue + ", " + this.codePostal + " " + this.ville;
  }
}
