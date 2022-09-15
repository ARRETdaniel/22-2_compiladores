//Trabalho de DANIEL TERRA

%{
#include <stdio.h>
#include <stdlib.h>
%}
dgt		[0-9]
%%
{dgt}+  return atoi(yytext);
%%
void main()
{
	int val, total = 0, n;

	while( (val = yylex()) > 0){
		total += val;
		n++;
	}

   printf("media = %d\n",total/n);
    
}
