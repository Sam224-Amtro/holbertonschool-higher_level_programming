-- script that creates a table second_table in the database hbtn_0c_0

-- Create the table `second_table` if it does not already exist
CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	score INT NOT NULL,
	PRIMARY KEY (id)
);

-- Insert the specified rows into the table
-- Use INSERT IGNORE to avoid errors if the rows already exis
INSERT IGNORE INTO second_table (id, name, score)
VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
