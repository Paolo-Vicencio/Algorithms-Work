#include <iostream>
#include <vector>
#include <chrono>

#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

#include <algorithm>
#include <ctime>
#include <random>

using namespace std;
using namespace std::chrono;


void insertionSort(vector<int> &list, int start, int end);
void quickSort(vector<int> &list, int i, int j, int minSize);
int partition(vector<int> &list, int p, int r);

int main() {
	// vector<int> insertVec;
	// vector<int> quickVec;

	// srand((unsigned)time(NULL));
	// int a = 1000; //1 to 20    
	// for (int i = 0; i < a; i++){
 //        int b = rand() % 1000000 + 1;
 //        insertVec.push_back(b);
 //        quickVec.push_back(b);
 //    }

	// // insertionSort(insertVec, 0, insertVec.size()-1);
	// // // for (int i =0; i < insertVec.size(); i++) {
	// // // 	cout << insertVec[i] << " " ;
	// // // }

	// insertionSort(quickVec, 0, quickVec.size()-1);
	// insertionSort(insertVec, 0, insertVec.size()-1);

 //    // for (int i = 0; i < quickVec.size(); i++) {
 //    // 	cout << quickVec[i] << " ";
 //    // }

 //    cout << " " << endl; 
    
 //    // Almost sorted lists

 //    // quick sort
 // //    int deez = 0;
 // //    for (int i = 0; i < 100; i++) {
 // //    	random_shuffle(quickVec.begin() + deez, quickVec.begin() + deez + 10);
 // //    	deez = deez + 10;
 // //    }	
    
 // //    // insertion sort
 // //    int doze = 0;
 // //    for (int i = 0; i < 100; i++) {
 // //    	random_shuffle(insertVec.begin() + doze, insertVec.begin() + doze + 10);
 // //    	doze = doze + 10;
 // //    }

	// // cout << " " << endl;

	// // auto startInsert = std::chrono::high_resolution_clock::now();
	// // insertionSort(insertVec,0,insertVec.size() - 1);
	// // auto stopInsert = std::chrono::high_resolution_clock::now();
	// // auto durationInsert = duration_cast<std::chrono::nanoseconds>(stopInsert - startInsert);
	// // cout << "Duration of Insertion Sort in Nano-Seconds: " << durationInsert.count() << endl;

	// // cout << " " << endl;


	// auto startQuick = std::chrono::high_resolution_clock::now();
	// quickSort(quickVec, 0, quickVec.size() - 1, 5);
	// auto stopQuick = std::chrono::high_resolution_clock::now();
	// auto durationQuick = duration_cast<std::chrono::nanoseconds>(stopQuick - startQuick);
	// cout << "Duration of Quick Sort in Nano-Seconds: " << durationQuick.count() << endl;

	// cout << " " << endl;

}




