# Faciliter l'accès au HPC pour les utilisateur·trice·s non spécialistes (Hackademia, UNIGE)

<p align="center">
    <a href="https://www.youtube.com/watch?v=wlp9px83dVA">
    <img src="https://edutechwiki.unige.ch/fmediawiki/images/1/1e/Hackademia_2024_vf.png" alt="Hackademia quote" width="500">
    </a>
</p>

22-23 novembre 2025 à l'UNIGE (https://www.unige.ch/hackademia/)

# Contexte

HPC: **High Performance Computing - Calculs Haute Performance**

3 Clusters (Baobab - Yggdrasil - Bamboo)

- environ 500 serveurs
- 27 968 coeurs 
- 134.86 To RAM
- 3,5 PB stockage
- 391 cartes gpu (RTX/GTX/A100 etc...)
- slurm: scheduler de jobs/ressource fairuse

Permet de booster la recherche en mettant en commun les ressources de calcul

## Problématiques

- Des utilisateur·trice·s en perdition devant un terminal linux avec un projet à rendre pour hier.

- "Je dois allouer combien de CPU ? Combien de RAM ? Combien de GPU ? Distribué ou  Multithreading (ou pas) ? Comment on fait pour se connecter?" 🤯 ➡️ **Read The Fucking Manual ❤️**

## Ce que nous avons

- Interface web user friendly [openondemand.baobab.hpc.unige.ch]https://openondemand.baobab.hpc.unige.ch) qui permet de lancer des jobs interactifs (JupyterLab, Vscode Server, Stata, MatLab etc...) sur des noeuds de calcul dédiés.

## Ce que nous voulons

- Même avec une interface web, les users sont souvent déconcertés. 

- Nous allons donc aider Jean-Phi et Josianne à lancer un job avec un minimum de clic.

- Déployer un outil pour générer des apps non interactive  à partir d'un fichier de config yaml qui peut être maintenu par un utilisateur plus confirmé, le tout intégrer dans notre interface OpenOnDemand.

# Dev

➡️ Suivre les README.md sous chaque directory

## Tree

`````
.
├── README.md
├── .gitlab-ci.yml //CI utilisant un runner GitLab
└── sources
    ├── README.md
    ├── config //dir contenant les fichiers de configuration du/de la mainteneur·e
    │   ├── config_example.yml //suivre les instructions dans le config_example.yml et renommer en config.yml
    └── script //dir contenant les scripts python pour transformer le config.yml en quatre yml et erb files sous templates
        ├── README.md
        ├── __init__.py
        ├── generate_app.py
        ├── generate_form.py
        ├── generate_manifest.py
        ├── generate_script.py
        ├── generate_submit.py
        ├── requirements.txt
        └── templates //outputs de generate_app.py
            ├── form.yml
            ├── manifest.yml
            ├── script.sh.erb
            └── submit.yml.erb
`````

# To-do list

- [X] Session non interactive
- [X] Exec  container via une SNI
- [X] Définition yaml config
- [X] Générer  fichiers de form/manifest/submit etc..pour SNI
- [ ] Générer submit.yml.erb script.sh
- [ ] intégration continue gitlab (+ container registry) etc...