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