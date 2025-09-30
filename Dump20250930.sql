-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: respiraai
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exercicio`
--

DROP TABLE IF EXISTS `exercicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercicio` (
  `nome` varchar(30) DEFAULT NULL,
  `descriçao` varchar(10000) DEFAULT NULL,
  `duraçao` int DEFAULT NULL,
  `animaçao_url` varchar(255) DEFAULT NULL,
  `id_exercicio` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercicio`
--

LOCK TABLES `exercicio` WRITE;
/*!40000 ALTER TABLE `exercicio` DISABLE KEYS */;
INSERT INTO `exercicio` VALUES ('técnica de respiração 4-7-8','Inspire pelo nariz contando até 4. Segure o ar nos pulmões contando até 7',3,NULL,1),(' Respiração Quadrada','Inspire pelo nariz em 4 segundos, segure o ar por 4 segundos, expire lentamente em 4 segundos e mantenha os pulmões vazios por mais 4 segundos. Imagine um quadrado a cada fase.',5,NULL,2),('Respiração Alternada','Sente-se ereto. Com o polegar da mão direita, feche a narina direita e inspire pela esquerda. Depois, feche a narina esquerda com o anelar e solte o ar pela direita. Inspire pela mesma narina (direita) e troque novamente para expirar pela esquerda.',5,NULL,3),('Respiração Alternada','Sente-se ereto. Com o polegar da mão direita, feche a narina direita e inspire pela esquerda. Depois, feche a narina esquerda com o anelar e solte o ar pela direita. Inspire pela mesma narina (direita) e troque novamente para expirar pela esquerda.',5,NULL,4);
/*!40000 ALTER TABLE `exercicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico`
--

DROP TABLE IF EXISTS `historico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico` (
  `id_historico` int NOT NULL AUTO_INCREMENT,
  `data` datetime DEFAULT NULL,
  `exercicio` int NOT NULL,
  `tempo` time DEFAULT NULL,
  PRIMARY KEY (`id_historico`,`exercicio`),
  KEY `historico_exercicio` (`exercicio`),
  CONSTRAINT `historico_exercicio` FOREIGN KEY (`exercicio`) REFERENCES `exercicio` (`id_exercicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico`
--

LOCK TABLES `historico` WRITE;
/*!40000 ALTER TABLE `historico` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pratica`
--

DROP TABLE IF EXISTS `pratica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pratica` (
  `data` datetime DEFAULT NULL,
  `tempo_dedicado` int DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_exercicio` int DEFAULT NULL,
  `id_pratica` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pratica`),
  KEY `pratica_usuario_idx` (`id_usuario`),
  KEY `pratica_exercicio` (`id_exercicio`),
  CONSTRAINT `pratica_exercicio` FOREIGN KEY (`id_exercicio`) REFERENCES `exercicio` (`id_exercicio`),
  CONSTRAINT `pratica_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pratica`
--

LOCK TABLES `pratica` WRITE;
/*!40000 ALTER TABLE `pratica` DISABLE KEYS */;
/*!40000 ALTER TABLE `pratica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `nome` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `senha` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-30 17:26:49
