/*
	std::sort guarantees O(nlogn) but is not a stable sort by default
	In constrast, time complexity of qsort in C is not specified, but is stable by default.
	However, qsort is not as slow when compared with std::sort
	- If a sort is stable, it does not change the index of objects when they have same value.
*/
#include <cstdio>
#include <algorithm>
#include <vector>

struct numidx{
	int num;
	int idx;
};

std::vector<struct numidx> A;

bool compare(struct numidx a, struct numidx b){
	return (a.num==b.num)? (a.idx < b.idx) : (a.num < b.num);
}

int solve(int N){
	int result = 0;
	std::sort(A.begin(), A.end(), compare);
	for(int i=0;i<N;i++){
		result = std::max(result, A[i].idx - i);
	}
	return result + 1;
}

int main(void){
	int i, N;
	struct numidx tmp;
	scanf("%d", &N);
	getchar();
	for(i=0;i<N;i++){
		scanf("%d", &tmp.num);
		getchar();
		tmp.idx = i;
		A.push_back(tmp);
	}
	printf("%d\n", solve(N));
	return 0;
}