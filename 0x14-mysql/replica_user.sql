-- Create replica_user with replication privileges
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'Ephy';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
