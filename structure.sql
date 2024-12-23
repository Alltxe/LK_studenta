CREATE DATABASE  IF NOT EXISTS `lk_studenta` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lk_studenta`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: lk_studenta
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `login` varchar(45) NOT NULL,
  `password` varchar(256) NOT NULL,
  `idstudent` int DEFAULT NULL,
  `idteacher` int DEFAULT NULL,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`login`),
  UNIQUE KEY `idstudent_UNIQUE` (`idstudent`),
  UNIQUE KEY `idteacher_UNIQUE` (`idteacher`),
  KEY `idstudent_idx` (`idstudent`),
  KEY `teacher_fk_idx` (`idteacher`),
  CONSTRAINT `idstudent` FOREIGN KEY (`idstudent`) REFERENCES `student` (`idstudent`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teacher_fk` FOREIGN KEY (`idteacher`) REFERENCES `teacher` (`idteacher`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `idnotification` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `time` datetime NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`idnotification`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `idschedule` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `location` varchar(10) NOT NULL,
  `subject` varchar(45) NOT NULL,
  `class_type` varchar(45) NOT NULL,
  `idteacher` int NOT NULL,
  `group` varchar(45) NOT NULL,
  PRIMARY KEY (`idschedule`),
  KEY `idteacher_idx` (`idteacher`),
  KEY `subject_schedule_idx` (`subject`),
  KEY `group_schedule_idx` (`group`),
  CONSTRAINT `group_schedule` FOREIGN KEY (`group`) REFERENCES `st_groups` (`idgroups`),
  CONSTRAINT `idteacher` FOREIGN KEY (`idteacher`) REFERENCES `teacher` (`idteacher`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `subject_schedule` FOREIGN KEY (`subject`) REFERENCES `subject` (`subject_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `st_groups`
--

DROP TABLE IF EXISTS `st_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `st_groups` (
  `idgroups` varchar(45) NOT NULL,
  PRIMARY KEY (`idgroups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `st_notification`
--

DROP TABLE IF EXISTS `st_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `st_notification` (
  `student` int NOT NULL,
  `notification` int NOT NULL,
  `checked` tinyint NOT NULL,
  PRIMARY KEY (`student`,`notification`),
  KEY `notification_student_idx` (`notification`),
  CONSTRAINT `notification_student` FOREIGN KEY (`notification`) REFERENCES `notification` (`idnotification`),
  CONSTRAINT `student_notification` FOREIGN KEY (`student`) REFERENCES `student` (`idstudent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `group` varchar(45) DEFAULT NULL,
  `birth_date` date NOT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idstudent`),
  KEY `group_idx` (`group`),
  CONSTRAINT `group` FOREIGN KEY (`group`) REFERENCES `st_groups` (`idgroups`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=659 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `student_tasks`
--

DROP TABLE IF EXISTS `student_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_tasks` (
  `student` int NOT NULL,
  `task` int NOT NULL,
  `status` tinyint DEFAULT NULL,
  PRIMARY KEY (`student`,`task`),
  KEY `student_fk_idx` (`student`),
  KEY `task_idx` (`task`),
  CONSTRAINT `student` FOREIGN KEY (`student`) REFERENCES `student` (`idstudent`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `task` FOREIGN KEY (`task`) REFERENCES `tasks` (`idtasks`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `subject_name` varchar(100) NOT NULL,
  PRIMARY KEY (`subject_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `idtasks` int NOT NULL AUTO_INCREMENT,
  `task_name` varchar(45) NOT NULL,
  `description` text,
  `addition_date` date NOT NULL,
  `due_time` date NOT NULL,
  `teacher` int NOT NULL,
  `group` varchar(45) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`idtasks`),
  KEY `teacher_task_idx` (`teacher`),
  KEY `group_task_idx` (`group`),
  KEY `subject_task_idx` (`subject`),
  CONSTRAINT `group_task` FOREIGN KEY (`group`) REFERENCES `st_groups` (`idgroups`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `subject_task` FOREIGN KEY (`subject`) REFERENCES `subject` (`subject_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teacher_task` FOREIGN KEY (`teacher`) REFERENCES `teacher` (`idteacher`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `idteacher` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `birth_date` date NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  PRIMARY KEY (`idteacher`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `teacher_subjects`
--

DROP TABLE IF EXISTS `teacher_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_subjects` (
  `teacher` int NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`teacher`,`subject`),
  KEY `teacher_idx` (`teacher`),
  KEY `subject_idx` (`subject`),
  CONSTRAINT `subject` FOREIGN KEY (`subject`) REFERENCES `subject` (`subject_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teacher` FOREIGN KEY (`teacher`) REFERENCES `teacher` (`idteacher`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-24  2:28:29
