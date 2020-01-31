#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>

struct Node{
	int ancestor[21];
	int depth;
};

struct Node nodes[100001];
std::vector<int> conn[100001];

void solve(void){
	int n, m, a, b;
	int i, j;
	int currentNum;

	// Get N
	scanf("%d", &n);
	getchar();

	/*struct Node *nodes = new struct Node[n+1];
	std::vector<int> *conn = new std::vector<int>[n+1];*/
	std::stack<int> *dfsSt = new std::stack<int>;

	// Save connection data
	for(i=0;i<n-1;i++){
		scanf("%d %d", &a, &b);
		getchar();
		conn[a].push_back(b);
		conn[b].push_back(a);
	}

	// Make Tree from Graph
	for(i=0;i<21;i++){
		nodes[1].ancestor[i] = 1;
	}
	nodes[1].depth = 1;
	std::vector<int>::iterator it;
	for(it=conn[1].begin(); it!=conn[1].end();it++){
		nodes[*it].ancestor[0] = 1;
		nodes[*it].depth = 2;
		dfsSt->push(*it);
	}

	while(!dfsSt->empty()){
		currentNum = dfsSt->top();
		dfsSt->pop();
		for(it=conn[currentNum].begin();it!=conn[currentNum].end();it++){
			if(*it == nodes[currentNum].ancestor[0])	continue;
			nodes[*it].ancestor[0] = currentNum;
			nodes[*it].depth = nodes[currentNum].depth + 1;
			dfsSt->push(*it);
		}
	}

	delete dfsSt;
	//delete conn;

	// Get all the ancestors(2^n)
	for(i=1;i<21;i++){
		for(j=2;j<n+1;j++){
			nodes[j].ancestor[i] = nodes[nodes[j].ancestor[i-1]].ancestor[i-1];
		}
	}

	scanf("%d", &m);
	getchar();
	int answer[m];
	for(i=0;i<m;i++){
		scanf("%d %d", &a, &b);
		getchar();
		// B should have more depth (exchange if not)
		if(nodes[a].depth > nodes[b].depth){
			a = a + b;
			b = a - b;
			a = a - b;
		}
		// Get B's ancestor which has A's depth
		for(j=20;j>=0;j--){
			if(nodes[nodes[b].ancestor[j]].depth >= nodes[a].depth){
				b = nodes[b].ancestor[j];
			}
		}
		if(a == b){
			answer[i] = a;
			continue;
		}
		for(j=20;j>=0;j--){
			if(nodes[a].ancestor[j] != nodes[b].ancestor[j]){
				a = nodes[a].ancestor[j];
				b = nodes[b].ancestor[j];
			}
		}
		answer[i] = nodes[a].ancestor[0];
	}
	for(i=0;i<m;i++){
		printf("%d\n", answer[i]);
	}
	//delete nodes;
}

int main(void){
	solve();
	return 0;
}