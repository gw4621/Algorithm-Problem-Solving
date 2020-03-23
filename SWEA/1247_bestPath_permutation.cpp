/*
* Solve using permutation
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

int sX, sY, eX, eY;
int cX[10], cY[10];
int s2c[10];
int c2e[10];
int c2c[10][10];
int N;

int getDist(int x1, int y1, int x2, int y2){
	return std::abs(x1-x2) + std::abs(y1-y2);
}

int solve(){
	int i, j;
	int minVal = 0x7fffffff, val;
	std::vector<int> v(N);
	for(i=0;i<N;i++){
		v[i] = i;
		s2c[i] = getDist(sX, sY, cX[i], cY[i]);
		c2e[i] = getDist(cX[i], cY[i], eX, eY);
		for(j=i+1;j<N;j++){
			c2c[i][j] = getDist(cX[i], cY[i], cX[j], cY[j]);
			c2c[j][i] = c2c[i][j];
		}
	}
	do{
		val = s2c[v[0]];
		for(i=0;i<N-1;i++){
			val += c2c[v[i]][v[i+1]];
		}
		val += c2e[v[N-1]];
		minVal = std::min(minVal, val);
	} while(std::next_permutation(v.begin(), v.end()));
	return minVal;
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
		std::cout << "#" << test_case << " " << solve() << std::endl;
	}
	return 0;
}