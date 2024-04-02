'''Problem Link : https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true  '''

SELECT DISTINCT(CITY) 
FROM STATION
WHERE SUBSTR(CITY, -1, 1) IN ('A', 'E', 'I', 'O', 'U');

'''
SELECT DISTINCT CITY FROM STATION
WHERE SUBSTRING(CITY, LENGTH(CITY), 1) IN ('A', 'E', 'I', 'O', 'U');

SELECT DISTINCT CITY FROM STATION
WHERE SUBSTRING(CITY, LENGTH(CITY), 2) IN ('A', 'E', 'I', 'O', 'U');
'''
