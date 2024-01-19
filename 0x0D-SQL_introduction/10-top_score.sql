-- lists all records of the table second_table of the database hbtn_0c_0
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SHOW CREATE TABLE second_table
ORDERED BY score, name, score DESC;
