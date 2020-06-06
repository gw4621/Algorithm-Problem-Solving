package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ2094 {
	static final int TRUE = 2;
	static final int MAYBE = 1;
	static final int FALSE = 0;
	static final int UNKNOWN = -1;

	public static int getResult(Map<Integer, Integer> y_rain, int[] yArr, int X, int Y){
		Integer Xrain = y_rain.get(Integer.valueOf(X)), Yrain = y_rain.get(Integer.valueOf(Y));
		if(Xrain == null && Yrain == null){
			return MAYBE;
		}
		int Xidx = bisect_left(yArr, X), Yidx = bisect_left(yArr, Y);
		int i;
		if(Xrain == null){
			for(i=Yidx+1;i<Xidx;i++){
				if(y_rain.get(Integer.valueOf(yArr[i])) >= Yrain){
					return FALSE;
				}
			}
			return MAYBE;
		}
		else if(Yrain == null){
			for(i=Yidx;i<Xidx;i++){
				if(y_rain.get(Integer.valueOf(yArr[i])) >= Xrain){
					return FALSE;
				}
			}
			return MAYBE;
		}
		else{
			if(Xrain > Yrain) return FALSE;
			for(i=Yidx+1;i<Xidx;i++){
				if(y_rain.get(Integer.valueOf(yArr[i])) >= Xrain){
					return FALSE;
				}
			}
			if(Xidx - Yidx == X - Y){
				return TRUE;
			}
			return MAYBE;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		Map<Integer, Integer> y_rain = new HashMap<>();
		int n = Integer.parseInt(br.readLine().trim());
		int i, y;
		int[] yArr = new int[n];
		int idx = 0;
		for(i=0;i<n;i++){
			st = new StringTokenizer(br.readLine().trim(), " ");
			y = Integer.parseInt(st.nextToken());
			y_rain.put(Integer.valueOf(y), Integer.valueOf(st.nextToken()));
			yArr[idx] = y;
			idx += 1;
		}
		Arrays.sort(yArr);
		int m = Integer.parseInt(br.readLine().trim());
		int X, Y;
		int result;
		StringBuilder sb = new StringBuilder();
		for(i=0;i<m;i++){
			st = new StringTokenizer(br.readLine().trim(), " ");
			Y = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			result = getResult(y_rain, yArr, X, Y);
			if(result == MAYBE){
				sb.append("maybe");
			}
			else if(result == TRUE){
				sb.append("true");
			}
			else if(result == FALSE){
				sb.append("false");
			}
			else if(result == UNKNOWN){
				System.out.println("Something's wrong");
				return;
			}
			sb.append("\n");
		}
		br.close();
		System.out.print(sb.toString());
	}

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
}