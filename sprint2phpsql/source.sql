-- MariaDB dump 10.19  Distrib 10.5.15-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	10.5.15-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contraseña` varchar(200) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `libro_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`libro_id`) REFERENCES `tLibros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tComentarios` VALUES (1,'Es una novela erotica recomendada para mayores de 18 años',1,1,'0000-00-00'),(2,'Es una novela de ciencia ficción en la que Julio Verme crea un submundo dentro de la tierra',2,2,'0000-00-00'),(3,'Es un libro destinado para los niños mas pequeños en la que nos cuenta las aventuras de geronimo en el reino de la fantasia',3,3,'0000-00-00'),(4,'Es una novela fantastica que nos muestra una realidad que desconocemos con figuras historicas y mitologicas',4,4,'0000-00-00'),(5,'Es un libro destinado a los mas pequeños que hara soñar a los niños',5,5,'0000-00-00'),(6,'Este libro esta guay',NULL,1,'0000-00-00'),(7,'Este libro esta guay, lo recomiendo',NULL,1,'0000-00-00'),(8,'Este Libro es increible',NULL,1,'2022-10-18'),(9,'Me lo leí varias veces que ganas de volverlo a leer\r\n',1,1,'2022-10-24'),(10,'asd',NULL,1,'2022-10-25');
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tLibros`
--

DROP TABLE IF EXISTS `tLibros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tLibros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tLibros`
--

LOCK TABLES `tLibros` WRITE;
/*!40000 ALTER TABLE `tLibros` DISABLE KEYS */;
INSERT INTO `tLibros` VALUES (1,'50 sombras de Grey','https://m.media-amazon.com/images/I/81LeWXJMmIL.jpg','E L James','Ciencia Ficcion'),(2,'Viaje al centro de la tierra','https://m.media-amazon.com/images/I/91zIwQ1iI1L.jpg','Julio Verne','Ciencia Ficcion'),(3,'El regreso al reino de la fantasia','https://m.media-amazon.com/images/I/51ETTqJmqWL._sx364_BO1,204,203,200_.jpg','Scholastic','Fantasia'),(4,'Juego de tronos','https://m.media-amazon.com/images/I/91RFD8825LL.jpg','George R.R. Martin','Fantasia'),(5,'El principito','https://m.media-amazon.com/images/I/71mf0KoCQLL.jpg','Antoine de Saint-Exupery','Fantasia');
/*!40000 ALTER TABLE `tLibros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES (1,'Quique','Rivas Fernandez','erivasf@fpcoruna.afundacion.org','Manolito74'),(2,'Iago','Morales Camacho','imoralesc@fpcoruna.afundacion.org','Renata89'),(3,'Miguel','Iglesias Rodriguez','miglesiasr@fpcoruna.afundacion.org','69Noestudio'),(4,'Anton','Pereira Garcia','apereirag@fpcoruna.afundacion.org','OdioLasDrigas'),(5,'Belen','Despacio Rivas','bdespacior@fpcoruna.afundacion.org','AmuraNeg');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-28 12:45:51
