-- Первое задания для PSQL -- 

SELECT c.login, COUNT(1)
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE (o."inDelivery") = TRUE
GROUP BY c.login;


-- Второе задание для PSQL -- 

SELECT track,
  CASE 
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0 
  END AS "Status"
FROM "Orders";
