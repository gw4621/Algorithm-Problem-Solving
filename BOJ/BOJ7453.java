package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ7453{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int i, j;
		int[][] nums = new int[4][n];
		for(i=0;i<n;i++){
			for(j=0;j<4;j++){
				nums[j][i] = sc.nextInt();
			}
		}
		int[] A = new int[n*n];
		int[] B = new int[n*n];
		int idx = 0;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				A[idx] = nums[0][i] + nums[1][j];
				B[idx] = nums[2][i] + nums[3][j];
				idx ++;
			}
		}
		Arrays.sort(B);
		long answer = 0;
		for(int a : A){
			answer += bisect_right(B, -a) - bisect_left(B, -a);
		}
		System.out.println(answer);
	}

	private static int bisect_left(int[] A, int num){
		return bisect_left(A, num, 0, A.length);
	}

	private static int bisect_left(int[] A, int num, int lo, int hi){
		while(lo < hi){
			int mid = (lo+hi) / 2;
			if(num > A[mid]) lo = mid+1;
			else hi = mid;
		}
		return hi;
	}

	private static int bisect_right(int[] A, int num){
		return bisect_right(A, num, 0, A.length);
	}

	private static int bisect_right(int[] A, int num, int lo, int hi){
		while(lo < hi){
			int mid = (lo+hi) / 2;
			if(num < A[mid]) hi = mid;
			else lo = mid+1;
		}
		return lo;
	}
}