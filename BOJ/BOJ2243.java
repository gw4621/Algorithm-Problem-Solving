package BOJ;

import java.util.Scanner;

public class BOJ2243{
	public static void update(int[] arr, int num, int quantity, int idx, int start, int end){
		arr[idx] += quantity;
		if(start != end){
			int mid = (start + end) / 2;
			if(num <= mid){
				update(arr, num, quantity, idx*2+1, start, mid);
			}
			else{
				update(arr, num, quantity, idx*2+2, mid+1, end);
			}
		}
	}
	public static int pop(int[] arr, int order, int idx, int start, int end){
		arr[idx] -= 1;
		if(start != end){
			int mid = (start+end) / 2;
			int left = idx*2+1;
			int right = idx*2+2;
			if(arr[left] < order){
				return pop(arr, order-arr[left], right, mid+1, end);
			}
			else{
				return pop(arr, order, left, start, mid);
			}
		}
		else{
			return start;
		}

	}

	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] command = new int[3];

		int[] arr = new int[2097152];

		for(int i=0;i<n;i++){
			command[0] = sc.nextInt();
			if(command[0] == 1){
				command[1] = sc.nextInt();
				System.out.println(pop(arr, command[1], 0, 1, 1000000));
			}
			else if(command[0] == 2){
				command[1] = sc.nextInt();
				command[2] = sc.nextInt();
				update(arr, command[1], command[2], 0, 1, 1000000);
			}
		}
		sc.close();
	}
}