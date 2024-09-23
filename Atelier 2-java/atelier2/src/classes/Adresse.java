package classes;

/**
 * La classe Adresse représente une adresse avec une rue, une ville et un code postal.
 */
public class Adresse {
  private String rue;
  private String ville;
  private int codePostal;

  /**
   * Constructeur de la classe Adresse.
   * 
   * @param rue La rue de l'adresse.
   * @param ville La ville de l'adresse.
   * @param codePostal Le code postal de l'adresse.
   */
  public Adresse(String rue, String ville, int codePostal) {
    this.rue = rue;
    this.ville = ville;
    this.codePostal = codePostal;
  }

  /**
   * Constructeur par défaut de la classe Adresse.
   */
  public Adresse() {
    this("", "", 0);
  }

  /**
   * Définit la rue de l'adresse.
   * 
   * @param rue La rue de l'adresse.
   */
  public void setRue(String rue) {
    this.rue = rue;
  }

  /**
   * Définit la ville de l'adresse.
   * 
   * @param ville La ville de l'adresse.
   */
  public void setVille(String ville) {
    this.ville = ville;
  }

  /**
   * Définit le code postal de l'adresse.
   * 
   * @param codePostal Le code postal de l'adresse.
   */
  public void setCodePostal(int codePostal) {
    this.codePostal = codePostal;
  }

  /**
   * Affiche les informations de l'adresse.
   */
  public void afficher() {
    System.out.println("Rue : " + this.rue + "\nVille : " + this.ville + "\nCode postal : " + this.codePostal);
  }

  /**
   * Retourne une représentation sous forme de chaîne de caractères de l'adresse.
   * 
   * @return Une chaîne de caractères représentant l'adresse.
   */
  public String toString() {
    return this.rue + ", " + this.codePostal + " " + this.ville;
  }
}