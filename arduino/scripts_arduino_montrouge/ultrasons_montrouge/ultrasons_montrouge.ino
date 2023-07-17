/*
 * Ce programme permet de mesurer la distance du telemetre a la surface reflechissante la plus proche de lui
 * 
 * Le telemetre doit etre branche sur la sortie D4 du shield Grove.
 * 
 * La communication se fait a l'aide d'une pin, celle de signal (pinSig).
 * 
 * Le signal de commande est un creneau TTL de 5 V (HIGH) durant 10 us.
 * 
 * En reponse, le telemetre renvoie 0 V pendant sa preparation, puis impose 5 V (HIGH) tant que le pulse est en l'air et retombe à 0 V (LOW) quand il revient.
 * 
 * Exemple de la tension sur pinSig pendant une sequence de mesure :
 *  
 *  
 *      ^                    
 * HIGH_|    _________        _________________________________
 *      |   |         |      |                                 |
 *  LOW_|___|         |______|                                 |_____
 *          <--10 us-->      <-------duree_microsecondes------->
 *          (signal de       ^                                 ^
 *            commande)   (envoi                          (reception 
 *                         du burst)                        du burst)
 * 
 * 
 * Le pulse consiste en 8 oscillations a 40 kHz.
 *  
 * Attention, ce programme fonctionne à 115200 baud, à régler sur l'affichage moniteur (Crtl+Shift+M).
 */

float const pauseEntreLesMesures = 1000; // Nombre de millisecondes entre chaque mesure de la distance.

int const pinSig = 4;  // Brancher le capteur ultrason sur l'épingle D4

double const c = 343.0; // Vitesse du son (m/s)

void setup()
{
Serial.begin(115200);
}

void loop()
{
  
  long duree_microsecondes;
  duree_microsecondes = mesurerUnTempsDeTrajet();
  
  double duree_millisecondes;
  duree_millisecondes = ( (double) duree_microsecondes ) / 1000;

  Serial.print("Temps d'aller_retour : ");
  Serial.print(duree_millisecondes, 3);
  Serial.println(" ms");

  
  double distance_mm;
  distance_mm = duree_millisecondes * c / 2;
  
  Serial.print("Distance : ");
  Serial.print(distance_mm, 2);
  Serial.println(" mm");
  
  Serial.println();

  delay(pauseEntreLesMesures);
}


/*
 * Cette fonction fait une mesure de temps de trajet aller-retour d'un burst d'ultrasons à 40 kHz.
 * 
 * Elle renvoie le temps écoulé entre l'envoi du burst et sa reception, en microsecondes.
 */
long mesurerUnTempsDeTrajet() {

    // Tout d'abord, il faut envoyer un signal au telemetre pour lui dire de lancer le protocole de mesure.
    // On commence a mettre le pin en mode OUTPUT et on impose une tension nulle.
    pinMode(pinSig, OUTPUT);
    digitalWrite(pinSig, LOW);
    delayMicroseconds(5); 
    // Le signal d'envoi est un creneau de 5 V pendant 10 us.
    digitalWrite(pinSig, HIGH); 
    delayMicroseconds(10); 
    digitalWrite(pinSig, LOW);
    // Ensuitew on ecoute la reponse du telemetre
    pinMode(pinSig, INPUT);

  
    long timeout = 1000000L; // Le delai maximum sans qu'il ne se passe rien est 1 s. Si ce temps est depassé sans mesure de signal, on renvoie 0 pour dire qu'une erreur s'est produite.
  
    long debut_sequence = micros();

    // wait for any previous pulse to end
    while (digitalRead(pinSig) == HIGH) {
      if ((micros() - debut_sequence) >= timeout) { return 0; } // Si le timeout est depassé, retourne 0
    }

    // wait for the pulse to start
    while (digitalRead(pinSig) == LOW) {
      if ((micros() - debut_sequence) >= timeout) { return 0; } // Si le timeout est depassé, retourne 0
    }
    
    long pulseBegin = micros(); // Date d'envoi du burst

    // wait for the pulse to stop
    while (digitalRead(pinSig) == HIGH) {
      if ((micros() - debut_sequence) >= timeout) { return 0; } // Si le timeout est depassé, retourne 0
    }
         
    long pulseEnd = micros(); // Date de reception du burst

    return pulseEnd - pulseBegin;
}
