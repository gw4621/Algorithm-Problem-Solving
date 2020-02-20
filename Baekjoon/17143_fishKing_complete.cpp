#include <vector>
#include <cstdio>
#include <map>

#define UP 1
#define DOWN 2
#define RIGHT 3
#define LEFT 4

int R, C, M;

class Shark{
	public:
		char dir;
		short speed;
		short size;
		Shark(){
			dir = 0;
			speed = 0;
			size = 0;
		}
		Shark(short speed, char dir, short size){
			this->dir = dir;
			this->speed = speed;
			this->size = size;
		}
		Shark(int speed, int dir, int size){
			this->dir = static_cast<char>(dir);
			this->speed = static_cast<short>(speed);
			this->size = static_cast<short>(size);
		}
};


std::map<std::pair<char, char>, Shark> sharkMap;
std::map<std::pair<char, char>, Shark> newSharkMap;


int catchShark(int king){
	std::map<std::pair<char, char>, Shark>::iterator it, toErase;
	bool caught = false;
	int closestToEarth = 128;
	int biggestSize = 0;
	for(it=sharkMap.begin();it!=sharkMap.end();it++){
		if(it->first.second == king && it->first.first < closestToEarth){
			caught = true;
			closestToEarth = it->first.first;
			biggestSize = it->second.size;
			toErase = it;
		}
	}
	if(caught) sharkMap.erase(toErase);
	return biggestSize;	
}

void sharkMove(){
	std::map<std::pair<char, char>, Shark>::iterator it;
	char row, col, dir;
	short speedCount;
	for(it=sharkMap.begin();it!=sharkMap.end();it++){
		speedCount = it->second.speed;
		row = it->first.first;
		col = it->first.second;
		dir = it->second.dir;
		while(speedCount > 0){
			if(dir == UP){
				if(row == 1){
					dir = DOWN;
					row += 1;
				}
				else row -= 1;
			}
			else if(dir == DOWN){
				if(row == R){
					dir = UP;
					row -= 1;
				}
				else row += 1;
			}
			else if(dir == LEFT){
				if(col == 1){
					dir = RIGHT;
					col += 1;
				}
				else col -= 1;
			}
			else if(dir == RIGHT){
				if(col == C){
					dir = LEFT;
					col -= 1;
				}
				else col += 1;
			}
			speedCount -= 1;
		}
		if(newSharkMap.count(std::make_pair(row, col)) > 0){	// If there already exists a shark, fight
			if(newSharkMap[std::make_pair(row, col)].size < it->second.size){
				it->second.dir = dir;
				newSharkMap[std::make_pair(row, col)] = it->second;
			}
		}
		else{	// Else occupy the position
			newSharkMap.insert(std::make_pair(std::make_pair(row, col), Shark(it->second.speed, dir, it->second.size)));
		}
	}
	sharkMap.clear();
	sharkMap = newSharkMap;
	newSharkMap.clear();
}

void solve(void){
	int i, j;
	int row, col, s, d, z;
	int kingSharkTotal = 0;

	scanf("%d %d %d", &R, &C, &M);
	getchar();
	if(M == 0){
		printf("0");
		return;
	}
	for(i=0;i<M;i++){
		scanf("%d %d %d %d %d", &row, &col, &s, &d, &z);
		getchar();
		if(d <= 2){
			s = s % ((R-1)*2);
		}
		else{
			s = s % ((C-1)*2);
		}
		sharkMap.insert(std::make_pair(std::make_pair(static_cast<char>(row), static_cast<char>(col)), Shark(s, d, z)));
	}
	for(int king=1;king<=C;king++){
		kingSharkTotal += catchShark(king);
		if(sharkMap.size() == 0) break;
		sharkMove();
		/*std::map<std::pair<char, char>, Shark>::iterator it;
		printf("\n");
		for(it=sharkMap.begin();it!=sharkMap.end();it++){
			printf("%d %d %d %d %d\n", it->first.first, it->first.second, it->second.speed, it->second.dir, it->second.size);
		}
		printf("\n");*/
	}
	printf("%d", kingSharkTotal);
}

int main(void){
	solve();
	return 0;
}