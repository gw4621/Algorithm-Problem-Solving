#include <cstdio>
#include <cmath>

char map[101][101];
char transposeMap[101][101];

bool checkRowRoad(int N, int L, int row){
	bool occupied[101] = {false, };
	int i, j;
	for(i=0;i<N-1;i++){
		if(map[row][i] == map[row][i+1] + 1){
			if(i+1+L > N){
				return false;
			}
			for(j=i+1;j<i+1+L;j++){
				if(!(map[row][j] == map[row][i+1] and !occupied[j])){
					return false;			
				}
			}
			for(j=i+1;j<i+1+L;j++){
				occupied[j] = true;
			}	
		}
		else if(map[row][i] == map[row][i+1] - 1){
			if(i-L < -1){
				return false;
			}
			for(j=i;j>i-L;j--){
				if(!(map[row][j] == map[row][i] and !occupied[j])){
					return false;
				}
			}
			for(j=i;j>i-L;j--){
				occupied[j] = true;
			}
		}
		else if(std::abs(map[row][i] - map[row][i+1]) > 1){
			return false;
		}
	}
	return true;
}

bool checkColRoad(int N, int L, int row){
	bool occupied[101] = {false, };
	int i, j;
	for(i=0;i<N-1;i++){
		if(transposeMap[row][i] == transposeMap[row][i+1] + 1){
			if(i+1+L > N){
				return false;
			}
			for(j=i+1;j<i+1+L;j++){
				if(!(transposeMap[row][j] == transposeMap[row][i+1] and !occupied[j])){
					return false;			
				}
			}
			for(j=i+1;j<i+1+L;j++){
				occupied[j] = true;
			}
			
		}
		else if(transposeMap[row][i] == transposeMap[row][i+1] - 1){
			if(i-L < -1){
				return false;
			}
			for(j=i;j>i-L;j--){
				if(!(transposeMap[row][j] == transposeMap[row][i] and !occupied[j])){
					return false;
				}
			}
			for(j=i;j>i-L;j--){
				occupied[j] = true;
			}
		}
		else if(std::abs(transposeMap[row][i] - transposeMap[row][i+1]) > 1){
			return false;
		}
	}
	return true;
}

int solve(int N, int L){
	int i, j;
	int isRoad = 0;

	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			transposeMap[i][j] = map[j][i];
		}
	}
	
	for(i=0;i<N;i++){
		if(checkRowRoad(N, L, i)){
			isRoad += 1;
		}
		if(checkColRoad(N, L, i)){
			isRoad += 1;
		}
	}

	return isRoad;	
}

int main(void){
	int N, L;
	
	scanf("%d %d", &N, &L);
	getchar();
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			scanf("%d", &map[i][j]);
			getchar();
		}
	}
	printf("%d", solve(N, L));

	return 0;
}