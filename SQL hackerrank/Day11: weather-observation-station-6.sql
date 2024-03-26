''' Problem Link : https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true   '''

SELECT DISTINCT CITY FROM STATION
WHERE SUBSTRING(CITY, 1, 1) IN('a', 'e', 'i', 'o', 'u');
