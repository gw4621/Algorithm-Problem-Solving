package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ12094 {
	
	private static final char UP = 0;
	private static final char DOWN = 1;
	private static final char LEFT = 2;
	private static final char RIGHT = 3;

	private static BufferedReader br;
	private static int N;

	private static void getBoard(int[][] board) throws IOException {
		StringTokenizer st;
		int i, j;
		for(i=0;i<N;i++){
			st = new StringTokenizer(br.readLine());
			for(j=0;j<N;j++){
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}

	private static void moveLeft(int[][] board){
		int i, j;
		int[] line = new int[N];
		int lSize;
		boolean merged;
		for(i=0;i<N;i++){
			lSize = 0;
			merged = false;
			for(j=0;j<N;j++){
				if(board[i][j] != 0){
					if(lSize > 0 && !merged && line[lSize-1] == board[i][j]){
						line[lSize-1] <<= 1;
						merged = true;
					}
					else{
						line[lSize] = board[i][j];
						lSize ++;
						merged = false;
					}
					board[i][j] = 0;
				}
			}
			for(j=0;j<lSize;j++){
				board[i][j] = line[j];
				line[j] = 0;
			}
		}
	}

	/*private static void printBoard(int[][] board){	// For debugging
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				sb.append(board[i][j]);
				sb.append(' ');
			}
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}*/

	private static int[][] move(int[][] board, char direction){
		int i, j, tmp;
		int[][] newBoard;
		switch(direction){
			case UP:
				newBoard = new int[N][N];
				for(i=0;i<N;i++){
					for(j=0;j<N;j++){
						newBoard[i][j] = board[j][i];
					}
				}
				moveLeft(newBoard);
				for(i=1;i<N;i++){
					for(j=0;j<i;j++){
						tmp = newBoard[i][j];
						newBoard[i][j] = newBoard[j][i];
						newBoard[j][i] = tmp;
					}
				}
				return newBoard;
			case DOWN:
				newBoard = new int[N][N];
				for(i=0;i<N;i++){
					for(j=0;j<N;j++){
						newBoard[i][j] = board[N-1-j][N-1-i];
					}
				}
				moveLeft(newBoard);
				for(i=0;i<N-1;i++){
					for(j=0;j<N-i-1;j++){
						tmp = newBoard[i][j];
						newBoard[i][j] = newBoard[N-1-j][N-1-i];
						newBoard[N-1-j][N-1-i] = tmp;
					}
				}
				return newBoard;
			case LEFT:
				newBoard = new int[N][];
				for(i=0;i<N;i++){
					newBoard[i] = board[i].clone();
				}
				moveLeft(newBoard);
				return newBoard;
			case RIGHT:
				newBoard = new int[N][N];
				for(i=0;i<N;i++){
					for(j=0;j<N;j++){
						newBoard[i][j] = board[i][N-1-j];
					}
				}
				moveLeft(newBoard);
				for(i=0;i<N;i++){
					for(j=0;j<N/2;j++){
						tmp = newBoard[i][j];
						newBoard[i][j] = newBoard[i][N-1-j];
						newBoard[i][N-1-j] = tmp;
					}
				}
				return newBoard;
		}
		return null;
	}

	private static int getMax(int[][] board){
		int i, j;
		int maxNum = 0;
		for(i=0;i<N;i++)
			for(j=0;j<N;j++)
				if(board[i][j] > maxNum)	maxNum = board[i][j];
		return maxNum;
	}

	private static int getMax(int a, int b){
		if(a>b) return a;
		return b;
	}

	private static int dfs(int[][] board, int level){
		if(level == 10){
			return getMax(board);
		}
		int maxNum = 0;
		maxNum = getMax(maxNum, dfs(move(board, UP), level+1));
		maxNum = getMax(maxNum, dfs(move(board, DOWN), level+1));
		maxNum = getMax(maxNum, dfs(move(board, LEFT), level+1));
		maxNum = getMax(maxNum, dfs(move(board, RIGHT), level+1));
		return maxNum;
	}

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int[][] board;
		N = Integer.parseInt(br.readLine().trim());
		board = new int[N][N];
		getBoard(board);
		br.close();
		System.out.println(dfs(board, 0));
	}
}