ALTER TABLE users
ADD COLUMN password TEXT;

UPDATE users
SET password = 'migration-placeholder';

ALTER TABLE users
ALTER COLUMN password SET NOT NULL;