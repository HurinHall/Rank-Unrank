//	 _______________________________________________
//	|Created by Hurin                                       
//	|09/05/2017
//	|Copyright 2017 Iceloof All rights reserved                 
//	|_______________________________________________
// Rank and Unrank based on Johnson-Trotter algorithm
import java.util.Arrays;
import java.util.Scanner;
import java.util.Vector;

public class JTRanking {
	private static Scanner scan;
	
	private static int rank(Vector<Integer> Perm){
		Integer[] array = {};
		Vector<Integer> Perm1 = new Vector<Integer>(Arrays.asList(array));
		int n = Perm.size();
	    if(n == 1){
	    	return 0;
	    }
	    int j = 0;
		for(int i = 0;i < n;i ++){
			if(Perm.get(i) != n){
				Perm1.add(Perm.get(i));
			}else{
				j = i;
			}
		}
		int R = rank(Perm1);
		if(R % 2 == 1){
			System.out.println("Rank:" + R + " \t Permutation: " + Perm1);
			return R * n  + j;
		}else{
			System.out.println("Rank:" + R + " \t Permutation: " + Perm1);
			return R * n + n - j - 1;
		}
	}
	
	private static Vector<Integer> unrank(int n, int rank, Vector<Integer> Perm) {
		for(int i=0;i<n;i++){
			Perm.add(0);
		}
		int k,R,Dir,C;
		int P = rank;
		for(int j = n;j > 0;j --){
			R = P % j;
			P = P/j;
			if(P%2 == 1){
				k = 0;
				Dir = 1;
			}else{
				k = n + 1;
				Dir = -1;
			}
			C = 0;
			do{
				k = k + Dir;
				if(Perm.get(k-1) == 0){
					C = C + 1;
				}
			}while(C != R + 1);
			System.out.println("Value: " + j + " \t Permutation index: " + (k-1));
			Perm.set(k-1, j);
		}
		return Perm;
	}
	
	public static void main(String[] args) {
		Integer[] array = {};
		Vector<Integer> Perm = new Vector<Integer>(Arrays.asList(array));
		scan = new Scanner(System.in);
		System.out.println("Please choose ");
		System.out.println("1. Ranking");
		System.out.println("2. Unranking");
		System.out.print("Your choice: ");
		int choice = scan.nextInt();
		if(choice == 1){
			scan.nextLine();
			System.out.print("Please input permutation(space between number): ");
			String s = scan.nextLine();
			String split[] = s.split(" ");
			for(int i=0;i<split.length;i++){
				Perm.add(Integer.parseInt(split[i]));
			}
			int rank = rank(Perm);
			System.out.println("Rank:" + rank + " \t Permutation: " + Perm);
		}else{
			System.out.print("Please input range: ");
			int n = scan.nextInt();
			System.out.print("Please input rank: ");
			int rank = scan.nextInt();
			Perm = unrank(n,rank,Perm);
			System.out.println("Permutation: " + Perm);
		}
	}
}
