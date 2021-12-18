
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// NOTES
// I was having trouble getting the random aspect to work as I kept on getting a corruption error.
// Due to this, I went online to look for a solution and, from GeeksForGeeks, I saw that instead of
// doing the randomization and the normal partition all in the same function, they split it up. I tried
// that and it worked, so this is my documentation of the issue and where I got the inspiration to solve it from.


void insertionSort(vector<int> &list, int start, int end) {
	//TODO: IMPLEMENT INSERTION SORT
	for (int j = start + 1; j <= end; j++) {
		int key = list[j];
		int i =  j - 1;
		while (i >= 0 && list[i] > key) {
			list[i + 1] = list[i];
			i = i - 1;
		}
		list[i + 1] = key;
	}
	
}


// Using Lomuto's
int partition(vector<int> &list, int p, int r) {
	//TODO: IMPLEMENT PARTITION FOR QUICKSORT
	// Selecting a random item in the list and sending it to the back of the list
	int partition = list[r];
	
	// i = the marker for <= the partition point
	int i = p - 1;

	// Regular (don't think that this changes?)

	for (int j = p; j <= r - 1; j++) {
		if (list[j] <= partition) {
			i = i + 1;
			swap(list[i], list[j]);
		}
	}
	swap(list[i+1], list[r]);
	return i + 1;
}

int random(vector<int> &list, int p, int r) {
	srand(time(NULL));
	int random = p + rand() % (r - p);
	swap(list[random], list[r]);
	return partition(list,p,r);
}

void quickSort(vector<int> &list, int p, int r, int minSize) {
	//TODO: IMPLEMENT QUICKSORT
	int size = (r - p) + 1 ;
	if (minSize > 1 && size <= minSize) {
		insertionSort(list, p, r);
	}
	if (minSize < 1 || size > minSize) {
		int q = random(list, p, r);
		quickSort(list, p, q - 1, minSize);
		quickSort(list, q + 1, r, minSize);
	}

}





















