package incomplete;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ3830 {
	
	final static int MAX_SP = 100001;
	static int[] parent = new int[MAX_SP];
	static long[] wd = new long[MAX_SP];
	static int N, M;
	
	
	static int getParent(int num){
		if(num == parent[num]){
			return num;
		}
		int realPar = getParent(parent[num]);
		wd[num] += wd[parent[num]];
		parent[num] = realPar;
		return parent[num];
	}

	static String query(int a, int b){
		int parA = getParent(a);
		int parB = getParent(b);
		if(parA != parB){
			return "UNKNOWN";
		}
		return String.valueOf(wd[b] - wd[a]);
	}
	
	static void merge(int a, int b, int c){
		int parA = getParent(a);
		int parB = getParent(b);
		if(parA == parB){
			return;
		}
		parent[parB] = parA;
		wd[parB] = c + wd[a] - wd[b];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int i, a, b, w;
		while(true){
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			if(N + M == 0){
				break;
			}
			for(i=0;i<=N;i++){
				parent[i] = i;
				wd[i] = 0;
			}

			for(i=0;i<M;i++){
				st = new StringTokenizer(br.readLine());
				if("!".equals(st.nextToken())){
					a = Integer.parseInt(st.nextToken());
					b = Integer.parseInt(st.nextToken());
					w = Integer.parseInt(st.nextToken());
					merge(a, b, w);
				}
				else{
					a = Integer.parseInt(st.nextToken());
					b = Integer.parseInt(st.nextToken());
					System.out.println(query(a, b));
				}
			} // for end
		} // while end
	} // main end
} // class end