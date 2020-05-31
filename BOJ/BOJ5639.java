package BOJ;

import java.util.Scanner;

class Node{
	Node left, right;
	int value;
	public Node(int value){
		this.value = value;
		this.left = null;
		this.right = null;
	}
	@Override
	public String toString(){
		return String.valueOf(this.value);
	}
}

class BinTree{
	Node root;

	public BinTree(){
		this.root = null;
	}

	public BinTree(Node root){
		this.root = root;
	}
	public BinTree(int value){
		this.root = new Node(value);
	}

	public void insert(int value){
		if(this.root == null){
			this.root = new Node(value);
			return;
		}
		Node cn = this.root;
		while(true){
			if(value < cn.value){
				if(cn.left != null){
					cn = cn.left;
				}
				else{
					cn.left = new Node(value);
					return;
				}
			}
			else{
				if(cn.right != null){
					cn = cn.right;
				}
				else{
					cn.right = new Node(value);
					return;
				}
			}
		}
	}

	public void printPostorder(){
		recurPo(this.root);
	}

	private void recurPo(Node n){
		if(n != null){
			recurPo(n.left);
			recurPo(n.right);
			System.out.println(n);
		}
	}
}

public class BOJ5639{

	public static void main(String[] args){
		BinTree bt = new BinTree();
		Scanner sc = new Scanner(System.in);
		String line;
		while(sc.hasNextLine()){
			line = sc.nextLine();
			bt.insert(Integer.parseInt(line));
		}
		bt.printPostorder();
		sc.close();
	}

}