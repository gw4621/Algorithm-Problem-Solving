package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class BOJ16985 {
	
	static char[][][] maze = new char[5][][];
	
	static char[][][][] board = new char[5][4][5][];
	
	static boolean[] visited = new boolean[5];
	static boolean[][][] bfsV = new boolean[5][5][5];
	static int answer = Integer.MAX_VALUE;
	
	
	static Queue<Point> q = new ArrayDeque<>();
	
	static class Point {
		int i, j, k;

		public Point(int i, int j, int k) {
			super();
			this.i = i;
			this.j = j;
			this.k = k;
		}

		@Override
		public String toString() {
			return "(" + i + ", " + j + ", " + k + ")";
		}
		
		
	}
	
	static void bfs() {
		if(maze[0][0][0] == '0' || maze[4][4][4] == '0') return;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				for (int k = 0; k < 5; k++) {
					bfsV[i][j][k] = false;
				}
			}
		}
		q.clear();
		q.offer(new Point(0, 0, 0));
		bfsV[0][0][0] = true;
		int move = 0;
		while(!q.isEmpty()) {
			int qSize = q.size();
			move ++;
			for (int i = 0; i < qSize; i++) {
				Point p = q.poll();
				int ni = p.i-1;
				if(ni >= 0 && maze[ni][p.j][p.k] == '1' && !bfsV[ni][p.j][p.k]) {
					bfsV[ni][p.j][p.k] = true; 
					q.offer(new Point(ni, p.j, p.k));
				}
				ni = p.i+1;
				if(ni < 5 && maze[ni][p.j][p.k] == '1' && !bfsV[ni][p.j][p.k]) {
					if(ni == 4 && p.j == 4 && p.k == 4) {
						answer = Math.min(answer, move);
						return;
					}
					bfsV[ni][p.j][p.k] = true; 
					q.offer(new Point(ni, p.j, p.k));
				}
				int nj = p.j-1;
				if(nj >= 0 && maze[p.i][nj][p.k] == '1' && !bfsV[p.i][nj][p.k]) {
					bfsV[p.i][nj][p.k] = true;
					q.offer(new Point(p.i, nj, p.k));
				}
				nj = p.j+1;
				if(nj < 5 && maze[p.i][nj][p.k] == '1' && !bfsV[p.i][nj][p.k]) {
					if(p.i == 4 && nj == 4 && p.k == 4) {
						answer = Math.min(answer, move);
						return;
					}
					bfsV[p.i][nj][p.k] = true;
					q.offer(new Point(p.i, nj, p.k));
				}
				int nk = p.k - 1;
				if(nk >= 0 && maze[p.i][p.j][nk] == '1' && !bfsV[p.i][p.j][nk]) {
					bfsV[p.i][p.j][nk] = true;
					q.offer(new Point(p.i, p.j, nk));
				}
				nk = p.k + 1;
				if(nk < 5 && maze[p.i][p.j][nk] == '1' && !bfsV[p.i][p.j][nk]) {
					if(p.i == 4 && p.j == 4 && nk == 4) {
						answer = Math.min(answer, move);
						return;
					}
					bfsV[p.i][p.j][nk] = true;
					q.offer(new Point(p.i, p.j, nk));
				}
			}
		}
		
	}
	
	static void permutation(int r) {
		if(r == 5) {
			bfs();
			return;
		}
		for (int i = 0; i < 5; i++) {
			if(!visited[i]) {
				visited[i] = true;
				for (int j = 0; j < 4; j++) {
					maze[r] = board[i][j];
					permutation(r+1);
				}
				visited[i] = false;
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				board[i][0][j] = br.readLine().replace(" ", "").trim().toCharArray();
				for (int k = 1; k < 4; k++) {
					board[i][k][j] = new char[5];
				}
			}
			for (int j = 1; j < 4; j++) {
				for (int k = 0; k < 5; k++) {
					for (int k2 = 0; k2 < 5; k2++) {
						board[i][j][k][k2] = board[i][j-1][4-k2][k];
					}
				}
			}
		}
		
		permutation(0);
		
		System.out.println(answer==Integer.MAX_VALUE?-1:answer);
		
		
	}
	
	
}
