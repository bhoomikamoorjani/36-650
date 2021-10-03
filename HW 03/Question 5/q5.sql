ALTER TABLE player_bios
ADD COLUMN position text;
UPDATE player_bios
SET position = (SELECT position FROM new_table WHERE player = id);
SELECT firstname, lastname, position FROM player_bios LIMIT 5;

