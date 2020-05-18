package BOJ;

import java.util.Scanner;

class BF {	// Bellman-Ford
	private int N, M;
	private int[][] busInfo;
	BF(int N, int M, int[][] busInfo){
		this.N = N;
		this.M = M;
		this.busInfo = busInfo;
	}
	public long[] solve(){
		int i, j;
		long[] distArr = new long[N+1];
		
		for(i=2;i<N+1;i++){
			distArr[i] = Long.MAX_VALUE;
		}
		int start, end, dist;
		for(i=0;i<N-1;i++){
			for(j=0;j<M;j++){
				start = busInfo[j][0];
				end = busInfo[j][1];
				dist = busInfo[j][2];
				if(distArr[start] != Long.MAX_VALUE){
					distArr[end] = Math.min(distArr[end], distArr[start] + dist);
				}
			}
		}
		for(i=0;i<M;i++){
			start = busInfo[i][0];
			end = busInfo[i][1];
			dist = busInfo[i][2];
			if(distArr[start] != Long.MAX_VALUE && Math.min(distArr[end], distArr[start]+dist) != distArr[end]){
				distArr[0] = -1;
				return distArr;
			}
		}
		for(i=1;i<N+1;i++){
			if(distArr[i] == Long.MAX_VALUE){
				distArr[i] = -1;
			}
		}
		return distArr;
	}
}

public class BOJ11659 {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N, M, i, j;
		N = sc.nextInt();
		M = sc.nextInt();
		int[][] busInfo = new int[M][3];
		for(i=0;i<M;i++){
			for(j=0;j<3;j++){
				busInfo[i][j] = sc.nextInt();
			}
		}
		sc.close();
		BF bf = new BF(N, M, busInfo);
		long[] ans = bf.solve();
		if(ans[0] < 0){
			System.out.println(-1);	
		}
		else{
			for(i=2;i<N+1;i++){
				System.out.println(ans[i]);
			}
		}
	}
}