==========================
Programmes pour les leçons
==========================

Liste des programmes disponibles
================================


Les programmes
==============

Voici quelques prescriptions sur l'écriture des programmes. On s'éfforcera d'utiliser
les recommentations de Python (PEP 8)

* Chaque programme commence par une chaine de documentation. Cette chaîne contient :

    * Un titre
    * Une description
    * Eventuellement un rappel des formules utilisées ou tout autre information utile (lien, ...)
    * D'autres informations (auteurs, licence, ....)

* Ensuite, l'ensembles des import. Si on souhaite avoir les bons paramètres par défaut pour
  la taille de la figure et le polices, il faut importer le module ``programmes_lecons``, 
  même si on n'utilise aucune de ces fonctions


Dans le suite, on s'efforcera de séparer le fond de la forme et de mettre le fond au début
du programme. Typiquement, un programme se sépare alors en 4 sections : 

* Les variables globales et le paramètres. Les paramètres sont des ``widget`` regroupés dans
  un dictionnaire. Les clés sont du dictionnaire seront les noms des variables. En général, 
  on recommande de donner des noms explicite pour une variable (par exemple ``resistance`` et
  non ``R``). Cette règle n'est pas indispensable si c'est le nom de la variale utilisée
  habituellement en physique (dans un circuit RLC, on sait que R est la résistance)
 
* Le modèle physique : toutes les fonctions utilisées. On utilisera toujours les unités SI (sans
  préfixe) ou les unités spécifiques au problèmes. 

* Le tracé des données : une fonction sera utilisée pour tracer les données en fonctions des
  paramètres. Les arguuments sont les noms des paramètres (les clés du dictionnaire). On
  effectuera les transformation en SI au début de la fonction. 

  Cette fonction changera les données des "lignes" des plots ::

     lines['nom_de_la_ligne'].set_data(x, y)

  Les variables x et y seront en SI sans préfixe. Si le graph à des préfix, on le mettra à ce
  moment là (``set_data(1E3*x, y)``)

* La création et la mise en page de la figure : création de la figure, des axes, des 'lignes'
  avec tous les paramètres de la mise en forme (couleur, style, ...); création des widgets et
  des autres boutons

* A la fin, le plt.show() est mis dans un ``if __name__=="__main__"`` : ceci permet d'importer
  le script comme une librairie sans afficher la figure pour faire des extractions automatiques


Création d'une animation
========================

Voir les exemples comme : ``propagation_onde``. 
