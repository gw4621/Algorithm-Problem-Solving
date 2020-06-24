package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ3176 {

	static class Link{
		int dest, len;
		public Link(int dest, int len){
			this.dest = dest;
			this.len = len;
		}
	}
	
	static int maxLevel;
	static List<List<Link>> G;
	static int[][] ancestor, minLen, maxLen;
	static int[] depth;
	static int N, K;
	static int ansMin, ansMax;

	static int getMin(int a, int b, int c){
		return getMin(getMin(a, b), c);
	}
	static int getMax(int a, int b, int c){
		return getMax(getMax(a, b), c);
	}
	static int getMin(int a, int b){
		return a>b?b:a;
	}
	static int getMax(int a, int b){
		return a>b?a:b;
	}

	static void lca(int a, int b){
		int tmp, i;
		if(depth[a] > depth[b]){
			tmp = a;
			a = b;
			b = tmp;
		}
		int depthDiff = depth[b] - depth[a];
		ansMin = minLen[b][0];
		ansMax = maxLen[b][0];
		for(i=maxLevel-1;i>=0;i--){
			tmp = 1 << i;
			if((tmp&depthDiff) == tmp){
				depthDiff -= tmp;
				ansMin = getMin(ansMin, minLen[b][i]);
				ansMax = getMax(ansMax, maxLen[b][i]);
				b = ancestor[b][i];
			}
		}
		if(a == b) return;
		for(i=maxLevel-1;i>=0;i--){
			if(ancestor[a][i] != ancestor[b][i]){
				ansMin = getMin(ansMin, minLen[a][i], minLen[b][i]);
				ansMax = getMax(ansMax, maxLen[a][i], maxLen[b][i]);
				a = ancestor[a][i];
				b = ancestor[b][i];
			}
		}
		ansMin = getMin(ansMin, minLen[a][0], minLen[b][0]);
		ansMax = getMax(ansMax, maxLen[a][0], maxLen[b][0]);
	}

	static void setAncestor(int parent, int child, int len){
		int i;
		depth[child] = depth[parent] + 1;
		ancestor[child][0] = parent;
		minLen[child][0] = len;
		maxLen[child][0] = len;
		for(i=1;i<maxLevel;i++){
			ancestor[child][i] = ancestor[ancestor[child][i-1]][i-1];
			minLen[child][i] = getMin(minLen[child][i-1], minLen[ancestor[child][i-1]][i-1]);
			maxLen[child][i] = getMax(maxLen[child][i-1], maxLen[ancestor[child][i-1]][i-1]);
		}
		for(Link l : G.get(child)){
			if(l.dest != parent){
				setAncestor(child, l.dest, l.len);
			}
		}
	}

	static void setMaxLevel(){
		int tmp = 1;
		maxLevel = 1;
		while(tmp < N){
			maxLevel += 1;
			tmp <<= 1;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int i, a, b, c;
		N = Integer.parseInt(bf.readLine());
		setMaxLevel();
		G = new ArrayList<>(N+1);
		depth = new int[N+1];
		ancestor = new int[N+1][maxLevel];
		minLen = new int[N+1][maxLevel];
		maxLen = new int[N+1][maxLevel];
		for(i=0;i<N+1;i++){
			G.add(new ArrayList<>());
		}
		for(i=0;i<N-1;i++){
			st = new StringTokenizer(bf.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			G.get(a).add(new Link(b, c));
			G.get(b).add(new Link(a, c));
		}
		
		setAncestor(0, 1, 0);

		K = Integer.parseInt(bf.readLine());
		for(i=0;i<K;i++){
			st = new StringTokenizer(bf.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			lca(a, b);
			System.out.printf("%d %d\n", ansMin, ansMax);
		}
		bf.close();
	}

}