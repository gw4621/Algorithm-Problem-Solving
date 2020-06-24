package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ10875 {
	static int L, N, dir, x, y;
	static String[][] info;
	static final int UP = 0;
	static final int RIGHT = 1;
	static final int DOWN = 2;
	static final int LEFT = 3;
	static final int[] dx = {0, 1, 0, -1};
	static final int[] dy = {1, 0, -1, 0};
	static ArrayList<LineX> lx;
	static ArrayList<LineY> ly;

	static class LineX{
		int x, start, end;
		public LineX(int x, int start, int end){
			this.x = x;
			if(start > end){
				this.start = end;
				this.end = start;
			}
			else{
				this.start = start;
				this.end = end;
			}
		}
	}

	static class LineY{
		int y, start, end;
		public LineY(int y, int start, int end){
			this.y = y;
			if(start > end){
				this.start = end;
				this.end = start;
			}
			else{
				this.start = start;
				this.end = end;
			}
		}
	}

	static int getMin(int a, int b){
		return a>b?b:a;
	}

	static int getMaxStop(){
		int maxStop = Integer.MAX_VALUE;
		if(dir == RIGHT){
			for(LineX clx : lx){
				if(clx.start <= y && y <= clx.end && x < clx.x){
					maxStop = getMin(maxStop, clx.x - x);
				}
			}
			for(LineY cly : ly){
				if(cly.y == y && cly.start > x){
					maxStop = getMin(maxStop, cly.start - x);
				}
			}
		}
		else if(dir == LEFT){
			for(LineX clx : lx){
				if(clx.start <= y && y <= clx.end && x > clx.x){
					maxStop = getMin(maxStop, x - clx.x);
				}
			}
			for(LineY cly : ly){
				if(cly.y == y && cly.end < x){
					maxStop = getMin(maxStop, x - cly.end);
				}
			}
		}
		else if(dir == UP){
			for(LineX clx : lx){
				if(clx.x == x && clx.start > y){
					maxStop = getMin(maxStop, clx.start - y);
				}
			}
			for(LineY cly : ly){
				if(cly.start <= x && x <= cly.end && cly.y > y){
					maxStop = getMin(maxStop, cly.y - y);
				}
			}
		}
		else if(dir == DOWN){
			for(LineX clx : lx){
				if(clx.x == x && clx.end < y){
					maxStop = getMin(maxStop, y - clx.end);
				}
			}
			for(LineY cly : ly){
				if(cly.start <= x && x <= cly.end && y > cly.y){
					maxStop = getMin(maxStop, y - cly.y);
				}
			}
		}
		return maxStop;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		L = Integer.parseInt(br.readLine());
		N = Integer.parseInt(br.readLine());
		info = new String[N][2];
		int i;
		StringTokenizer st;
		for(i=0;i<N;i++){
			st = new StringTokenizer(br.readLine());
			info[i][0] = st.nextToken();
			info[i][1] = st.nextToken();
		}
		br.close();
		lx = new ArrayList<>();
		ly = new ArrayList<>();
		lx.add(new LineX(-L-1, -L, L));
		lx.add(new LineX(L+1, -L, L));
		ly.add(new LineY(-L-1, -L, L));
		ly.add(new LineY(L+1, -L, L));
		dir = RIGHT;
		x = 0;
		y = 0;
		int maxStop, timeLimit, newX, newY;
		long totalTime = 0;

		for(i=0;i<N;i++){
			maxStop = getMaxStop();
			timeLimit = Integer.parseInt(info[i][0]);

			if(maxStop <= timeLimit){
				totalTime += maxStop;
				System.out.println(totalTime);
				return;
			}

			totalTime += timeLimit;
			if((dir & 1) > 0){	// LEFT or RIGHGT
				newX = x + dx[dir] * timeLimit;
				ly.add(new LineY(y, x, newX));
				x = newX;
			}
			else{	// UP or DOWN
				newY = y + dy[dir] * timeLimit;	
				lx.add(new LineX(x, y, newY));
				y = newY;
			}
			if(info[i][1].equals("L")) dir = (dir+3) % 4;
			else dir = (dir + 1) % 4;
		}
		maxStop = getMaxStop();
		totalTime += maxStop;
		System.out.println(totalTime);
		return;
	}
}