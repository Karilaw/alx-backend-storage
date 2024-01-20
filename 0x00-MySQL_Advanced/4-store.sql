-- Write a SQL script that creates a trigger that decreases the quantity
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
   UPDATE items
   SET quantity = quantity - NEW.number
   WHERE name = NEW.item_name;
END;//
DELIMITER ;
