/*
 * Ce programme permet de mesurer le temps que met un condensateur à se charger.
 * 
 * Le système doit être branché comme suit.
 * 
 * 
 *    (pin 8) --- [ R ] ------- (pin A0)
 *                         |
 *                         = C
 *                         |
 *                     (pin GND)
 *                     
 * La pin 8 fournit la tension d'alimentation (0 ou 5 V).
 * La pin A0 sert à la mesure de la tension.
 *  
 * Le programme effectue plusieurs cycles de charges, et mesure le temps que met la tension aux bornes du condensateur pour atteindre une valeur seuil.
 *  
 * Attention, ce programme fonctionne à 115200 baud, à régler sur l'affichage moniteur ou plotteur.
 */

float const pauseEntreLesMesures = 0.; // Nombre de millisecondes entre chaque mesure de la tension.
int const pauseEntreCycles = 500; // Nombre de millisecondes entre chaque cycle de mesure.

float const seuil = 0.95; // Seuil de charge/decharge a partir duquel on considere la charge terminee.

int const nombreDeCyclesDeMesure = 10; // Nombre de cycles de mesure à faire pour moyenner.

int tension; // Variable qui stocke la tension sous forme d'un entier codé sur 10 bits (0 V = 0, 5 V = 1023).

unsigned long t0; // Variable qui stocke le temps au debt d'une sequence de mesure.
float tempsDeCharge[nombreDeCyclesDeMesure]; // Les temps de charge pour chaque cycle

void setup() {
  pinMode(8, OUTPUT); // alimentation du condensateur
  Serial.begin(115200);
  
  // DECHARGE INITIALE DU CONDENSATEUR
  digitalWrite(8,LOW); // La tension aux bornes du condensateur est mise a 0
  
  tension = 1023;
  while (tension > 0.5 * 1023 ) { 
    tension = analogRead(A0);
    delay(10);
  }

}

void loop() {

  // *** MESURE DES TEMPS DE CHARGE / DECHARGE ***
  
  for (int i_mesure = 0 ; i_mesure < nombreDeCyclesDeMesure ; i_mesure += 1) {

    delay(pauseEntreCycles);
  
    Serial.print("Cycle ");
    Serial.print(i_mesure+1);
    Serial.println(" :");
    
    // CHARGE
    digitalWrite(8,HIGH); // La tension aux bornes du condensateur est mise a 5 V
    t0 = micros();
    
    while (1) {
      tension = analogRead(A0);
      if (tension > seuil*1023) {
        tempsDeCharge[i_mesure] = (float)((micros() - t0))/1000;
        break;
      }
      delay(pauseEntreLesMesures);
    }
    Serial.print("Temps de charge : ");
    Serial.print(tempsDeCharge[i_mesure],3);
    Serial.println(" ms");
    
    // DECHARGE
    digitalWrite(8,LOW); // La tension aux bornes du condensateur est mise a 0
  
  tension = 1023;
  while (tension > 0.5 * 1023 ) { 
    tension = analogRead(A0);
    delay(10);
  }
    
  }

  Serial.println();

  // *** AFFICHAGE DES RESULTATS ***

  Serial.print("Sur ");
  Serial.print(nombreDeCyclesDeMesure);
  Serial.println(" cycles :");
  
  // Calcul temps moyen de charge
  float tempsDeChargeMoyen = 0;
  for (int i=0 ; i < nombreDeCyclesDeMesure ; i += 1) {
    tempsDeChargeMoyen += tempsDeCharge[i];
  }
  tempsDeChargeMoyen = tempsDeChargeMoyen / nombreDeCyclesDeMesure;
  Serial.print("Temps de charge moyen : ");
  Serial.print(tempsDeChargeMoyen,3);
  Serial.println(" ms");

  // Fin du programme, on ne fait plus rien
  while (1) {
    delay(10000);
  }
}
