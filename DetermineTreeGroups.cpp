//	 _______________________________________________
//	|Created by Hurin                                       
//	|21/05/2017
//	|Copyright 2017 Iceloof All rights reserved                 
//	|_______________________________________________
// Determine Tree Groups

#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

const int HASH = 2333;
const int size_k = 102;
const int size_n = 1002;

struct Tree{
	int size;
	int sucNum;
	vector<Tree*> sucs;
	int dep;
	int hash_value;
	
	void gethash(){
		hash_value = 0;
		for(int i = 0; i < sucNum; i++){
			sucs[i]->gethash();
			hash_value += sucs[i]->hash_value;
		}
		hash_value += size*size + dep*dep + sucNum*sucNum;
		hash_value %= HASH;
	}
	
	void getdep(){
		if(!sucNum) {
			dep = 0;
			return;
		}
		dep = 0;
		for(int i = 0; i < sucNum; i++){
			sucs[i]->getdep();
			if(dep < sucs[i]->dep) dep = sucs[i]->dep;
		}
		dep++;
	}
	
	void getSize(){
		size = 0;
		for(int i = 0; i < sucNum; i++){
			sucs[i]->getSize();
			size += sucs[i]->size;
		}
		size ++;
	}
	
	void getsuc(){
		sucNum = sucs.size();
		for(int i = 0; i < sucNum; i++){
			sucs[i]->getsuc();
		}
	}
};

bool isIsomph(Tree *t1, Tree *t2){
	if(t1->hash_value != t2->hash_value || t1->dep != t2->dep || t1->sucNum != t2->sucNum || t1->size != t2->size){
		return false;
	}
	
	bool visited[size_k] = {0};
	
	for(int i = 0; i < t1->sucNum; i++){
		int offset = 0;
		for(; offset < t1->sucNum; offset++){
			if(isIsomph(t1->sucs[i], t2->sucs[offset]) && !visited[offset]){
				visited[offset] = true;
				break;
			}
		}
		if(offset == t1->sucNum){
			return false;
		} 
	}
	return true;
}

void setTree(int adj_node[size_n], int adj_list[size_n][size_n], Tree *tree, int root){
	if(!adj_node[root]){
		return;
	}
	for(int i = 0; i < adj_node[root]; i++){
		Tree *temp = new Tree;
		tree->sucs.push_back(temp);
		setTree(adj_node, adj_list, temp, adj_list[root][i]);
	}
}

int main(int argc, char *argv[]){
	
	int k,n;
	scanf("%d",&k);
	int index = 0;
	int id_index[size_n*2]={0};
	int position[size_n*2]={0};
	vector<int> table[HASH];
	
	while(k!=0){
		
		Tree trees[size_n+2];
		
		for(int i = 1; i <= k; i++){
			
			scanf("%d", &n);
			int adj_node[size_n] = {0};
			int adj_list[size_n][size_n];
			bool bei[size_n] = {0};
			
			for(int j = 0; j < n; j++){
				int a, b;
				scanf("%d", &a);
				a += 2;
				adj_list[a][adj_node[a]] = j+2;
				adj_node[a]++;
				bei[j+2] = 1;
			}
			
			int root = 1;
			for(; root <= n && bei[root]; root++);
			setTree(adj_node, adj_list, &trees[i], root);
			
			trees[i].getsuc();
			trees[i].getSize();
			trees[i].getdep();
			trees[i].gethash();
			
			id_index[i] = trees[i].hash_value;
			position[i] = table[id_index[i]].size();
			table[id_index[i]].push_back(i);
		}
		
		bool visited[size_n*2] = {0};
		int result[k];
		int count = 0;
		printf("%d:",index);
		
		for(int i = 1; i <= k; i++){
			
			if(visited[i]){
				continue;
			}
			
			visited[i] = 1;
			result[i-1] = count;
			int hash = table[id_index[i]].size();
			
			for(int j = position[i]+1; j < hash; j++){
				int d = table[id_index[i]][j];
				if(visited[d]) continue;
				if(isIsomph(&trees[i], &trees[d])){
					visited[d] = 1;
					result[d-1] = result[i-1];
				}
			}
			
			count ++;
		}
		
		for(int i=0;i<k;i++){
			printf(" %d",result[i]);
		}
		printf("\n");
		
		index ++;
		scanf("%d",&k);
	}
	return 0;
}