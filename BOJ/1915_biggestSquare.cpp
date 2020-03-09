#include <cstdio>

int n, m;
bool **arr;
bool **square;

int solve(){
	int i, j;
	int stage = 1;
	bool hasSquare;
	int locN = n, locM = m;

	hasSquare = false;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			if(arr[i][j]){
				hasSquare = true;
				break;
			}
		}
	}
	if(!hasSquare) return 0;

	while(true){
		locN -= 1;
		locM -= 1;
		hasSquare = false;
		for(i=0;i<locN;i++){
			for(j=0;j<locM;j++){
				if(arr[i][j] && arr[i][j+1] && arr[i+1][j] && arr[i+1][j+1]){
					square[i][j] = true;
					hasSquare = true;
				}
				else square[i][j] = false;
			}
		}
		if(hasSquare){
			stage += 1;
			bool **tmp = arr;
			arr = square;
			square = tmp;
		}
		else return stage*stage;
	}
}

int main(void){
	int i, j;
	scanf("%d %d", &n, &m);
	getchar();
	arr = new bool*[n];
	square = new bool*[n];
	for(i=0;i<n;i++){
		arr[i] = new bool[m];
		square[i] = new bool[m];
	}
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			arr[i][j] = (getchar() == '1');
		}
		getchar();
	}
	printf("%d",solve());
	for(i=0;i<n;i++){
		delete[] arr[i];
		delete[] square[i];
	}
	delete[] arr;
	delete[] square;
	return 0;
}