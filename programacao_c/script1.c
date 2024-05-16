#include <stdio.h>

int main()
{
    int matrix[3][4], line, colu, npar=0, nimpar=0;
    printf("\nDigite o valor para os elementos da matriz\n\n");
    for (line=0; line<3; line++) {
        for (colu=0; colu<4; colu++) {
            printf("\nElementos[%d][%d] = ", line, colu);
            scanf("%d", &matrix[line][colu]);
        }
    }
    printf("\n\n******************** Saída de dados ******************** \n\n");
    for (line=0; line<3; line++) {
        for (colu=0; colu<4; colu++) {
            if (matrix[line][colu]%2==0) {
                npar++;
            } else {
                nimpar++;
            }
        }
    }
    printf("\nPares: %d ", npar);
    printf("\nImpares: %d ", nimpar);
    return(0);
}
