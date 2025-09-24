/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let rotate = function(nums, k) {
    
    nums.reverse() //*reverse 변경형* 7,6,5,4,3,2,1
    const len = nums.length //전체길이 7
    k %= len  //회전이니깐 진또배기만 
    
    //0~k 까지 - 잘라서 뒤집기 *slice 복사형*
    const first =nums.slice(0,k).reverse()

    //나머지부분 - 뒤집기 
    const second =nums.slice(k).reverse()

    //nums 자체를 바꾸면 안되고, 값을 넣어줘야함 . 
    const rotated =first.concat(second); //*concat 복사형*
    for(let i = 0; i< nums.length; i++)
    {        nums[i] = rotated[i]     }

};