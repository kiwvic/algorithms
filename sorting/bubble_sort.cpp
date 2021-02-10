#include <vector>
#include <iostream>
#include <ctime>

using namespace std;


void bubble_sort_ref(vector <int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++)
        for (int j = 0; j < arr.size() - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}


void bubble_sort_pointer(vector <int>* arr) {
    for (int i = 0; i < (*arr).size() - 1; i++)
        for (int j = 0; j < (*arr).size() - 1; j++)
            if ((*arr)[j] > (*arr)[j + 1])
                swap((*arr)[j], (*arr)[j + 1]);
}


void render(vector <int> & arr) {
    for (int i : arr)
        cout << i << " ";
}


