// This example shows the 3 axis acceleration.
#include "LIS3DHTR.h" // La bibliotheque du capteur
#include <Wire.h>
LIS3DHTR<TwoWire> LIS; // Protocole IIC (Inter_Integrated Circuits)
#define WIRE Wire

// Le délimiteur pour les données enregistrées
//#define SPACER " ; "
#define SPACER "\t"

/////////////////////////////// ATTENTION, CE CAPTEUR FONCTIONNE SUR 3.3 V ///////////////////////////////////

/////////////////////////////// ATTENTION, CE PROGRAMME TRAVAILLE A 115200 baud ///////////////////////////////////

/* 
Ce programme renvoie les accelerations lues par le capteur.

Brancher ce capteur sur une sortie I2C.

Attention, ce programme necessite l'installation de la librairie LIS3DHTR. 
Pour l'installer : Sketch -> Include Library -> Add .ZIP Library -> sélectionner le fichier "Seeed_Arduino_LIS3DHTR-master.zip" dans le dossier "bibliotheques"

Utiliser Crtl+Maj+L pour afficher le graphe.
Utiliser Crtl+Maj+M pour afficher le moniteur.

MODE VISUALISATION
 - Mettre la variable mode_enregistrement à false
 - Mettre la variable show_x (resp. y, z) à true/false pour afficher/cacher l'acceleration selon x (resp. y, z)
 - Téléverser le programme
 - Afficher le graphe (Crtl + Maj + L)
 - Verifier que le débit est correct (115200 baud)

MODE ENREGISTREMENT
Pour utiliser le mode enregistrement : 
 - Mettre la variable mode_enregistrement à true
 - Choisir la valeur de T_enregistrement, le temps d'enregistrement en ms
 - Téléverser le programme
 - Afficher le moniteur (Crtl + Maj + M)
 - Verifier que le débit est correct (115200 baud)

Pour lancer un enregistrement
 - Appuyer sur le bouton 'reset' et cliquer vite sur 'Effacer la sortie'
 - Attendre le temps d'enregistrement
 - Sélectionner tout (Crtl + A) et copier (Crtl + C)
 - Coller dans un fichier texte
 - Enjoy

Le temps est affiché en ms, les accelerations en g / 100.
*/

bool mode_enregistrement = true; // Mettre true pour enregistrer, false pour juste afficher
float T_enregistrement = 10000; // La duree d'enregistrement (en ms)

bool show_x = true;
bool show_y = true;
bool show_z = true;

float t = 0; // Le temps en ms
float acc_x = 0; // L' acceleration selon x
float acc_y = 0; // L' acceleration selon y
float acc_z = 0; // L' acceleration selon z

void setup() {
    Serial.begin(115200); // Travail a 115200 baud
    while (!Serial) {}; // Attendre l'initialisation de la liaison avec l'ordi
    LIS.begin(WIRE, 0x19); //Initier la liaison IIC (entre le capteur et la carte)
    delay(100);
      LIS.setFullScaleRange(LIS3DHTR_RANGE_2G); // le plus petit range pour plus de precision
    //  LIS.setFullScaleRange(LIS3DHTR_RANGE_4G);
    //  LIS.setFullScaleRange(LIS3DHTR_RANGE_8G);
    //  LIS.setFullScaleRange(LIS3DHTR_RANGE_16G);
    
    //  LIS.setOutputDataRate(LIS3DHTR_DATARATE_1HZ);
    //  LIS.setOutputDataRate(LIS3DHTR_DATARATE_10HZ);
    //  LIS.setOutputDataRate(LIS3DHTR_DATARATE_25HZ);
    // LIS.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);
//      LIS.setOutputDataRate(LIS3DHTR_DATARATE_100HZ);
      LIS.setOutputDataRate(LIS3DHTR_DATARATE_200HZ); // Frequence d'aquisition adaptee a la frequence d'affichage
//      LIS.setOutputDataRate(LIS3DHTR_DATARATE_1_6KHZ);
//      LIS.setOutputDataRate(LIS3DHTR_DATARATE_5KHZ);
    LIS.setHighSolution(true); //High solution enable

    if (mode_enregistrement) { 
      Serial.print("t"); Serial.print(SPACER); 
      Serial.print("acc_x"); Serial.print(SPACER);
      Serial.print("acc_y"); Serial.print(SPACER);
      Serial.print("acc_z"); Serial.print(SPACER);
      Serial.println();
    }
}

void loop() {
    if (!LIS) {
        Serial.println("LIS3DHTR didn't connect.");
        while (1);
        return;
    }
    
    //Choper les données 
    acc_x = LIS.getAccelerationX() * 100;
    acc_y = LIS.getAccelerationY() * 100;
    acc_z = LIS.getAccelerationZ() * 100;
    
    // Afficher les données
    if (mode_enregistrement) { 
      Serial.print( millis() ); Serial.print(SPACER); 
      Serial.print( acc_x ); Serial.print(SPACER);
      Serial.print( acc_y ); Serial.print(SPACER);
      Serial.print( acc_z ); Serial.print(SPACER);
      Serial.println();
    } else {
      if (show_x) {Serial.print("x:"); Serial.print(   acc_x   ); Serial.print(" ");}
      if (show_y) {Serial.print("y:"); Serial.print(   acc_y   ); Serial.print(" ");}
      if (show_z) {Serial.print("z:"); Serial.print(   acc_z   ); Serial.print(" ");}
      Serial.println(); // Passer a la ligne
    }

    t += 10;
    delay(10);

    if (mode_enregistrement and (t > T_enregistrement)) {
      while (true) { delay(1000); } // attendre jusque la fin des temps
    }
}
