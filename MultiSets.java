//	 _______________________________________________
//	|Created by Hurin                                       
//	|09/05/2017
//	|Copyright 2017 Iceloof All rights reserved                 
//	|_______________________________________________
// Multi sets list

import java.util.Arrays;
import java.util.Scanner;

public class MultiSets {

	private static Scanner scan;
	
	private static void list(int n, int k){
		int v[]=new int[k];
		for(int i=0;i<k;i++){
			v[i] = 0;
		}
		boolean Done = false;
		int i = n-1;
		while(!Done){
			i = n-1;
			while(i>=0){
				System.out.println(Arrays.toString(v));
				i --;
				if(v[k-1] < n-1){
					v[k-1] += 1;
				}else{
					for(int j=0;j<k;j++){
						if(v[j] == n-1&&j==0){
							Done = true;
							break;
						}
						if(v[j] == n-1&&j>0){
							if(v[j-1] < n-1){
								v[j-1] += 1;
								while(j<k){
									v[j] = v[j-1];
									j++;
								}
							}
						}
					}
				}
			}
		}
	}
	public static void main(String[] args) throws InterruptedException {
		scan = new Scanner(System.in);
		System.out.print("Input n: ");
		int n = scan.nextInt();
		System.out.print("Input k: ");
		int k = scan.nextInt();
		list(n, k);
	}

}
