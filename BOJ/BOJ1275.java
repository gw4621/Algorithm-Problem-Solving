package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class SegTree{
	private long[] tree;
	private int firstNumIdx;
	public SegTree(int N, long[] numArr){
		this(N);
		int idx;
		for(int i=0;i<numArr.length;i++){
			idx = firstNumIdx + i;
			while(idx > 0){
				this.tree[idx] += numArr[i];
				idx >>= 1;
			}
		}
	}
	public SegTree(int N){
		int l = 1;
		while(l < N){
			l <<= 1;
		}
		firstNumIdx = l;
		l <<= 1;
		tree = new long[l];
	}

	public void update(int a, long b){
		int idx = firstNumIdx + a - 1;
		long diff = b - tree[idx];
		while(idx > 0){
			tree[idx] += diff;
			idx >>= 1;
		}
	}

	public long getSum(int start, int end){
		if(start <= end) return getSum(start, end, 1, 1, firstNumIdx);
		else return getSum(end, start, 1, 1, firstNumIdx);
	}

	public long getSum(int start, int end, int idx, int lo, int hi){
		if(start > hi || end < lo){
			return 0;
		}
		if(start <= lo && hi <= end){
			return this.tree[idx];
		}
		int mid = (lo + hi) / 2;
		return getSum(start, end, idx*2, lo, mid) + getSum(start, end, idx*2+1, mid+1, hi);
	}
	
	@Override
	public String toString(){
		StringBuilder builder = new StringBuilder();
		for(long i : tree){
			builder.append(i);
			builder.append(" ");
		}
		return builder.toString();
	}
}

public class BOJ1275 {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine().trim();
		String[] ls = line.split(" ");
		int N = Integer.parseInt(ls[0]), Q = Integer.parseInt(ls[1]);
		SegTree st = new SegTree(N);
		line = br.readLine().trim();
		ls = line.split(" ");
		int i;

		for(i=0;i<N;i++){
			st.update(i+1, Long.parseLong(ls[i]));
		}
		StringBuilder builder = new StringBuilder();
		for(i=0;i<Q;i++){
			line = br.readLine().trim();
			ls = line.split(" ");
			builder.append(st.getSum(Integer.parseInt(ls[0]), Integer.parseInt(ls[1])));
			builder.append('\n');
			st.update(Integer.parseInt(ls[2]), Long.parseLong(ls[3]));
		}
		br.close();
		System.out.println(builder.toString());
	}
}