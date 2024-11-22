## Objectifs:
Améliorer l'accès au HPC pour les noobs

## Contexte
HPC: **High Performance Computing - Calculs hautes Performances**

3 Clusters (Baobab - Yggdrasil - Bamboo)

- environ 500 serveurs
- 27 968 coeurs 
- 134.86 To RAM
- 3,5 PB stockage
- 391 cartes gpu (RTX/GTX/A100 etc...)
- slurm: scheduler de jobs/ressource fairuse

Permets de booster la recherche en mettant en communs les ressources de Calculs

## Problématiques
Des Utilisateurs en perdition devant un terminal linux avec un projet à rendre pour hier.

Je dois allouer combien de CPU ? Combien de RAM ? Combien de GPU ? Distribué ou  Multithreading (ou pas) ? Comment on fait pour se connecter? 🤯

### **Read The Fucking Manual ❤️** 

## Ce que nous avons
Interface web user friendly [openondemand.baobab.hpc.unige.ch]https://openondemand.baobab.hpc.unige.ch) qui permet de lancer des jobs interactif (JupyterLab, Vscode Server, Stata, MatLab etc...) sur des noeuds de calcul dédiés.


## Ce que nous voulons
Même avec une interface web, les users sont souvent déconcertés. 

Nous allons donc aider Jean-Phi et Josianne à lancer un jobs  avec un minimum de clic.


Déployer un outil pour générer des apps non interactive  à partir d'un fichier de config yaml qui peut être maintenu par un utilisateur plus confirmé, le tout intégrer dans notre interface OpenOnDemand.


Tasks:

- [X] Session non interactive
- [X] Exec  container via une SNI
- [X] Définition yaml config
- [X] Générer  fichiers de form/manifest/submit etc..pour SNI
- [ ] Générer submit.yml.erb script.sh
- [ ] intégration continue gitlab (+ container registry) etc...
    




