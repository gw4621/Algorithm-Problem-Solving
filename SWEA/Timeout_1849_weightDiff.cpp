#include <iostream>
#include <stack>

int parent[100001];
int weightDiff[100001];
int rank[100001];

int findParent(int a){
	std::stack<int> st;
	std::stack<int> weight;
	int totalW = 0;
	int par = a;
	while(parent[par] != par){
		st.push(par);
		weight.push(weightDiff[par]);
		par = parent[par];
	}
	while(!st.empty()){
		totalW += weight.top();
		weightDiff[st.top()] = totalW;
		parent[st.top()] = par;
		weight.pop();
		st.pop();
	}
	return par;
}

void setHeavier(int a, int b, int w){
	int pa = findParent(a);
	int pb = findParent(b);
	if(pa == pb) return;
	if(rank[pa] < rank[pb]){
		parent[pa] = pb;
		weightDiff[pa] = -w -weightDiff[a] + weightDiff[b];
	}
	else{
		if(rank[pa] == rank[pb]){
			rank[pa] += 1;
		}
		parent[pb] = pa;
		weightDiff[pb] = w + weightDiff[a] -weightDiff[b];
	}
}

/*void checkParent(int N){	// Debugging Function
	for(int i=1;i<N+1;i++){
		std::cout << i << " par: " << parent[i] << " rank: " << rank[i] << " weight: " << weightDiff[i] << std::endl;
	}
}*/

void solve(){
	int N, M;
	int i, a, b, w, pa, pb;
	char order;
	std::cin >> N >> M;
	// Initialization
	for(i=1;i<=N;i++){
		parent[i] = i;
		weightDiff[i] = 0;
		rank[i] = 0;
	}
	// Query
	for(i=0;i<M;i++){
		std::cin >> order;
		if(order == '!'){
			std::cin >> a >> b >> w;
			setHeavier(a, b, w);
			//checkParent(N);
		}
		else if(order == '?'){
			std::cin >> a >> b;
			pa = findParent(a);
			pb = findParent(b);
			//checkParent(N);
			if(pa != pb) std::cout << "UNKNOWN ";
			else{
				std::cout << weightDiff[b] - weightDiff[a] << " ";
			}
		}
	}
}

int main(int argc, char** argv){
	int test_case, T;

	std::ios::sync_with_stdio(false);
	std::cin.tie(0);

	std::cin >> T;
	for(test_case=1;test_case<=T;test_case++){
		std::cout << "#" << test_case << " ";
		solve();
		std::cout << std::endl;
	}

	return 0;
}