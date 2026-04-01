-- FUNCTION 1: search by pattern
-- Returns contacts where name or phone contains pattern

CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.name, pb.phone
    FROM phonebook pb
    WHERE pb.name ILIKE '%' || p || '%'
       OR pb.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- FUNCTION 2: pagination (LIMIT + OFFSET)
-- Returns part of table (page)

CREATE OR REPLACE FUNCTION get_contacts(limit_num INT, offset_num INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.name, phonebook.phone
    FROM phonebook
    LIMIT limit_num
    OFFSET offset_num;
END;
$$ LANGUAGE plpgsql;