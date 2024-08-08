SELECT  eu.unique_id , e.name  #이순서대로 column순서 정렬됨 
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eu
ON e.id = eu.id
    

