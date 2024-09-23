package classes;

/**
 * La classe Personne représente une personne avec un nom, un prénom, un âge et une adresse.
 */
public class Personne {
  
  // Attributs ou variables d'instances
  private String nom;
  private String prenom;
  private int age;
  private Adresse adresse;
  private static int nbPersonnes = 0;

  /**
   * Constructeur de la classe Personne.
   * 
   * @param nom Le nom de la personne.
   * @param prenom Le prénom de la personne.
   * @param age L'âge de la personne.
   * @param adresse L'adresse de la personne.
   */
  public Personne(String nom, String prenom, int age, Adresse adresse) {
    this.nom = nom;
    this.age = age;
    this.prenom = prenom;
    this.adresse = adresse;
    nbPersonnes++;
  }
  
  /**
   * Constructeur par défaut de la classe Personne.
   */
  public Personne() {
    this("", "", 0, new Adresse());
  }

  /**
   * Obtient le nombre total de personnes créées.
   * 
   * @return Le nombre total de personnes.
   */
  public static int getNbPersonnes() {
    return nbPersonnes;
  }

  /**
   * Compare l'âge de cette personne avec une autre personne.
   * 
   * @param p La personne à comparer.
   * @return La personne la plus âgée.
   */
  public Personne plusAgeeQue(Personne p) {
    if (this.age > p.age) {
      return this;
    } else {
      return p;
    }
  }

  /**
   * Compare l'âge de deux personnes.
   * 
   * @param p1 La première personne.
   * @param p2 La deuxième personne.
   * @return La personne la plus âgée.
   */
  public static Personne plusAgee(Personne p1, Personne p2) {
    if (p1.age > p2.age) {
      return p1;
    } else {
      return p2;
    }
  }

  /**
   * Vérifie si deux personnes sont égales.
   * 
   * @param p1 La première personne.
   * @param p2 La deuxième personne.
   * @return true si les personnes sont égales, false sinon.
   */
  public static boolean personneEqual(Personne p1, Personne p2) {
    return p1.nom.equals(p2.nom) && p1.prenom.equals(p2.prenom) && p1.age == p2.age;
  }

  /**
   * Affiche les informations de la personne.
   */
  public void afficher() {
    System.out.println("Nom : " + this.nom + "\nPrénom : " + this.prenom + "\nAge : " + this.age + "\nAdresse : " + this.adresse);
  }

  /**
   * Retourne une représentation sous forme de chaîne de caractères de la personne.
   * 
   * @return Une chaîne de caractères représentant la personne.
   */
  public String toString() {
    return this.nom + " (" + this.age + " ans)";
  }

  /**
   * Obtient le prénom de la personne.
   * 
   * @return Le prénom de la personne.
   */
  public String getPrenom() {
    return this.prenom;
  }

  /**
   * Obtient le nom de la personne.
   * 
   * @return Le nom de la personne.
   */
  public String getNom() {
    return this.nom;
  }

  /**
   * Obtient l'âge de la personne.
   * 
   * @return L'âge de la personne.
   */
  public int getAge() {
    return this.age;
  }

  /**
   * Obtient l'adresse de la personne.
   * 
   * @return L'adresse de la personne.
   */
  public Adresse getAdresse() {
    return this.adresse;
  }

  /**
   * Définit le nom de la personne.
   * 
   * @param nom Le nom de la personne.
   */
  public void setNom(String nom) {
    this.nom = nom;
  }

  /**
   * Définit l'âge de la personne.
   * 
   * @param age L'âge de la personne.
   */
  public void setAge(int age) {
    this.age = age;
  }
}