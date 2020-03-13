#include <cstdio>

int answer[11] = {1, 1, 2, };
int check = 2;

int solve(int n){
	if(n <= check){
		return answer[n];
	}
	while(check < n){
		answer[check+1] = answer[check-2]+answer[check-1]+answer[check];
		check += 1;
	}
	return answer[n];
}

int main(void){
	int T, n;
	scanf("%d", &T);
	getchar();
	for(int i=0;i<T;i++){
		scanf("%d", &n);
		getchar();
		printf("%d\n", solve(n));
	}
	return 0;
}