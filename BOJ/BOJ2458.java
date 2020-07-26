package incomplete;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2458{

	static int N, M;
	static int[][] con = new int[501][501];	// current connection

	static int solve(){
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				for (int k = 1; k <= N; k++) {
					if(con[j][k] == 0 && con[j][i] != 0 && con[j][i] == con[i][k]){
						con[j][k] = con[j][i];
					}
				}
			}
		}
		int count = 0;
		boolean isConnected;
		for(int i = 1; i <= N; i++){
			isConnected = true;
			for(int j = 1; j <= N; j++){
				if(i != j && con[i][j] == 0){
					isConnected = false;
					break;
				}
			}
			if(isConnected){
				count += 1;
			}
		}
		return count;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int a, b;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			con[a][b] = 1;
			con[b][a] = -1;
		}
		System.out.println(solve());/*
		for(int i=1;i<=N;i++){
			int[] show = new int[N];
			System.arraycopy(con[i], 1, show, 0, N);
			System.out.println(Arrays.toString(show));
		}*/
		br.close();
	}
}