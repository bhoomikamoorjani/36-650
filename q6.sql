ALTER TABLE player_bios
ADD COLUMN height2 numeric; 
UPDATE player_bios
SET height2 = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;
ALTER TABLE player_bios 
DROP COLUMN height;
ALTER TABLE player_bios 
RENAME COLUMN height2 TO height; 
SELECT firstname, lastname, height FROM player_bios LIMIT 5;
