#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

#define UP 1
#define DOWN 2
#define RIGHT 3
#define LEFT 4

class Shark{
	public:
		int row, col;
		int speed;
		int direction;
		int size;
		Shark *next, *prev;
		Shark(int row, int col, int speed, int direction, int size){
			this->row = row;
			this->col = col;
			this->speed = speed;
			this->direction = direction;
			this->size = size;
			next = nullptr;
			prev = nullptr;
		}
};

int r, c, m;
Shark* sharkMap[110][110];
Shark* sharkPtr;

void eraseShark(Shark *toErase){
	if(toErase == nullptr){
		return;
	}
	if(toErase->prev == nullptr && toErase->next == nullptr){
		sharkPtr = nullptr;
		delete toErase;
	}
	else if(toErase->prev == nullptr){
		sharkPtr = toErase->next;
		sharkPtr->prev = nullptr;
		delete toErase;
	}
	else if(toErase->next == nullptr){
		toErase->prev->next = nullptr;
		delete toErase;
	}
	else{
		toErase->prev->next = toErase->next;
		toErase->next->prev = toErase->prev;
		delete toErase;
	}
}

int catchShark(int kingCol){
	int closestToEarth = 101;
	int sharkSize = 0;
	Shark *toErase=nullptr, *currentShark=sharkPtr;
	while(currentShark != nullptr){
		if(currentShark->col == kingCol && currentShark->row < closestToEarth){
			sharkSize = currentShark->size;
			closestToEarth = currentShark->row;
			toErase = currentShark;
		}
		currentShark = currentShark->next;
	}
	eraseShark(toErase);
	return sharkSize;
}

void sharkMove(void){
	int i, j, speedCount;
	for(i=0;i<101;i++){
		for(j=0;j<101;j++){
			sharkMap[i][j] = nullptr;
		}
	}
	Shark *currentShark = sharkPtr;
	while(currentShark != nullptr){
		speedCount = currentShark->speed;
		while(speedCount > 0){	// Shark Move According to Speed and Direction
			if(currentShark->direction == UP){
				if(currentShark->row == 1){
					currentShark->direction = DOWN;
					currentShark->row += 1;
				}
				else{
					currentShark->row -= 1;
				}
			}
			else if(currentShark->direction == DOWN){
				if(currentShark->row == r){
					currentShark->direction = UP;
					currentShark->row -= 1;
				}
				else{
					currentShark->row += 1;
				}
			}
			else if(currentShark->direction == RIGHT){
				if(currentShark->col == c){
					currentShark->direction = LEFT;
					currentShark->col -= 1;
				}
				else{
					currentShark->col += 1;
				}
			}
			else if(currentShark->direction == LEFT){
				if(currentShark->col == 1){
					currentShark->direction = RIGHT;
					currentShark->col += 1;
				}
				else{
					currentShark->col -= 1;
				}
			}
			speedCount -= 1;
		}	// Shark Move End
		// Assign Shark to Sharkmap:
		if(sharkMap[currentShark->row][currentShark->col] == nullptr){
			sharkMap[currentShark->row][currentShark->col] = currentShark;
			currentShark = currentShark -> next;
		}
		else{	// If another shark exists, fight, and one of them dies.
			if(sharkMap[currentShark->row][currentShark->col]->size > currentShark->size){
				currentShark = currentShark -> next;
				eraseShark(currentShark->prev);
			}
			else{
				eraseShark(sharkMap[currentShark->row][currentShark->col]);
				sharkMap[currentShark->row][currentShark->col] = currentShark;
				currentShark = currentShark -> next;
			}
		}
		//printf("Eat ENd\n");
	}
}

void solve(void){
	int row, col, s, d, z;
	int kingCol, kingSharkTotal;
	Shark* currentShark;

	scanf("%d %d %d", &r, &c, &m);
	getchar();

	if(m==0){
		printf("0");
		return;
	}

	// Get Shark information
	// First Shark
	scanf("%d %d %d %d %d", &row, &col, &s, &d, &z);
	getchar();
	if(d <= 2){
		s = s % ((r-1)*2);		
	}
	else{
		s = s % ((c-1)*2);
	}
	sharkPtr = new Shark(row, col, s, d, z);
	currentShark = sharkPtr;
	// From second shark to the last
	for(int i=1;i<m;i++){
		scanf("%d %d %d %d %d", &row, &col, &s, &d, &z);
		getchar();
		if(d <= 2){
			s = s % ((r-1)*2);		
		}
		else{
			s = s % ((c-1)*2);
		}
		printf("%d. ", i);
		currentShark->next = new Shark(row, col, s, d, z);
		printf("%d\n", i);
		currentShark->next->prev = currentShark;
		currentShark = currentShark->next;
	}

	kingCol = 1;
	kingSharkTotal = 0;
	while(kingCol <= c){
		if(sharkPtr == nullptr){
			break;
		}
		kingSharkTotal += catchShark(kingCol);
		sharkMove();
		printf("kingSharkTotal=%d\n", kingSharkTotal);
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				if(sharkMap[i][j] != nullptr){
					printf("%d %d %d %d %d\n", sharkMap[i][j]->row, sharkMap[i][j]->col, sharkMap[i][j]->speed, sharkMap[i][j]->direction, sharkMap[i][j]->size);
				}
			}
		}
		printf("\n");
		kingCol ++;

	}
	int totalMemory = 0;
	// Delete memory
	if(sharkPtr != nullptr){
		while(sharkPtr->next != nullptr){
			sharkPtr = sharkPtr->next;
			totalMemory += sizeof(*(sharkPtr->prev));
			delete sharkPtr->prev;
		}
		totalMemory += sizeof(*sharkPtr);
		delete sharkPtr;
	}
	printf("%d\n", totalMemory);
	printf("%d", kingSharkTotal);
}


int main(void){
	solve();
	return 0;
}