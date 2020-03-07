#include <cstdio>
#include <vector>
#include <algorithm>

#define EMPTY 0
#define WALL 6

int N, M;
char map[10][10];
char cType[8], cRow[8], cCol[8], cCount;

char cctv1[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
char cctv2[2][2][2] = { { {0, 1}, {0, -1} }, { {1, 0}, {-1, 0} } };
char cctv3[4][2][2] = { { {0, 1}, {1, 0} }, { {0, 1}, {-1, 0} }, { {0, -1}, {1, 0} }, { {0, -1}, {-1, 0} } };
char cctv4[4][3][2] = { { {0, 1}, {0, -1}, {1, 0} }, { {0, 1}, {0, -1}, {-1, 0} }, { {1, 0}, {-1, 0}, {0, 1} }, { {1, 0}, {-1, 0}, {0, -1} } };
char cctv5[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

class Node{
public:
	char **map;
	char cNum;
	Node(char cNum, char **map){
		this->cNum = cNum;
		this->map = map;
	}
	~Node(){
		for(int i=0;i<10;i++){
			delete[] map[i];
		}
		delete[] map;
	}
};

std::vector<Node *> st;

int countBlind(char **completeMap){
	int blind = 0;
	for(int i=1;i<N+1;i++){
		for(int j=1;j<M+1;j++){
			if(completeMap[i][j] == EMPTY){
				blind += 1;
			}
		}
	}
	return blind;
}

char** copyMap(char **originalMap){
	char **newMap = new char*[10];
	for(int i=0;i<10;i++){
		newMap[i] = new char[10];
		for(int j=0;j<10;j++){
			newMap[i][j] = originalMap[i][j];
		}
	}
	return newMap;
}

void handleCCTV(const Node* cNode){
	int i, j, k;
	char r, c, defaultR = cRow[cNode->cNum], defaultC = cCol[cNode->cNum];
	char nextNum = (cNode->cNum) + 1;
	switch(cType[cNode->cNum]){
		case 1:
		for(i=0;i<4;i++){
			r = defaultR;
			c = defaultC;
			char **newMap = copyMap(cNode->map);
			while(true){
				r += cctv1[i][0];
				c += cctv1[i][1];
				if(newMap[r][c] == EMPTY) newMap[r][c] = '#';
				else if(newMap[r][c] == WALL) break;
			}
			st.push_back(new Node(nextNum, newMap));
		}
		break;
		case 2:
		for(i=0;i<2;i++){
			char **newMap = copyMap(cNode->map);
			for(j=0;j<2;j++){
				r = defaultR;
				c = defaultC;
				while(true){
					r += cctv2[i][j][0];
					c += cctv2[i][j][1];
					if(newMap[r][c] == EMPTY) newMap[r][c] = '#';
					else if(newMap[r][c] == WALL) break;
				}
			}
			st.push_back(new Node(nextNum, newMap));
		}
		break;
		case 3:
		for(i=0;i<4;i++){
			char **newMap = copyMap(cNode->map);
			for(j=0;j<2;j++){
				r = defaultR;
				c = defaultC;
				while(true){
					r += cctv3[i][j][0];
					c += cctv3[i][j][1];
					if(newMap[r][c] == EMPTY) newMap[r][c] = '#';
					else if(newMap[r][c] == WALL) break;
				}
			}
			st.push_back(new Node(nextNum, newMap));
		}
		break;
		case 4:
		for(i=0;i<4;i++){
			char **newMap = copyMap(cNode->map);
			for(j=0;j<3;j++){
				r = defaultR;
				c = defaultC;
				while(true){
					r += cctv4[i][j][0];
					c += cctv4[i][j][1];
					if(newMap[r][c] == EMPTY) newMap[r][c] = '#';
					else if(newMap[r][c] == WALL) break;
				}
			}
			st.push_back(new Node(nextNum, newMap));
		}
		break;
		case 5:
		char **newMap = copyMap(cNode->map);
		for(i=0;i<4;i++){
			r = defaultR;
			c = defaultC;
			while(true){
				r += cctv5[i][0];
				c += cctv5[i][1];
				if(newMap[r][c] == EMPTY) newMap[r][c] = '#';
				else if(newMap[r][c] == WALL) break;
			}
		}
		st.push_back(new Node(nextNum, newMap));
		break;
	}
}

int solve(){
	int i, j;
	int minBlind = 100;
	char **newMap = new char*[10];
	for(i=0;i<10;i++){
		newMap[i] = new char[10];
		for(j=0;j<10;j++){
			newMap[i][j] = map[i][j];
		}
	}
	st.clear();
	st.push_back(new Node(0, newMap));
	while(!st.empty()){
		Node* cNode = st.back();
		st.pop_back();
		if(cNode->cNum == cCount){
			minBlind = std::min(minBlind, countBlind(cNode->map));
		}
		else{
			handleCCTV(cNode);
		}
		delete cNode;
	}
	return minBlind;
}

int main(void){
	int i, j;
	scanf("%d %d", &N, &M);
	getchar();
	for(i=0;i<N+2;i++){
		map[i][0] = WALL;
		map[i][M+1] = WALL;
	}
	for(i=0;i<M+2;i++){
		map[0][i] = WALL;
		map[N+1][i] = WALL;
	}
	cCount = 0;
	for(i=1;i<N+1;i++){
		for(j=1;j<M+1;j++){
			scanf("%d", &map[i][j]);
			getchar();
			if(map[i][j] > 0 && map[i][j] < 6){
				cRow[cCount] = i;
				cCol[cCount] = j;
				cType[cCount] = map[i][j];
				cCount += 1;
			}
		}
	}
	printf("%d", solve());
	return 0;
}