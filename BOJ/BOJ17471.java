package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ17471 {

	static int N;
	static int[] population;
	static int totalPopulation, answer;
	static LinkedList<Integer>[] link;
	static int[] groupA;
	static int groupANum;
	static boolean[] visited;
	
	
	static HashSet<Integer> aSet = new HashSet<>();
	static Queue<Integer> q = new ArrayDeque<>();
	
	static void makeCombination(int num) {
		groupANum = num;
		makeCombination(0, 2);
	}
	
	static void makeCombination(int count, int start) {
		if(groupANum == count) {
			aSet.clear();
			aSet.add(1);
			for (int i = 0; i < groupANum; i++) {
				aSet.add(groupA[i]);
			}
			if(validateGroup()) {
				int sumA = 0;
				for (Integer integer : aSet) {
					sumA += population[integer];
				}
				answer = Math.min(answer, Math.abs(totalPopulation - sumA * 2));
			}
			return;
		}
		for (int i = start; i <= N-groupANum+count+1; i++) {
			groupA[count] = i;
			makeCombination(count+1, i+1);
		}
	}
	
	static boolean validateGroup() {
		int count = 1;
		int i;
		for (i = 1; i <= N; i++) {
			visited[i] = false;
		}
		q.offer(1);
		visited[1] = true;
		Iterator<Integer> li; 
		while(!q.isEmpty()) {
			int num = q.poll();
			li = link[num].iterator();
			while(li.hasNext()) {
				int next = li.next();
				if(!visited[next] && aSet.contains(next)) {
					q.offer(next);
					count ++;
				}
				visited[next] = true;
			}
		}
		if(count != aSet.size()) {
			return false;
		}
		
		for (i = 1; i <= N; i++) {
			visited[i] = false;
		}
		for (i = 1; i <= N; i++) {
			if(!aSet.contains(i)) {
				break;
			}
		}
		visited[i] = true;
		q.offer(i);
		count = 1;
		while(!q.isEmpty()) {
			int num = q.poll();
			li = link[num].iterator();
			while(li.hasNext()) {
				int next = li.next();
				if(!visited[next] && !aSet.contains(next)) {
					q.offer(next);
					count ++;
				}
				visited[next] = true;
			}
		}
		if(count != N - aSet.size()) {
			return false;
		}
		return true;
	}
	
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		population = new int[N+1];
		link = new LinkedList[N+1];
		groupA = new int[N];
		visited = new boolean[N+1];
		answer = Integer.MAX_VALUE;
		int i, j;
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(i = 1; i <= N; i++) {
			population[i] = Integer.parseInt(st.nextToken());
			totalPopulation += population[i];
			link[i] = new LinkedList<Integer>();
		}
		for (i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int adjCount = Integer.parseInt(st.nextToken());
			for (j = 0; j < adjCount; j++) {
				link[i].add(Integer.parseInt(st.nextToken()));
			}
		}
		for (i = 0; i < N-1; i++) {
			makeCombination(i);
		}
		System.out.println(answer==Integer.MAX_VALUE?-1:answer);
	}
	
}
