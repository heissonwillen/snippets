#include "stdio.h"

int main(){
  float nota_1, nota_2, nota_3, media;

  printf("Digite a primeira nota: ");
  scanf("%f", &nota_1);
  printf("Digite a segunda nota: ");
  scanf("%f", &nota_1);
  printf("Digite a terceira nota: ");
  scanf("%f", &nota_1);

  media = (nota_1+nota_2+nota_3)/3;

  if (media >= 7){
    printf("O aluno foi aprovado :) \n");
  } else {
    printf("O aluno foi reprovado :( \n");
  }

  return 0;
}
