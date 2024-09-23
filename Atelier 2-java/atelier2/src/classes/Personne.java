package classes;
public class Personne {
  
	//Attributs ou variables d'instances
	private String nom;
  private String prenom;
  private int age;
  private Adresse adresse;
  private static int nbPersonnes = 0;

  public Personne(String nom, String prenom, int age, Adresse adresse) {
    this.nom = nom;
    this.age = age;
    this.prenom = prenom;
    this.adresse = adresse;
    nbPersonnes++;
  }
  
  public Personne() {
    this("", "", 0, new Adresse());
  }

  // 1 Q1
  public static int getNbPersonnes() {
    return nbPersonnes;
  }

  // 3 Q1
  public Personne plusAgeeQue(Personne p) {
    if (this.age > p.age) {
      return this;
    } else {
      return p;
    }
  }

  // 2 Q1
  public static Personne plusAgee(Personne p1, Personne p2) {
    if (p1.age > p2.age) {
      return p1;
    } else {
      return p2;
    }
  }

  // 4 Q1
  public static boolean personneEqual(Personne p1, Personne p2) {
    return p1.nom.equals(p2.nom) && p1.prenom.equals(p2.prenom) && p1.age == p2.age;
  }

	public void afficher() {
		System.out.println("Nom : " + this.nom + "\nPrénom : " + this.prenom + "\nAge : " + this.age + "\nAdresse : " + this.adresse);
	}
	public String toString() {
		return this.nom + " (" + this.age + " ans)";
	}

  public String getPrenom() {
    return this.prenom;
  }
  public String getNom() {
    return this.nom;
  }
  public int getAge() {
    return this.age;
  }
  public Adresse getAdresse() {
    return this.adresse;
  }
  public void setNom(String nom) {
		this.nom=nom;
	}
	public void setAge(int age) {
		this.age=age;
	}

}
