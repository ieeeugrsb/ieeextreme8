#!/bin/bash
#####################################
# Script para ejecutar programas de #
#           IEEEXtreme 8.0          #
#               v1.0                #
#            by pleonex             #
#####################################

# Ejecuta el comando
while IFS= read -r line
do
    lines[i]="$line"
    ((i++))
done < <(/usr/bin/time -f "%E\n%M\n" "$@" 2>&1)

# Obtiene los datos
num=${#lines[@]}
t=${lines[$((num - 3))]}
m=${lines[$((num - 2))]}

# Muestra los tiempos
echo "----------------"
echo "Tiempo:  $t"
echo "Memoria: $m KB"
echo "----------------"
echo "Salida:"
echo "----------------"

# Muestra la salida del comando
for (( i=0; i < $((num - 3)); i++))
do
    echo "${lines[$i]}"
done
