#!/bin/bash
# Script qui identifie le service correspondant a chaque port

# Le tableau contenant la liste des ports
ports=(22 25 80 443 3306 8080)

# On parcourt chaque port du tableau
for port in "${ports[@]}"
do
    # Selon la valeur du port, on affiche le service correspondant
    case $port in
        22)
            echo "Port $port : SSH"
            ;;
        80)
            echo "Port $port : HTTP"
            ;;
        443)
            echo "Port $port : HTTPS"
            ;;
        3306)
            echo "Port $port : MySQL"
            ;;
        *)
            echo "Port $port : Port inconnu"
            ;;
    esac
done
