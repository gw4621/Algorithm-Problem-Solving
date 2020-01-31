#include <iostream>
#include <string>
#include <cstdio>
#include <deque>
#include <stack>
#include <array>
#include <algorithm>

bool compare(std::array<int, 3> a, std::array<int, 3> b){
	return a[2] < b[2];
}

int getParent(int *parent, int n){
	std::stack<int> st;
	while(parent[n] != n){
		st.push(n);
		n = parent[n];
	}
	while(!st.empty()){
		parent[st.top()] = n;
		st.pop();
	}
	return n;
}

void solve(void){
	int i, j, a, b, c;  // Temporary Variable
	int n, m;   // Basic information
	

	scanf("%d", &n);
	getchar();
	scanf("%d", &m);
	getchar();
	std::deque<std::array<int, 3>> G;

	for(i=0;i<m;i++){
		scanf("%d %d %d", &a, &b, &c);
		getchar();
		G.push_back({a-1, b-1, c});  
	}

	int parent[n];
	for(i=0;i<n;i++){
		parent[i] = i;
	}

	sort(G.begin(), G.end(), compare);

	int connected = 0, sumOfConnPrice = 0;
	int parent1, parent2;
	while(connected < n-1){
		parent1 = getParent(parent, G.front()[0]);
		parent2 = getParent(parent, G.front()[1]);
		if(parent1 > parent2){
			parent[parent1] = parent2;
			sumOfConnPrice += G.front()[2];
			connected ++;
		}
		else if(parent1 < parent2){
			parent[parent2] = parent1;
			sumOfConnPrice += G.front()[2];
			connected ++;
		}
		G.pop_front();
	}
	
	printf("%d", sumOfConnPrice);
	return;
}

int main(void){
	solve();

	return 0;
}
