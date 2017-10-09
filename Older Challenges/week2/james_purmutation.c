// James Clinton
// is x a purmutation of y

// Compare the values of the two characters
// to be used by qsort
int compare(const void *a, const void *b){
	
    return *(const char *)a - *(const char *)b;
	
}

// Main Method
int main (){
	
	// Place to store the two arrays
	char x[100];
	char y[100];
	
	// Get the input of the two arrays
	printf("enter a string: ");
	scanf("%s", x);
	printf("enter another string: ");
	scanf("%s", y);
	
	// If the arrays are not the same length return they are not purmutations
	if(strlen(x) != strlen(y)){
		printf("X is not a Purmutation of Y");
		return 0;
	}
	
	// Sort the arrays
	qsort(x, strlen(x), 1, compare);
	qsort(y, strlen(y), 1, compare);
	
	// Compare the arrays
	int i;
	for(i = 0; i < strlen(x); i++){
		if(x[i] != y[i]){
			printf("X is not a Purmutation of Y");
			return 0;
		}
	}
	
	// Return true
	printf("X is a Purmutation of Y");
	return 0;

}
