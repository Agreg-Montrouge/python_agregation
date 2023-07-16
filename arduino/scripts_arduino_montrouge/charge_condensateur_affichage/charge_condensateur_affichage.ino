/*
 * Ce programme permet de mesurer la tension aux bornes du condensateur. au cours de sa charge.
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
 *  La pin 8 fournit la tension d'alimentation (0 ou 5 V).
 *  La pin A0 sert à la mesure de la tension.
 *  
 *  Le programme effectue plusieurs cycles de charges, où le condensateur est chargé jusqu'à ce que la tension à ses bornes atteigne une valeur seuil, puis déchargé.
 *  
 *  Attention, ce programme fonctionne à 115200 baud, à régler sur l'affichage moniteur (Crtl+Shift+M).
 */

float const pauseEntreLesMesures = 0.01; // Nombre de millisecondes entre chaque mesure de la tension.
int const pauseEntreCycles = 2000; // Nombre de millisecondes entre chaque cycle de mesure.

float const seuil = 0.95; // Seuil de charge/decharge a partir duquel on considere la charge terminee.

int tension; // Variable qui stocke la tension sous forme d'un entier codé sur 10 bits (0 V = 0, 5 V = 1023).

void setup() {
  pinMode(8, OUTPUT); // alimentation du condensateur
  Serial.begin(115200);
  
  // DECHARGE INITIALE DU CONDENSATEUR
  digitalWrite(8,LOW); // La tension aux bornes du condensateur est mise a 0
  
  tension = 1023;
  while (tension > 0.5 * 1023 ) 
  { 
    tension = analogRead(A0);
    delay(10);
  }

}

void loop() {

  delay(pauseEntreCycles);
  
  // CHARGE
  digitalWrite(8,HIGH); // La tension aux bornes du condensateur est mise a 5 V
  
  tension = 0;
  while (tension < seuil * 1023 ) 
  {
    tension = analogRead(A0);
    Serial.println(tension);
    
    delay(pauseEntreLesMesures);
  }
  
  
  // DECHARGE
  digitalWrite(8,LOW); // La tension aux bornes du condensateur est mise a 0
  
  tension = 1023;
  while (tension > 0.5 * 1023 ) 
  {
    tension = analogRead(A0);
    delay(10);
  }

}
