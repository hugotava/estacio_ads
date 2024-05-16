// Faça um algoritmo que leia uma matriz 4x4 de números inteiros.
// Gere uma segunda matriz (matriz 2), na qual as linhas são as colunas da matriz 1, e as colunas são as linhas da matriz 1.

#include <stdio.h>

int main() {

    int matriz1[4][4],matriz2[4][4],line,colu;
    printf ("\n Digite a matriz original \n");

    for (line=0;line<4;line++)

        for (colu=0;colu<4;colu++) {
            scanf ("%d",&matriz1
    [line][colu]);
            matriz2[colu][line]=matriz1
    [line][colu];
        }

    printf ("\n Matriz gerada \n");

    for (line=0;line<4;line++) {
        for (colu=0;colu<4;colu++)
        printf ("%d ",matriz2[line][colu]);
        printf ("\n");
    }
}