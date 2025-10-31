#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    int pass = 0;
    
    printf("\nEnter the password: \n");
    
    // Use fgets() instead - safe with bounds checking
    if (fgets(buff, sizeof(buff), stdin) == NULL) {
        printf("Error reading input\n");
        return 1;
    }
    
    // Remove trailing newline if present
    buff[strcspn(buff, "\n")] = '\0';
    
    if(strcmp(buff, "thecorrectpaswd") == 0) {
        printf("\nCorrect Password\n");
        pass = 1;
    } else {
        printf("\nWrong Password\n");
    }
    
    if(pass) {
        printf("\nRoot privileges given to the user\n");
    }
    
    return 0;
}