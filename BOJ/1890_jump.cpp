/*
* DP problem
* Can be solved with priority queue, but takes much time and space
* Solved with dps + dp
*/

#include <cstdio>
#include <stack>

int N;
int board[100][100];
long long route[100][100];
bool visited[100][100];

long long solve(){
	std::stack<std::pair<int, int>> st;
	std::pair<int, int> pos;
	int move, r, c;
	bool both;
	st.push(std::make_pair(0, 0));
	while(!st.empty()){
		pos = st.top();
		r = pos.first;
		c = pos.second;
		if(!(r==N-1 && c==N-1) && board[r][c] == 0){
			visited[r][c] = true;
			route[r][c] = 0;
			st.pop();
			continue;
		}
		move = board[r][c];
		both = true;
		if( (r+move < N) && (!visited[r+move][c]) ){
			st.push(std::make_pair(r+move, c));	
			both = false;
		}
		if( (c+move < N) && (!visited[r][c+move]) ){
			st.push(std::make_pair(r, c+move));
			both = false;
		}
		if(both){
			if(c+move < N) route[r][c] += route[r][c+move];
			if(r+move < N) route[r][c] += route[r+move][c];
			visited[r][c] = true;
			st.pop();
		}
	}
	return route[0][0];
}

int main(void){
	int i, j;
	scanf("%d", &N);
	getchar();
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			scanf("%d", &board[i][j]);
			getchar();
		}
	}
	route[N-1][N-1] = 1;
	visited[N-1][N-1] = true;
	printf("%lld", solve());
	return 0;
}