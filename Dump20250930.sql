-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema setembroamarelo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `setembroamarelo` DEFAULT CHARACTER SET utf8 ;

-- -----------------------------------------------------
-- Schema respiraai
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `respiraai` DEFAULT CHARACTER SET utf8mb3 ;

USE `setembroamarelo` ;

-- -----------------------------------------------------
-- Table `setembroamarelo`.`exercicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `setembroamarelo`.`exercicio` (
  `nome` VARCHAR(30) NULL DEFAULT NULL,
  `descriçao` VARCHAR(10000) NULL DEFAULT NULL,
  `duraçao` INT NULL DEFAULT NULL,
  `id_exercicio` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercicio`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `setembroamarelo`.`historico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `setembroamarelo`.`historico` (
  `id_historico` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NULL DEFAULT NULL,
  `exercicio` INT NOT NULL,
  `tempo` TIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_historico`, `exercicio`),
  INDEX `historico_exercicio` (`exercicio` ASC) VISIBLE,
  CONSTRAINT `historico_exercicio`
    FOREIGN KEY (`exercicio`)
    REFERENCES `setembroamarelo`.`exercicio` (`id_exercicio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `setembroamarelo`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `setembroamarelo`.`usuario` (
  `nome` VARCHAR(50) NULL DEFAULT NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `senha` VARCHAR(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `setembroamarelo`.`pratica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `setembroamarelo`.`pratica` (
  `data` DATETIME NULL DEFAULT NULL,
  `tempo_dedicado` INT NULL DEFAULT NULL,
  `id_usuario` INT NULL DEFAULT NULL,
  `id_exercicio` INT NULL DEFAULT NULL,
  `id_pratica` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pratica`),
  INDEX `pratica_usuario_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `pratica_exercicio` (`id_exercicio` ASC) VISIBLE,
  CONSTRAINT `pratica_exercicio`
    FOREIGN KEY (`id_exercicio`)
    REFERENCES `setembroamarelo`.`exercicio` (`id_exercicio`),
  CONSTRAINT `pratica_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `setembroamarelo`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Inserindo exercícios no banco setembroamarelo
-- -----------------------------------------------------
INSERT INTO exercicio (nome, descriçao, duraçao) VALUES
('Respiração Diafragmática', 'Sente-se ou deite-se confortavelmente. Coloque uma mão sobre o peito e outra no abdômen. Inspire profundamente pelo nariz, expandindo o abdômen. Expire lentamente pela boca, contraindo a barriga.', 60),
('Respiração Quadrada', 'Inspire contando até 4, segure o ar por 4 segundos, expire em 4 segundos e segure novamente por 4 segundos antes de inspirar de novo. Repita por alguns minutos.', 60),
('Respiração Alternada', 'Com o polegar direito, feche a narina direita e inspire pela esquerda. Depois, feche a esquerda e expire pela direita. Inverta o processo e repita.', 90),
('Respiração 4-7-8', 'Inspire pelo nariz por 4 segundos, segure o ar por 7 segundos e expire lentamente pela boca por 8 segundos. Excelente para relaxamento e sono.', 60),
('Respiração Contada', 'Inspire profundamente e conte até 5. Expire contando novamente até 5. Mantenha o ritmo e concentre-se apenas na contagem e na respiração.', 60),
('Respiração de Atenção Plena', 'Sente-se com a coluna ereta, feche os olhos e concentre-se apenas na entrada e saída do ar pelas narinas. Se pensamentos surgirem, apenas observe e volte ao foco.', 120),
('Respiração Profunda com Alongamento', 'Enquanto inspira profundamente, levante os braços lentamente acima da cabeça. Expire devagar abaixando-os. Repita várias vezes, coordenando respiração e movimento.', 90);

USE `respiraai` ;

-- -----------------------------------------------------
-- Table `respiraai`.`exercicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `respiraai`.`exercicio` (
  `nome` VARCHAR(30) NULL DEFAULT NULL,
  `descriçao` VARCHAR(10000) NULL DEFAULT NULL,
  `duraçao` INT NULL DEFAULT NULL,
  `id_exercicio` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercicio`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `respiraai`.`historico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `respiraai`.`historico` (
  `id_historico` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NULL DEFAULT NULL,
  `exercicio` INT NOT NULL,
  `tempo` TIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_historico`, `exercicio`),
  INDEX `historico_exercicio` (`exercicio` ASC) VISIBLE,
  CONSTRAINT `historico_exercicio`
    FOREIGN KEY (`exercicio`)
    REFERENCES `respiraai`.`exercicio` (`id_exercicio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `respiraai`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `respiraai`.`usuario` (
  `nome` VARCHAR(50) NULL DEFAULT NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `senha` VARCHAR(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `respiraai`.`pratica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `respiraai`.`pratica` (
  `data` DATETIME NULL DEFAULT NULL,
  `tempo_dedicado` INT NULL DEFAULT NULL,
  `id_usuario` INT NULL DEFAULT NULL,
  `id_exercicio` INT NULL DEFAULT NULL,
  `id_pratica` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pratica`),
  INDEX `pratica_usuario_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `pratica_exercicio` (`id_exercicio` ASC) VISIBLE,
  CONSTRAINT `pratica_exercicio`
    FOREIGN KEY (`id_exercicio`)
    REFERENCES `respiraai`.`exercicio` (`id_exercicio`),
  CONSTRAINT `pratica_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `respiraai`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Inserindo exercícios no banco respiraai
-- -----------------------------------------------------
INSERT INTO exercicio (nome, descriçao, duraçao) VALUES
('Respiração Diafragmática', 'Sente-se ou deite-se confortavelmente. Coloque uma mão sobre o peito e outra no abdômen. Inspire profundamente pelo nariz, expandindo o abdômen. Expire lentamente pela boca, contraindo a barriga.', 60),
('Respiração Quadrada', 'Inspire contando até 4, segure o ar por 4 segundos, expire em 4 segundos e segure novamente por 4 segundos antes de inspirar de novo. Repita por alguns minutos.', 60),
('Respiração Alternada', 'Com o polegar direito, feche a narina direita e inspire pela esquerda. Depois, feche a esquerda e expire pela direita. Inverta o processo e repita.', 90),
('Respiração 4-7-8', 'Inspire pelo nariz por 4 segundos, segure o ar por 7 segundos e expire lentamente pela boca por 8 segundos. Excelente para relaxamento e sono.', 60),
('Respiração Contada', 'Inspire profundamente e conte até 5. Expire contando novamente até 5. Mantenha o ritmo e concentre-se apenas na contagem e na respiração.', 60),
('Respiração de Atenção Plena', 'Sente-se com a coluna ereta, feche os olhos e concentre-se apenas na entrada e saída do ar pelas narinas. Se pensamentos surgirem, apenas observe e volte ao foco.', 120),
('Respiração Profunda com Alongamento', 'Enquanto inspira profundamente, levante os braços lentamente acima da cabeça. Expire devagar abaixando-os. Repita várias vezes, coordenando respiração e movimento.', 90);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
