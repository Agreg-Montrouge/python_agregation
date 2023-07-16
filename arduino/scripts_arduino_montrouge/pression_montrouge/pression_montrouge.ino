
/*
 * Ce programme permet de mesurer la pression, en mesurant la tension sur le pin A0.
 * 
 * Il faut utiliser le shield Grove, et brancher le capteur sur la 4-broche A0.
 * 
 * La variable "offset" peut être modifiée, par exemple en étalonnant le capteur à la pression ambiante.
 *  
 * Pour afficher un graphe continu : choisir intervalleEntreMesures court (de l'ordre de 10) et afficher le plotteur (Crtl+Shift+L).
 *  
 * Pour afficher des valeurs de pression : choisir intervalleEntreMesures long (de l'ordre de 1000) et afficher le moniteur (Crtl+Shift+M).
 *  
 * Attention, ce programme fonctionne à 115200 baud, à régler sur l'affichage moniteur (Crtl+Shift+M).
 */

///////////////////////////// ATTENTION, CE CAPTEUR FONCTIONNE EN 5 V /////////////////////////////
 
float const intervalleEntreMesures = 10; // Intervalle entre les mesures, en ms.

int const pin = A0;

double const sensibilite = 6.4; // Sensibilite du capteur : 6.4 mV / kPa
double const offset = 152; // Offset du capteur : normalement entre 88 et 313 mV

void setup() {
  Serial.begin(115200);
}

void loop() {
  // On lit la valeur de la tension (entier sur 1024 values) sur la pin A0.
  int rawValue = analogRead(pin);

  // On obtient la tension delivree (en mV)
  double rawVoltage;
  rawVoltage = (double) rawValue * 5000 / 1023;

  // On transforme la tension en pression
  double pression;
  pression = (rawVoltage - offset) / sensibilite;

  Serial.print("Pression (kPa) "); Serial.println(pression);
  delay(intervalleEntreMesures);
}
