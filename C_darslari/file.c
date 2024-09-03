#include <stdio.h>
int main()
{
    FILE *fp;
    fp=fopen("newfile","w");
    fprintf(fp,"Salom qalaysila");
    fprintf(fp,"Ishlar qalay\n");
    int son=123;
    float pi=3.1415;
    char sym='#';
    fprintf(fp,"son=%d\tpi=%f\tsym=%c\n",son,pi,sym);
    fclose(fp);
    return 0;
}