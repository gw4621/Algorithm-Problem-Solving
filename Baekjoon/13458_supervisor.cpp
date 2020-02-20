#include <cstdio>

int n, b, c;
int a[1000000];

long long solve(){
	long long total = static_cast<long long int>(n);
	for(int i=0;i<n;i++){
		a[i] -= b;
		if(a[i] > 0){
			total += static_cast<long long int>(a[i] / c);
			total += (a[i] % c > 0) ? 1 : 0;
		}
	}
	return total;
}

int main(void){
	scanf("%d", &n);
	getchar();
	for(int i=0;i<n;i++){
		scanf("%d", &a[i]);
		getchar();
	}
	scanf("%d %d", &b, &c);
	getchar();
	printf("%lld", solve());
	return 0;
}