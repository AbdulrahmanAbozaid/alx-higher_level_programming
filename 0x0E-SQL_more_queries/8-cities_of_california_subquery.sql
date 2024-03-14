-- calilinux
SELECT c.id, c.name FROM states s, cities c WHERE s.id = c.id AND s.name = 'California' ORDER BY c.id ASC;
