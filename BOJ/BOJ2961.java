package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2961 {

	static int N;
	
	static int[][] ingredient;
	
	static int answer;
	
	// Add Ingredient, one by one.
	static void addIngredient(int i, int sour, int bitter) {
		int nextSour = sour * ingredient[0][i];
		int nextBitter = bitter + ingredient[1][i];
		answer = Math.min(answer, Math.abs(nextSour-nextBitter));
		for (int j = i + 1; j < N; j++) {
			addIngredient(j, nextSour, nextBitter);
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		ingredient = new int[2][N];
		
		answer = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			ingredient[0][i] = Integer.parseInt(st.nextToken());
			ingredient[1][i] = Integer.parseInt(st.nextToken());
		}
		
		// Recursive Ingredient Adding
		for (int i = 0; i < N; i++) {
			addIngredient(i, 1, 0);			
		}
		
		System.out.println(answer);
		
	}
	
}
