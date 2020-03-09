#include <cstdio>
#include <utility>
#include <cmath>

int N;
std::pair<long long, long long> firstP;
std::pair<long long, long long> Points[10000];

void solve(){
	int i;
	long long answer = 0;
	for(i=0;i<N-2;i++){
		answer += (firstP.first*Points[i].second + Points[i].first*Points[i+1].second + Points[i+1].first * firstP.second - firstP.first * Points[i+1].second - Points[i+1].first * Points[i].second - Points[i].first * firstP.second);
	}
	answer = std::abs(answer);
	printf("%lld", answer/2);
	if(answer%2 > 0) printf(".5");
	else printf(".0");
}

int main(void){
	int i;
	scanf("%d", &N);
	getchar();
	scanf("%lld %lld", &firstP.first, &firstP.second);
	getchar();
	for(i=0;i<N-1;i++){
		scanf("%lld %lld", &Points[i].first, &Points[i].second);
		getchar();
	}
	solve();
	return 0;
}