#include <cstdio>

int R, C, T;
int **A;


void phase1(void){
	int nextA[R][C];
	int i, j;
	int diffusion;
	
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			nextA[i][j] = 0;
		}
	}

	// Four Corner
	diffusion = A[0][0] / 5;
	nextA[0][0] += A[0][0] - diffusion*2;
	nextA[0][1] += diffusion;
	nextA[1][0] += diffusion;
	diffusion = A[0][C-1] / 5;
	nextA[0][C-1] += A[0][C-1] - diffusion*2;
	nextA[0][C-2] += diffusion;
	nextA[1][C-1] += diffusion;
	diffusion = A[R-1][0] / 5;
	nextA[R-1][0] += A[R-1][0] - diffusion*2;
	nextA[R-1][1] += diffusion;
	nextA[R-2][0] += diffusion;
	diffusion = A[R-1][C-1] / 5;
	nextA[R-1][C-1] += A[R-1][C-1] - diffusion*2;
	nextA[R-1][C-2] += diffusion;
	nextA[R-2][C-1] += diffusion;

	// Four Edge
	for(i=1;i<R-1;i++){
		diffusion = A[i][0] / 5;
		nextA[i][0] += A[i][0] - diffusion * 3;
		nextA[i-1][0] += diffusion;
		nextA[i+1][0] += diffusion;
		nextA[i][1] += diffusion;
		diffusion = A[i][C-1] / 5;
		nextA[i][C-1] += A[i][C-1] - diffusion * 3;
		nextA[i-1][C-1] += diffusion;
		nextA[i+1][C-1] += diffusion;
		nextA[i][C-2] += diffusion;
	}
	for(i=1;i<C-1;i++){
		diffusion = A[0][i]/5;
		nextA[0][i] += A[0][i] - diffusion * 3;
		nextA[1][i] += diffusion;
		nextA[0][i-1] += diffusion;
		nextA[0][i+1] += diffusion;
		diffusion = A[R-1][i]/5;
		nextA[R-1][i] += A[R-1][i] - diffusion * 3;
		nextA[R-2][i] += diffusion;
		nextA[R-1][i-1] += diffusion;
		nextA[R-1][i+1] += diffusion;
	}
	
	// One line which has air purifier on its left
	for(i=1;i<R-1;i++){
		if(A[i][0] == -1){
			diffusion = A[i][1] / 5;
			nextA[i][1] += A[i][1] - diffusion * 3;
			nextA[i-1][1] += diffusion;
			nextA[i+1][1] += diffusion;
			nextA[i][2] += diffusion;
		}
		else{
			diffusion = A[i][1] / 5;
			nextA[i][1] += A[i][1] - diffusion * 4;
			nextA[i-1][1] += diffusion;
			nextA[i+1][1] += diffusion;
			nextA[i][0] += diffusion;
			nextA[i][2] += diffusion;
		}
	}

	// Center
	for(i=1;i<R-1;i++){
		for(j=2;j<C-1;j++){
			diffusion = A[i][j] / 5;
			nextA[i][j] += A[i][j] - diffusion * 4;
			nextA[i-1][j] += diffusion;
			nextA[i+1][j] += diffusion;
			nextA[i][j-1] += diffusion;
			nextA[i][j+1] += diffusion;
		}
	}

	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			if(A[i][j] != -1){
				A[i][j] = nextA[i][j];
			}
		}
	}

}

void phase2(void){
	int purC[2];
	int i, j;

	// Find Air Purifier
	for(i=0;i<R;i++){
		if(A[i][0] == -1){
			purC[0] = i;
			purC[1] = i+1;
			break;
		}
	}

	// Wind 1
	for(i=purC[0]-2;i>=0;i--){
		A[i+1][0] = A[i][0];
	}
	for(j=1;j<C;j++){
		A[0][j-1] = A[0][j]; 
	}
	for(i=0;i<purC[0];i++){
		A[i][C-1] = A[i+1][C-1];
	}
	for(j=C-1;j>=2;j--){
		A[purC[0]][j] = A[purC[0]][j-1];
	}
	A[purC[0]][1] = 0;

	// Wind 2
	for(i=purC[1]+2;i<R;i++){
		A[i-1][0] = A[i][0];
	}
	for(j=1;j<C;j++){
		A[R-1][j-1] = A[R-1][j];
	}
	for(i=R-1;i>purC[1];i--){
		A[i][C-1] = A[i-1][C-1];
	}
	for(j=C-1;j>=2;j--){
		A[purC[1]][j] = A[purC[1]][j-1];
	}
	A[purC[1]][1] = 0;
}

void solve(void){
	int i, j;
	int ans;

	scanf("%d %d %d", &R, &C, &T);
	getchar();

	A = new int*[R];
	for(i=0;i<R;i++){
		A[i] = new int[C];
	}
	
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			scanf("%d", &A[i][j]);
			getchar();
		}
	}

	for(i=0;i<T;i++){
		phase1();
		phase2();
	}

	ans = 0;

	for(i=0;i<R;i++){
		if(A[i][0] != -1){
			ans += A[i][0];
		}
	}
	for(i=0;i<R;i++){
		for(j=1;j<C;j++){
			ans += A[i][j];
		}
	}

	printf("%d", ans);

	for(i=0;i<R;i++){
		delete A[i];
	}
	delete A;
}


int main(void){
	solve();
	return 0;
}