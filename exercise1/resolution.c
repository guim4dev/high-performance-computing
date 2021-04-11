#include <stdio.h>
#include <stdlib.h>
#define BASE_LEN 50

void getUserIntInput(char *str, int *reference) {
	char input[BASE_LEN] = "";
	char *endptr = NULL;
	printf("%s\n", str);
    fgets(input, BASE_LEN, stdin);
    *reference = (int) strtol(input, &endptr, 10);
	printf("\n");
}

int main() {
    int number_of_rows = 0;
    getUserIntInput("Number of rows in the square matrix:", &number_of_rows);
    return 0;
}