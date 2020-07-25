package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ19235 {

	static class Block{
		short type;
		public Block(short type){
			this.type = type;
		}
		public Block(int type){
			this.type = (short)type;
		}
	}

	static int N;
	static int score;
	static Block[][] blue = new Block[6][4];
	static Block[][] green = new Block[6][4];
	public static void main(String[] args) throws IOException {
		int i, t, x, y;
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		score = 0;
		for(i=0;i<N;i++){
			st = new StringTokenizer(br.readLine());
			t = Integer.parseInt(st.nextToken());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			addBlockToBlue(t, x, y);
			addBlockToGreen(t, x, y);
			score += checkFullLineAndHandle(blue, (short)3);
			score += checkFullLineAndHandle(green, (short)2);
			checkCeilingAndHandle(blue, (short)3);
			checkCeilingAndHandle(green, (short)2);
		}
		br.close();
		System.out.println(score);
		System.out.println(countObj(blue) + countObj(green));
	}

	static void printArr(Block[][] arr){
		for(int i=0;i<6;i++){
			for(int j=0;j<4;j++){
				System.out.print(arr[i][j]==null?"0 ":arr[i][j].type==1?"1 ":Math.abs(arr[i][j].type)==2?"2 ":"3 ");
			}
			System.out.println();
		}
		System.out.println();
	}

	static int countObj(Object[][] arr){
		int ans = 0;
		for(Object[] a : arr){
			for(Object i : a){
				if(i != null){
					ans += 1;
				}
			}
		}
		return ans;
	}

	static void addBlockToBlue(int t, int x, int y){
		int i;
		boolean found = false;
		if(t == 1){
			for(i=0;i<6;i++){
				if(blue[i][x] != null){
					blue[i-1][x] = new Block(t);
					found = true;
					break;
				}
			}
			if(!found){
				blue[5][x] = new Block(t);
			}
		}
		else if(t == 2){
			for(i=0;i<6;i++){
				if(blue[i][x] != null){
					blue[i-1][x] = new Block(-t);
					blue[i-2][x] = new Block(t);
					found = true;
					break;
				}
			}
			if(!found){
				blue[4][x] = new Block(t);
				blue[5][x] = new Block(-t);
			}
		}
		else{
			for(i=0;i<6;i++){
				if(blue[i][x] != null || blue[i][x+1] != null){
					blue[i-1][x] = new Block(t);
					blue[i-1][x+1] = new Block(-t);
					found = true;
					break;
				}
			}
			if(!found){
				blue[5][x] = new Block(t);
				blue[5][x+1] = new Block(-t);
			}
		}
	}

	static void addBlockToGreen(int t, int x, int y){
		int i;
		boolean found = false;
		if(t == 1){
			for(i=0;i<6;i++){
				if(green[i][y] != null){
					green[i-1][y] = new Block(t);
					found = true;
					break;
				}
			}
			if(!found){
				green[5][y] = new Block(t);
			}
		}
		else if(t == 2){
			for(i=0;i<6;i++){
				if(green[i][y] != null || green[i][y+1] != null){
					green[i-1][y] = new Block(t);
					green[i-1][y+1] = new Block(-t);
					found = true;
					break;
				}
			}
			if(!found){
				green[5][y] = new Block(t);
				green[5][y+1] = new Block(-t);
			}
		}
		else{
			for(i=0;i<6;i++){
				if(green[i][y] != null){
					green[i-2][y] = new Block(t);
					green[i-1][y] = new Block(-t);
					found = true;
					break;
				}
			}
			if(!found){
				green[4][y] = new Block(t);
				green[5][y] = new Block(-t);
			}
		}
	}

	static int checkFullLineAndHandle(Block[][] arr, short axis){
		int i, j, k, ans = 0;
		boolean hasLine = false, isFull, found;
		for(i=0;i<6;i++){
			isFull = true;
			for(j=0;j<4;j++){
				if(arr[i][j] == null){
					isFull = false;
				}
			}
			if(!isFull){
				continue;
			}
			// If line i is Full
			hasLine = true;
			ans += 1;
			for(j=0;j<4;j++){
				if(arr[i][j].type == 1 || Math.abs(arr[i][j].type) == axis){
					arr[i][j] = null;
				}
				else{
					if(arr[i][j].type < 0){
						arr[i-1][j].type = 1;
					}
					else{
						arr[i+1][j].type = 1;
					}
					arr[i][j] = null;
				}
			}
		}
		for(i=4;i>=0;i--){
			for(j=0;j<4;j++){
				if(arr[i][j] == null) continue;
				if(arr[i][j].type == 1){
					found = false;
					if(arr[i+1][j] != null){
						continue;
					}
					for(k=i+2;k<6;k++){
						if(arr[k][j] != null){
							arr[k-1][j] = arr[i][j];
							arr[i][j] = null;
							found = true;
							break;
						}
					}
					if(!found){
						arr[5][j] = arr[i][j];
						arr[i][j] = null;
					}
				}
				else if(arr[i][j].type == axis){
					found = false;
					if(arr[i+1][j] != null || arr[i+1][j+1] != null){
						continue;
					}
					for(k=i+2;k<6;k++){
						if(arr[k][j] != null || arr[k][j+1] != null){
							arr[k-1][j] = arr[i][j];
							arr[k-1][j+1] = arr[i][j+1];
							arr[i][j] = null;
							arr[i][j+1] = null;
							found = true;
							break;
						}
					}
					if(!found){
						arr[5][j] = arr[i][j];
						arr[5][j+1] = arr[i][j+1];
						arr[i][j] = null;
						arr[i][j+1] = null;
					}
				}
				else if(arr[i][j].type < 0 && arr[i][j].type + axis != 0){
					found = false;
					if(arr[i+1][j] != null){
						continue;
					}
					for(k=i+2;k<6;k++){
						if(arr[k][j] != null){
							arr[k-1][j] = arr[i][j];
							arr[i][j] = null;
							arr[k-2][j] = arr[i-1][j];
							arr[i-1][j] = null;
							found = true;
							break;
						}
					}
					if(!found){
						arr[5][j] = arr[i][j];
						arr[i][j] = null;
						arr[4][j] = arr[i-1][j];
						arr[i-1][j] = null;
					}
				}
			}
		}

		if(hasLine){
			ans += checkFullLineAndHandle(arr, axis);
		}
		return ans;
	}

	static void checkCeilingAndHandle(Block[][] arr, short axis){
		int i, j, ceilLine = 0;
		for(i=0;i<2;i++){
			for(j=0;j<4;j++){
				if(arr[i][j] != null){
					ceilLine += 1;
					break;
				}
			}
		}
		if(ceilLine == 0) return;
		for(i=5-ceilLine;i>=2-ceilLine;i--){
			for(j=0;j<4;j++){
				arr[i+ceilLine][j] = arr[i][j];
			}
		}
		for(i=0;i<2;i++){
			for(j=0;j<4;j++){
				arr[i][j] = null;
			}
		}
		for(i=0;i<4;i++){
			if(arr[5][i] != null && arr[5][i].type > 0 && arr[5][i].type != axis){
				arr[5][i].type = 1;
			}
		}
	}
}