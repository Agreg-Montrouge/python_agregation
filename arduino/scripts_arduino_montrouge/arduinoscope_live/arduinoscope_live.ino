/*
 * Ce programme utilise l'arduino comme oscilloscope, le but est d'afficher en direct des valeurs de temps et de tension pour ensuite les analyser à l'aide d'un programme python.
 * 
 * Une source de tension alternative doit etre branchée entre la pin GND (à la masse) et la pin A0 (où la mesure est faite).
 * 
 * Attention, il faut envoyer à l'arduino une tension POSITIVE en 0 et 5 V, sinon on risque de l'abimer.
 * 
 * Pour enregistrer les mesures : 
 * 
 *  - Uploader le programme
 *  - Afficher le moniteur (Crtl+Shift+M)
 *  - Effacer la sortie (clear output)
 *  - Appuyer sur le bouton RESET sur l'arduino pour relancer le programme
 *  - Sélectionner toutes les données (Crtl+A), les copier et les coller dans un fichier texte.
 *  
 * Attention, ce programme fonctionne à 614400 baud, à régler sur l'affichage moniteur ou plotteur.
 */

const int pinRead = A0;

int const nombreDeValeurs = 10000; // Nombre de valeurs à afficher à l'écran

void setup() {
  Serial.begin(614400);
}


void loop() {

  // On écrit toutes les valeurs, le plus vite possible.
  for (int i = 0 ; i < nombreDeValeurs ; i += 1) {
    Serial.print(micros());
    Serial.print("\t");
    Serial.println(analogRead(pinRead));
  }

  // Le programme est terminé, on attend.
  while(1) {
    delay(1000);
  }
  
}
