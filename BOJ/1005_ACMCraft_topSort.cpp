/*
*	Topological Sort
*	This problem can be solved by dfs too, but problem is that
*	it search for the same node over and over when graph is complex.
*	Using topological sort, this problem can be solved by
*	visiting any node only one time, starting from
*	the ones that do not need previous conditions.
*/

#include <cstdio>
#include <vector>
#include <queue>

int N, K, W;
int D[1001];
int numOfPrecon[1001];
std::vector<int> nextBuild[1001];
int preTime[1001];

std::queue<int> getBuildable(){
	std::queue<int> buildable;
	for(int i=1;i<=N;i++){
		if(numOfPrecon[i] == 0){
			buildable.push(i);
		}
	}
	return buildable;
}

int solve(){
	int i, j;
	int c;
	std::queue<int> q = getBuildable();
	std::vector<int>::iterator it;
	while(!q.empty()){
		c = q.front();
		if(c == W){
			return preTime[W] + D[W];
		}
		for(it=nextBuild[c].begin();it!=nextBuild[c].end();it++){
			preTime[*it] = std::max(preTime[*it], preTime[c]+D[c]);
			numOfPrecon[*it] -= 1;
			if(numOfPrecon[*it] == 0){
				q.push(*it);
			}
		}
		q.pop();
	}

	return preTime[W] + D[W];
}

int main(void){
	int T, i, j, tmp, x, y;
	scanf("%d", &T);
	getchar();
	for(i=0;i<T;i++){
		scanf("%d %d", &N, &K);
		getchar();
		for(j=1;j<=N;j++){
			scanf("%d", &D[j]);
			getchar();
		}
		for(j=1;j<=N;j++){
			nextBuild[j].clear();
			numOfPrecon[j] = 0;
			preTime[j] = 0;
		}
		for(j=1;j<=K;j++){
			scanf("%d %d", &x, &y);
			getchar();
			nextBuild[x].push_back(y);
			numOfPrecon[y] += 1;
		}
		scanf("%d", &W);
		getchar();
		printf("%d\n", solve());
	}
	return 0;
}