/*
* Solve using recursive DFS
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <stack>

int sX, sY, eX, eY;
int cX[10], cY[10];
int s2c[10];
int c2e[10];
int c2c[10][10];
bool visited[10];
int N;
int minVal;

int getDist(int x1, int y1, int x2, int y2){
	return std::abs(x1-x2) + std::abs(y1-y2);
}

void recurDist(int val, int prev, int cnt){
	int i;
	if(cnt==N){
		minVal = std::min(val+c2e[prev], minVal);
		return;
	}
	for(i=0;i<N;i++){
		if(visited[i]) continue;
		visited[i] = true;
		recurDist(val+c2c[prev][i], i, cnt+1);
		visited[i] = false;
	}
}

void solve(){
	int i, j;
	minVal = 0x7fffffff;
	for(i=0;i<N;i++){
		s2c[i] = getDist(sX, sY, cX[i], cY[i]);
		c2e[i] = getDist(cX[i], cY[i], eX, eY);
		visited[i] = false;
		for(j=i+1;j<N;j++){
			c2c[i][j] = getDist(cX[i], cY[i], cX[j], cY[j]);
			c2c[j][i] = c2c[i][j];
		}
	}
	for(i=0;i<N;i++){
		visited[i] = true;
		recurDist(s2c[i], i, 1);
		visited[i] = false;
	}
}

int main(void){
	int T, test_case;
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	std::cin >> T;
	for(test_case=1;test_case<=T;test_case++){
		std::cin >> N;
		std::cin >> sX >> sY >> eX >> eY;
		for(int i=0;i<N;i++){
			std::cin >> cX[i] >> cY[i];
		}
		solve();
		std::cout << "#" << test_case << " " << minVal << std::endl;
	}
	return 0;
}