//     _______________________________________________
//    |Created by Hurin                                       
//    |09/05/2017
//    |Copyright 2017 Iceloof All rights reserved                 
//    |_______________________________________________
// Rank and Unrank for colex order of subsets
import java.util.Arrays;
import java.util.Scanner;
import java.util.Vector;

public class SubsetRanking {
    private static Scanner scan;
    
    private static int fact(int n){
       int result;
       if(n < 2){
           return 1;
       }
       result = fact(n-1) * n;
       return result;
    }

    private static int rank(Vector<Integer> Perm) {
        int R = 0;
        int fact = 0;
        Integer[] array = {};
        Vector<Integer> Perm1 = new Vector<Integer>(Arrays.asList(array));
        for(int i = 0; i < Perm.size(); i ++){
            if(Perm.get(i)==1){
                R = R + 1;
            }else{
                fact = fact(Perm.get(i) - 1)/(fact(i + 1) * fact(Perm.get(i) - i - 2));
                R = R + fact;
            }
            System.out.println("Rank(" + Perm1 + ") +  (" + (Perm.get(i) - 1) + "," + (i+1) + ")[" + fact + "] = " + R);
            Perm1.add(Perm.get(i));
        }
        return R;
    }

    private static Vector<Integer> unrank(int length, int n, int rank, Vector<Integer> Perm) {
        int R = rank;
        int p,fact;
        for(int i = 0; i < length; i ++){
            Perm.add(i, 0);
        }
        System.out.println(Perm);
        for(int i = length; i > 0 ; i --){
            p = i-1;
            do{
                p = p + 1;
                fact = fact(p)/(fact(i) * fact(p- i));
            }while(fact <= R && p <= n);
            fact = fact(p-1)/(fact(i) * fact(p- 1 - i));
            R = R - fact;
            System.out.println("P: " + p + " \t R: " + R + " \t Value: " + p + " \t Permutation index: " + i);
            Perm.set(i-1, p);
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
            System.out.print("Please input subset length: ");
            int length = scan.nextInt();
            System.out.print("Please input range: ");
            int n = scan.nextInt();
            System.out.print("Please input rank: ");
            int rank = scan.nextInt();
            Perm = unrank(length,n,rank,Perm);
            System.out.println("Permutation: " + Perm);
        }
    }
}

