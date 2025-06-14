[TOC]
# Feedback 

## Contexte
Cette installation est une évaluation pour un projet de migration de [syncloud](https://syncloud.org/), solution opensource mais pas ouverte sur laquelle est hébergée 6 services sur une machine Odroid 32 bits.

* NextCloud
* Gogs
* bitwarden ( vault )
* synapse et élément matrix
* synthing
* calibre

### Objectif
Cet installation a pour but de tester la solution **yunohost** dans le but de
1. Passer en architecture 64 bit pour héberger l'application **photoprism**
2. m'ouvrir la possibilité de déployer des applications web sur le même matériel  

je choisi de faire ce travail sur un serveur sous Debian 11, la version Debian 12 n'étant pas disponible

### Hardware 
**Odroid HC4** 

 composant  | Spécifications  
 :---: | :-- 
Processeur| Amlogic S905X3 Processor 
 "|**L1 instruction cache** : 32 KB, 4-way set associative (128 sets), 64 byte lines, shared by 1 processor
 "| **L1 data cache**: 32 KB, 4-way set associative (128 sets), 64 byte lines, shared by 1 processor 
 "| **L3 data cache**: 512KB , 16-way set associative (512 sets), 64 byte lines, shared by 4 processors 
 "| **Quad-Core Cortex-A55 (1.800GHz)** 
 "| **ARMv8-A architecture** with Neon and Crypto extensions 
 "|**Mali-G31 MP2 GPU** with 4 x Execution Engines (650Mhz) 
 Mémoire| **DDR4 4GiB** with 32-bit bus width
"| **Data rate**: 2640 MT/s (PC4-21333 grade)
"| 1.2Volt low power design
Connecteur | **HDMI** 2.0
"| **1Gb Lan** 
Stockage | **2 x SATA** Connectors
" | **SSD** 250Go"
 
 ### Accès internet 
 
 Info| valeur
 :-:|:-
 Connection| **1 Gb** symétrique
 IP| **IP fixe**
 Domaine| pirboazo.xyz
 
 ### Système 
 
 Installation de Debian 11.8 par le réseau
 
## Installation Yunohost (core)
### systeme yunohost

L'installation en **CLI** par la commande c-dessous, c'est déroulé sans problème.

> curl https://install.yunohost.org | bash


### post installation
Ces opérations de post-installation ont été faites depuis l'interface web.

* Lancement de la configuration initiale
* lancement des diagnostics
* Examen de ceux-ci 
* modification **dns** ajout de l'enregistrement 
	* CAA   0 issue "letsencrypt.org"
	* suppression des sous-domaine devenus inutiles
* Lancement de la création du certificat **Letsencryp**	
	* OK 
* ignorer les modifications **dns** pour le mail
	
**NOTA :** A posteriori cette étape de configuation des dns Email est quasi obligatoire.	
	
	
## Installation des applications	

L'installation des applications est sans problème, j'ai donc installé :
* Photoprism 
* syncthing
* Nextcloud
* gitea
* calibre
* Vaultwarden

### Vue 
Administrateur finale
![](/home/pboizot/Pictures/yunohost/Ecran-admin-application.jpg)

Utilisateur finale 
![](/home/pboizot/Pictures/yunohost/Ecran-utilisateur.jpg)

### Bilan des installations d'applications
Je vais faire application par application quelques remarques et donner une note de satisfaction.

Application| Satisfaction | Remarques 
:-: | :-: | :-: 
Photoprism | *** | Version trop ancienne
syncthing | *****| la déconnection ne renvoie as sur la page de yunohost
Nextcloud | ***** | idem 
gitea | *** | test à finir migration gogs ne marche pas
calibre| *****| 
Vaultwarden | **** | Visiblement pas utilisable sans la gestion des emails  


## Conclusion
Après cette série de tests je pense qu'il m'est possible de basculer de **syncloud** vers **yunohost** si je résoud les problèmes 

1. **vaultwarden**.   
	1.Ouverture d'une demande de support sur le forum. 
1. **Photoprism**
	1. Lié au passage de yunohost en Debian 12 
	
Par ailleurs je n'installerai pas **synapse** ni le client élément

**Nota :** Reste à faire au 12 Janvier.

1. Mettre en route la gestion d'e-mail. Fait le 13/01 , il me reste un problème à traiter avec **Infomaniak**
1. Valider le bon fonctionnement de Vautlwarden
	1. accés distant OK
	1. migration des données OK
1. Installer une aplication web ( biblioteko )

Je ne migrerai pas le serveur **synapse** 

Je vais investir du temps, en participant à des tests  de yunohost sur Debian 12






