--! [특정 형질을 가지는 대장균 찾기] !--

/* 
비트는 거꾸로 읽음.
비트: 1 1 0 1
형질:4 3 2 1
*/

SELECT  COUNT(*)  AS COUNT
FROM  ECOLI_DATA
WHERE  1=1
        AND (GENOTYPE & 2) != 2 
        AND ((GENOTYPE & 4) = 4 OR (GENOTYPE & 1) = 1)
