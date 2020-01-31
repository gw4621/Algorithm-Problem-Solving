#include <cstdio>
#include <stdlib.h>
#include <queue>
#define FARAWAY 32768
#define WALL 32768

int **map;
int **distMap;

std::queue<int> xq, yq;
bool **visited;

void makeDistMap(int N, int sharkY, int sharkX, int sharkSize){		
	int i, j, x, y;
	for(i=0;i<N+2;i++){
		for(j=0;j<N+2;j++){
			visited[i][j] = false;
			distMap[i][j] = FARAWAY;
		}
	}
	
	xq.push(sharkX);
	yq.push(sharkY);
	distMap[sharkY][sharkX] = 0;
	visited[sharkY][sharkX] = true;
	while(!xq.empty()){
		x = xq.front();
		y = yq.front();
		xq.pop();
		yq.pop();
		for(i=-1;i<=1;i+=2){
			if(map[y+i][x] <= sharkSize && !visited[y+i][x]){
				distMap[y+i][x] = distMap[y][x] + 1;
				visited[y+i][x] = true;
				xq.push(x);
				yq.push(y+i);
			}
			if(map[y][x+i] <= sharkSize && !visited[y][x+i]){
				distMap[y][x+i] = distMap[y][x] + 1;
				visited[y][x+i] = true;
				xq.push(x+i);
				yq.push(y);
			}
		}
	}
	return;
}

void solve(void){
	int N;
	int i, j, a, b;
	int sharkX, sharkY;
	scanf("%d", &N);
	getchar();
	
	map = new int*[N+2];
	distMap = new int*[N+2];
	visited = new bool*[N+2];
	for(i=0;i<N+2;i++){
		map[i] = new int[N+2];
		distMap[i] = new int[N+2];
		visited[i] = new bool[N+2];
	}
	for(i=0;i<N+2;i++){
		map[i][0] = WALL;
		map[i][N+1] = WALL;
		map[0][i] = WALL;
		map[N+1][i] = WALL;
	}
	for(i=1;i<N+1;i++){
		for(j=1;j<N+1;j++){
			scanf("%d", &map[i][j]);
			getchar();
			if(map[i][j] == 9){
				sharkX = j;
				sharkY = i;
				map[i][j] = 0;
			}
		}
	}
	int sharkSize = 2;
	int evoCount = sharkSize;
	int preyX, preyY, preyDist;
	int totalDist = 0;
	while(true){
		preyDist = FARAWAY;
		makeDistMap(N, sharkY, sharkX, sharkSize);
		/* FOR DEBUGGING
		printf("%d\n", sharkSize);
		for(i=1;i<N+1;i++){
			for(j=1;j<N+1;j++){
				printf("%d(%d) ", distMap[i][j], map[i][j]);
			}
			printf("\n");
		}
		*/
		for(i=1;i<N+1;i++){
			for(j=1;j<N+1;j++){
				if(map[i][j] < sharkSize && map[i][j] > 0 && distMap[i][j] < preyDist){
					preyX = j;
					preyY = i;
					preyDist = distMap[i][j];
				}
			}
		}
		
		if(preyDist == FARAWAY){
			break;
		}
		else{
			totalDist += preyDist;
			sharkX = preyX;
			sharkY = preyY;
			map[preyY][preyX] = 0;
			if(--evoCount == 0){
				sharkSize += 1;
				evoCount = sharkSize;
			}
		}
		//printf("preyDist=%d, totalDist=%d\n\n", preyDist, totalDist);
	}

	printf("%d", totalDist);

	for(i=0;i<N+2;i++){
		delete[] map[i];
		delete[] distMap[i];
		delete[] visited[i];
	}
	delete[] map;
	delete[] distMap;
	delete[] visited;
}

int main(void){
	solve();
	return 0;
}