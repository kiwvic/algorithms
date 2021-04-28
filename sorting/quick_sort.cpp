#include <iostream>

using namespace std;

void quick_sort(char* arr, int start, int end) {
    /*
    * Массив неявно делится на левую и правую часть, разделяет их опорный элемент pivot
    * До тех пор, пока левая и правая граница не будут пересекаться будем сдвигать эти границы к друг другу
    * с перекидыванием с левой стороны на правую элементы, которые будут меньше правых и точно так-же с правыми,
    * но наоборот.
    * Проделываем то-же самое с неявной левой и правой частями.
    */
    if (start < end) {
        int left = start;
        int right = end;
        char pivot = arr[(start + end) / 2];  // char to int conv.
        while (left < right) {
            while (arr[left] < pivot)
                left++;
            while (arr[right] > pivot)
                right--;
            if (left <= right) {
                swap(arr[left], arr[right]);
                left++;
                right--;
            }
        }
        quick_sort(arr, start, right);
        quick_sort(arr, left, end);
    }
}


/* start  --> Starting index,  end  --> Ending index */
quickSort(arr[], start, end)
{
    if (start < end)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, start, end);

        quickSort(arr, start, pi - 1);  // Before pi
        quickSort(arr, pi + 1, end); // After pi
    }
}

/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
partition(arr[], start, end)
{
    // pivot (Element to be placed at right position)
    pivot = arr[end];  
 
    i = (start - 1)  // Index of smaller element and indicates the 
                   // right position of pivot found so far

    for (j = start; j <= end- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap(arr[i + 1], arr[end])
    return (i + 1)
}


int main() {
    return 0;
}
