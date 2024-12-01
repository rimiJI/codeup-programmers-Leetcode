-- 집계함수가 들어갔겠군
SELECT car_type, COUNT(car_id)
FROM CAR_RENTAL_COMPANY_CAR
WHERE options LIKE '%통풍시트%' 
   OR options LIKE '%열선시트%'
   OR options LIKE '%가죽시트%' 
GROUP BY car_type
ORDER BY car_type