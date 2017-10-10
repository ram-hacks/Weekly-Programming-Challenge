//
//  main.cpp
//  sort
//
//  Created by Christopher Glasz on 12/8/15.
//  Copyright © 2015 Christopher Glasz. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

vector<double> dps(vector<double> nums);
vector<double> insertion_sort(vector<double> nums);
bool verify(vector<double> nums);

int main(int argc, const char * argv[]) {
    
    fstream myfile("/Users/Christopher/Desktop/RamHacks/rand/samples/10mb.txt",
                   std::ios_base::in);
    
    vector<double> nums, sorted;
    double a;
    while (nums.size() + 1 < nums.max_size() && myfile >> a)
        nums.push_back(a);
    
    clock_t begin, end;
    
    begin = clock();
    sorted = dps(nums);
    end = clock();
    
    printf("%d integers ", (int)nums.size());
    if (verify(sorted) != 0)
        printf("successfully sorted in ");
    else
        printf("unsuccessfully sorted in ");
    printf("%f seconds using distributive partition sort (DPS)\n\n",
           double(end - begin) / CLOCKS_PER_SEC);
    
    begin = clock();
    copy(nums.begin(), nums.end(), sorted.begin());
    sort(sorted.begin(), sorted.end());
    reverse(sorted.begin(), sorted.end());
    end = clock();
    
    printf("%d integers ", (int)nums.size());
    if (verify(sorted) != 0)
        printf("successfully sorted in ");
    else
        printf("unsuccessfully sorted in ");
    printf("%f seconds using C++ default sort() function\n\n",
           double(end - begin) / CLOCKS_PER_SEC);
    
    
    return 0;
}

vector<double> dps(vector<double> nums) {
    int n = (int)nums.size();
    
    // Find maximum and minimum values
    double max = nums[0];
    double min = nums[0];
    for (int i = 1; i < n; i++) {
        max = (double)std::max(max, (double)nums[i]);
        min = (double)std::min(min, (double)nums[i]);
    }
    double range = max - min;
    
    // DPS kinda sucks with crappy distributions.
    //  This at least fixes some of the problem
    if (max == min)
        return nums;
    
    // Distribute numbers into n buckets
    vector< vector<double> > buckets(n);
    for (int i = 0; i < n; i++) {
        int b = n*((max - nums[i])/range)/2;
        buckets[b].push_back(nums[i]);
    }
    
    // For each bucket, if theres more than 10 elements, recurse
    //  If there's between 2 and 10 elements, use insertion sort
    for (int i = 0; i < buckets.size(); i++) {
        if (buckets[i].size() > 20) {
            buckets[i] = dps(buckets[i]);
        } else if (buckets[i].size() > 1) {
            buckets[i] = insertion_sort(buckets[i]);
        }
    }
    
    // Reassemble all the buckets into one list
    vector<double> ret;
    for (int i = 0; i < buckets.size(); i++)
        for (int j = 0; j < buckets[i].size(); j++)
            ret.push_back(buckets[i][j]);
    
    return ret;
}

vector<double> insertion_sort (vector<double> arr){
    int j, temp;
    
    for (int i = 0; i < arr.size(); i++){
        j = i;
        while (j > 0 && arr[j] > arr[j-1]){
            temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j--;
        }
    }
    
    return arr;
}

bool verify(vector<double> nums) {
    for (int i = 1; i < nums.size(); i++)
        if (nums[i] > nums[i-1])
            return false;
    return true;
}