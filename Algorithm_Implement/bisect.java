package Algorithm_Implement;

public class bisect {
	public static int bisect_left(int[] A, int num){
		return bisect_left(A, num, 0, A.length);
	}

	public static int bisect_left(int[] A, int num, int lo, int hi){
		while(lo < hi){
			int mid = (lo+hi) / 2;
			if(num > A[mid]) lo = mid+1;
			else hi = mid;
		}
		return hi;
	}

	public static int bisect_right(int[] A, int num){
		return bisect_right(A, num, 0, A.length);
	}

	public static int bisect_right(int[] A, int num, int lo, int hi){
		while(lo < hi){
			int mid = (lo+hi) / 2;
			if(num < A[mid]) hi = mid;
			else lo = mid+1;
		}
		return lo;
	}
}