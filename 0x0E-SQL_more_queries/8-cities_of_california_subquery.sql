-- calilinux
SELECT c.id, c.name
FROM states s, cities c
WHERE s.id = 'California'
ORDER BY c.id ASC;
