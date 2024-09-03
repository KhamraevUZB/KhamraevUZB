#include <stdio.h>

int main() {
    int number, temp, digit;
    int digits[10]; // O'nliklik sonlar uchun massiv
    int count = 0;

    printf("Istalgan honali son kiriting: ");
    scanf("%d", &number);

    printf("Soni raqamlari: ");

    if (number == 0) {
        printf("0");
    } else {
        temp = number;
        do {
            digit = temp % 10;
            digits[count] = digit;
            count++;
            temp /= 10;
        } while (temp != 0);

        while (count > 0) {
            count--;
            printf("%d ", digits[count]);
        }
    }

    return 0;
}
// #include <stdio.h>
// #include <math.h>

// int main () {

//     int son = 1020;
//     int xona = 4;
//     while (son > 9) {
//         int number = son / pow(10, xona - 1);
//         son = son % (int)(pow(10, xona - 1));
//         xona = xona - 1;
        
//         printf("%d\n", number);
//     }

//     int birlik = son % 10;
//     son = son / 10;

//     printf("%d\n", birlik);
    
//     for (int i = 1; i < xona; i++) {
//         printf("0\n");
//     }
    
//     return 0;
// }
