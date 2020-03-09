#include <cstdio>
#include <vector>
#include <stdlib.h>
#define FARAWAY 32767


int n, m;
std::vector<std::pair<int, int>> house, chicken;
std::vector<int> combination;

int calcDist(std::pair<int, int> a, std::pair<int, int> b){
	return abs(a.first - b.first) + abs(a.second - b.second);
}

int calcCombinationMinDist(std::vector<int> combination){
	int i, j;
	int dist, minDist, totalMin = 0;
	for(i=0;i<house.size();i++){
		minDist = FARAWAY;
		for(j=0;j<combination.size();j++){
			dist = calcDist(house[i], chicken[combination[j]]);
			if(dist < minDist){
				minDist = dist;
			}
		}
		totalMin += minDist;
	}
	return totalMin;
}

int minimalChickenDist(int a, int b){
	int dist, minDist = FARAWAY;

	for(int i=a;i<chicken.size()-b+1;i++){
		combination.push_back(i);
		if(combination.size() == m){
			dist = calcCombinationMinDist(combination);
			if(minDist > dist){
				minDist = dist;
			}
			combination.pop_back();	
		}
		else{
			dist = minimalChickenDist(i+1, b-1);
			if(dist < minDist){
				minDist = dist;
			}
		}
	}
	combination.pop_back();
	return minDist;
}



void solve(void){
	int i, j, tmp;

	scanf("%d %d", &n, &m);
	getchar();
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			scanf("%d", &tmp);
			getchar();
			if(tmp==1){
				house.push_back(std::pair<int, int>(i, j));
			}
			else if(tmp==2){
				chicken.push_back(std::pair<int, int>(i, j));
			}
		}
	}
	printf("%d", minimalChickenDist(0, m));

}

int main(void){
	solve();
	return 0;
}