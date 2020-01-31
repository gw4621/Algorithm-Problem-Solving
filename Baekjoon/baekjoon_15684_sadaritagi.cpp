#include <cstdio>

int N, M, H;

int ladderGoesTo[31][11];
int newLadder[31][11];

bool check(){
	int i1, j1;
	int position[N+1];
	for(i1=1;i1<=N;i1++){
		position[i1] = i1;
	}
	for(i1=1;i1<=H;i1++){
		for(j1=1;j1<N;j1++){
			position[j1] = newLadder[i1][position[j1]];
		}
	}
	for(i1=1;i1<=N;i1++){
		if(position[i1] != i1) return false;
	}
	return true;
}

void initNewLadder(){
	for(int i1=1;i1<=H;i1++){
		for(int j1=1;j1<=N;j1++){
			newLadder[i1][j1] = ladderGoesTo[i1][j1];
		}
	}
}

int solve(){
	int i1, j1, i2, j2, i3, j3;
	int minimal = 4;
	// Check If it is already done
	initNewLadder();
	if(check()){
		return 0;
	}
	// Not done, put one horizontal line and check
	for(i1=1;i1<=H;i1++){
		for(j1=1;j1<=N-1;j1++){
			if(newLadder[i1][j1] == j1 && newLadder[i1][j1+1] == j1+1){
				newLadder[i1][j1] = j1+1;
				newLadder[i1][j1+1] = j1;
				if(check()) return 1;
				for(i2=i1;i2<=H;i2++){
					for(j2=1;j2<=N-1;j2++){
						if(newLadder[i2][j2] == j2 && newLadder[i2][j2+1] == j2+1){
							newLadder[i2][j2] = j2+1;
							newLadder[i2][j2+1] = j2;
							if(check() && minimal > 2) minimal = 2;
							if(minimal > 3){
								for(i3=i2;i3<=H;i3++){
									for(j3=1;j3<=N-1;j3++){
										if(newLadder[i3][j3] == j3 && newLadder[i3][j3+1] == j3+1){
											newLadder[i3][j3] = j3+1;
											newLadder[i3][j3+1] = j3;
											if(check()) minimal = 3;
											newLadder[i3][j3] = j3;
											newLadder[i3][j3+1] = j3+1;
										}
									}
								}
							}
							newLadder[i2][j2] = j2;
							newLadder[i2][j2+1] = j2+1;
						}
					}
				}
				newLadder[i1][j1] = j1;
				newLadder[i1][j1+1] = j1+1;	
			}
		}
	}
	return minimal>3?-1:minimal;
}

int main(void){
	int a, b;
	scanf("%d %d %d", &N, &M, &H);
	for(int i1=1;i1<=H;i1++){
		for(int j1=1;j1<=N;j1++){
			ladderGoesTo[i1][j1] = j1;
		}
	}
	for(int i1=0;i1<M;i1++){
		scanf("%d %d", &a, &b);
		getchar();
		ladderGoesTo[a][b] = b+1;
		ladderGoesTo[a][b+1] = b;
	}
	printf("%d", solve());
	return 0;
}