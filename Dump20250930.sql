-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema setembroamarelo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema setembroamarelo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `setembroamarelo` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema respiraai
-- -----------------------------------------------------

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
  `animaçao_url` VARCHAR(255) NULL DEFAULT NULL,
  `id_exercicio` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercicio`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
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

USE `respiraai` ;

-- -----------------------------------------------------
-- Table `respiraai`.`exercicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `respiraai`.`exercicio` (
  `nome` VARCHAR(30) NULL DEFAULT NULL,
  `descriçao` VARCHAR(10000) NULL DEFAULT NULL,
  `duraçao` INT NULL DEFAULT NULL,
  `animaçao_url` VARCHAR(255) NULL DEFAULT NULL,
  `id_exercicio` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercicio`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
