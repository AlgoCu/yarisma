#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main(){
    int nums[5] = {2,4,6,7,9};
    int numsSize = sizeof(nums)/sizeof(nums[0]);
    int target = 9;
    int returnSize[2] = {0,0};
    int* ptr;
    ptr = (int*)malloc(2 * sizeof(int));
    ptr = twoSum(nums, numsSize, target, returnSize);

    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for(int i = 0; i <  numsSize - 1; i++){
        for(int j = i +1; j < numsSize;j++){
            //printf(" %d, %d \n", i, j);
            if(nums[i] + nums[j] == target){
                int answer[2] = {i,j};
                printf("[%d,%d]", i,j);
                return answer;
            } 
        }
    }
}