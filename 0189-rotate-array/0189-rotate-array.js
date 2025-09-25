/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let rotate = function (nums, k) {
  const swapRev = function (l, r, nums) {
    while (l < r) {
      [nums[l], nums[r]] = [nums[r], nums[l]];
      l++;
      r--;
    }
  };
  const len = nums.length;
  k %= len; 
  swapRev(0, len - 1, nums); 
  swapRev(0, k - 1, nums); 
  swapRev(k, len - 1, nums); 

};
