/**
 * @param {number[]} nums
 * @return {boolean}
 */
let containsDuplicate = function (nums) {
  const unique = new Set(nums);
  return unique.size !== nums.length; //오타주의 1) rength❌  2) Set에는 length 속성 없음 size
};