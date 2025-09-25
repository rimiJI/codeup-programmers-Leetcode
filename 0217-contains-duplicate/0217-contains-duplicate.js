/**
 * @param {number[]} nums
 * @return {boolean}
 */
// let containsDuplicate = function (nums) {
//   const unique = new Set(nums);
//   return unique.size !== nums.length; //오타주의 1) rength❌  2) Set에는 length 속성 없음 size
// };

//또 다른 방법 _ 위와 같은 원리인데 이건 중복값 발견하면 바로 true 출력
containsDuplicate = (nums) => {
  const unique = new Set();
  for (v of nums) {
    if (unique.has(v)) return true;
    unique.add(v);
  }
  return false;
};