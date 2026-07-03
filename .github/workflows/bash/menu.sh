#!/bin/bash
# Menu interactif pour l'administration systeme

choix=0

# Boucle : le menu reste actif tant que l'utilisateur n'a pas choisi 4 (quitter)
while [ "$choix" != "4" ]
do
    echo ""
    echo "===== MENU ====="
    echo "1) Afficher la date et l'heure du systeme"
    echo "2) Afficher les utilisateurs connectes"
    echo "3) Afficher l'espace disque disponible"
    echo "4) Quitter"
    echo "================"
    read -p "Votre choix : " choix

    case $choix in
        1)
            date
            ;;
        2)
            who
            ;;
        3)
            df -h
            ;;
        4)
            echo "Au revoir !"
            ;;
        *)
            echo "Choix invalide, recommencez."
            ;;
    esac
done
