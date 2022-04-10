-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: soccer_ratings
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `performance`
--

DROP TABLE IF EXISTS `performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance` (
  `performance_id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(45) NOT NULL,
  `Player` varchar(45) NOT NULL,
  `Date` date NOT NULL,
  `rating` int NOT NULL,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`performance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=228 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `performance`
--

LOCK TABLES `performance` WRITE;
/*!40000 ALTER TABLE `performance` DISABLE KEYS */;
INSERT INTO `performance` VALUES (104,'admin','Donnarumma','2022-04-10',3,'Goalkeeper'),(103,'admin','Raspadori','2022-04-10',3,'Foreward'),(29,'admin','Nicolo Barella','2022-04-10',5,'Midfielder'),(28,'admin','Nicolo Barella','2022-04-09',4,'Midfielder'),(27,'admin','Marco Verratti','2022-04-10',5,'Midfielder'),(26,'admin','Marco Verratti','2022-04-09',5,'Midfielder'),(24,'admin','Marco Verratti','2022-04-07',5,'Midfielder'),(227,'admin','Marco Verratti','2022-03-30',4,'Midfielder'),(102,'admin','Raspadori','2022-04-09',4,'Foreward'),(101,'admin','Scamacca','2022-04-10',3,'Foreward'),(100,'admin','Scamacca','2022-04-09',3,'Foreward'),(99,'admin','Scamacca','2022-04-08',2,'Foreward'),(98,'admin','Belotti','2022-04-07',4,'Foreward'),(97,'admin','Belotti','2022-04-06',3,'Foreward'),(30,'admin','Nicolo Barella','2022-04-08',5,'Midfielder'),(31,'admin','Manuel Locatelli','2022-04-10',3,'Midfielder'),(32,'admin','Manuel Locatelli','2022-04-09',5,'Midfielder'),(33,'admin','Manuel Locatelli','2022-04-08',5,'Midfielder'),(36,'admin','Jorginho','2022-04-10',5,'Midfielder'),(37,'admin','Jorginho','2022-04-09',1,'Midfielder'),(38,'admin','Jorginho','2022-04-08',5,'Midfielder'),(96,'admin','Belotti','2022-04-05',3,'Foreward'),(95,'admin','Immobile','2022-04-10',5,'Foreward'),(93,'admin','Immobile','2022-04-09',4,'Foreward'),(94,'admin','Immobile','2022-04-08',4,'Foreward'),(92,'admin','Immobile','2022-04-07',2,'Foreward'),(91,'admin','Pessina','2022-04-10',3,'Midfielder'),(90,'admin','Pessina','2022-04-09',2,'Midfielder'),(89,'admin','Pessina','2022-04-08',2,'Midfielder'),(88,'admin','De Sciglio','2022-04-10',3,'Defender'),(87,'admin','De Sciglio','2022-04-09',2,'Defender'),(86,'admin','Acerbi','2022-04-10',3,'Defender'),(74,'admin','Donnarumma','2022-04-09',1,'Goalkeeper'),(82,'admin','Bastoni','2022-04-04',3,'Defender'),(81,'admin','Bonucci','2022-04-10',4,'Defender'),(80,'admin','Bonucci','2022-04-09',4,'Defender'),(85,'admin','Acerbi','2022-04-09',4,'Defender'),(84,'admin','Bastoni','2022-04-03',4,'Defender'),(83,'admin','Bastoni','2022-04-02',3,'Defender'),(79,'admin','Bonucci','2022-04-08',5,'Defender'),(78,'admin','Chiellini','2022-04-10',4,'Defender'),(77,'admin','Chiellini','2022-04-09',5,'Defender'),(76,'admin','Cristante','2022-04-10',4,'Midfielder'),(75,'admin','Cristante','2022-04-09',5,'Midfielder'),(105,'admin','Sirigu','2022-04-10',3,'Goalkeeper'),(106,'admin','Sirigu','2022-04-09',2,'Goalkeeper'),(107,'admin','Donnarumma','2022-04-08',2,'Goalkeeper'),(108,'admin','Donnarumma','2022-04-07',3,'Goalkeeper'),(207,'admin','Donnarumma','2022-04-06',2,'Goalkeeper'),(208,'admin','Donnarumma','2022-04-05',3,'Goalkeeper'),(205,'admin','Sirigu','2022-04-08',3,'Goalkeeper'),(206,'admin','Sirigu','2022-04-07',2,'Goalkeeper'),(209,'admin','Sirigu','2022-04-06',3,'Goalkeeper'),(210,'admin','Sirigu','2022-04-05',2,'Goalkeeper'),(211,'admin','Acerbi','2022-04-08',4,'Defender'),(212,'admin','Acerbi','2022-04-07',3,'Defender'),(213,'admin','Acerbi','2022-03-31',4,'Defender'),(226,'admin','Marco Verratti','2022-03-31',4,'Midfielder'),(215,'admin','Acerbi','2022-03-30',1,'Defender'),(216,'admin','Acerbi','2022-03-29',4,'Defender'),(219,'admin','Cragno','2022-03-31',4,'Goalkeeper'),(220,'admin','Cragno','2022-03-31',5,'Goalkeeper'),(223,'admin','Cragno','2022-03-29',2,'Goalkeeper');
/*!40000 ALTER TABLE `performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `Name` varchar(45) NOT NULL,
  `Role` varchar(45) NOT NULL,
  `Username` varchar(45) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES ('Acerbi','Defender','admin'),('Nicolo Barella','Midfielder','admin'),('Marco Verratti','Midfielder','admin'),('Manuel Locatelli','Midfielder','admin'),('Jorginho','Midfielder','admin'),('Donnarumma','Goalkeeper','admin'),('Sirigu','Goalkeeper','admin'),('Cragno','Goalkeeper','admin'),('Bonucci','Defender','admin'),('Chiellini','Defender','admin'),('Cristante','Midfielder','admin'),('De Sciglio','Defender','admin'),('Bastoni','Defender','admin'),('Immobile','Foreward','admin'),('Belotti','Foreward','admin'),('Raspadori','Foreward','admin'),('Scamacca','Foreward','admin'),('Pessina','Midfielder','admin');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Username` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('admin','admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-10 22:36:47
