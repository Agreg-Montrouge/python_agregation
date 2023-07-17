/*
 * Ce programme utilise l'arduino comme oscilloscope, le but est d'enregistrer des valeurs de temps et de tension pour ensuite les afficher a l'aide d'un programme python.
 * 
 * Une source de tension alternative doit etre branchée entre la pin GND (à la masse) et la pin A0 (où la mesure est faite).
 * 
 * Attention, il faut envoyer à l'arduino une tension POSITIVE en 0 et 5 V, sinon on risque de l'abimer./
 * 
 * Pour enregistrer les mesures : 
 * 
 *  - Uploader le programme
 *  - Afficher le moniteur (Crtl+Shift+M)
 *  - Effacer la sortie (clear output)
 *  - Appuyer sur le bouton RESET sur l'arduino pour relancer le programme
 *  - Sélectionner toutes les données (Crtl+A), les copier et les coller dans un fichier texte.
 *  
 * Attention, ce programme fonctionne à 115200 baud, à régler sur l'affichage moniteur ou plotteur.
 */

const int pinRead = A0;

int const nombreDeValeurs = 250; // Taille du buffer a garder en memoire. On est limités par la mémoire ridicule de l'arduino.

unsigned long temps[nombreDeValeurs]; // Les temps de mesure
int tension[nombreDeValeurs]; // Les tensions mesurees

void setup() {
}


void loop() {

  // D'abord on enregistre toutes les valeurs, le plus vite possible
  for (int i = 0 ; i < nombreDeValeurs ; i += 1) {
    temps[i] = micros();
    tension[i] = analogRead(pinRead);
  }

  // On communique toutes les valeurs à l'ordinateur
  Serial.begin(115200);
  for (int i = 0 ; i < nombreDeValeurs ; i += 1) {
    Serial.print(temps[i]);
    Serial.print("\t");
    Serial.print(tension[i]);
    Serial.println();
  }

  // Le programme est terminé, on attend.
  while(1) {
    delay(1000);
  }
  
}
