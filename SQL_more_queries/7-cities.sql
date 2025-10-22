--  Créez la base de données si elle n'existe pas encore.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilisez la base de données
USE hbtn_0d_usa;

-- Créez la table « cities » si elle n'existe pas encore.
CREATE TABLE IF NOT EXISTS cities (
-- Unique, généré automatiquement, non nul, clé primaire
id INT AUTO_INCREMENT PRIMARY KEY,
-- Clé étrangère référençant `states.id`
state_id INT NOT NULL,
-- Nom, ne peut être nul
name VARCHAR(256) NOT NULL,
-- Contrainte de clé étrangère
FOREIGN KEY (state_id) REFERENCES states (id)
);
