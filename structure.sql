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
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('abramovjakub','scrypt:32768:8:1$MRwlcXJ1FWP2EwQR$2065a61172eb00fc41a4274c04b173e930e47c63233bf66bc426088622e9a74bdc3f267e195cd7ae66627505eaae26649af15a8ca7a0033a5cd87478a207e126',601,NULL,'student'),('adam69','scrypt:32768:8:1$hw5RrbcGsnTaRPFx$400719a50d6b276d64633b94b7de4b9897232a4d87b180a494f08819325aa7a5ba96cdb1e822ad520e92693b3084e952e2990074770f7e494b9a08a2d54394e0',569,NULL,'student'),('admin','scrypt:32768:8:1$Mf6ByCgiPEodlbA5$7309695b231a3d9a90d6b528fb410261a7ab5169e9f4e0721a140cef13dddb4f296273d5a0ed639220c53f30c4142a73b5533e286253663dea019f5a280e4a21',NULL,NULL,'admin'),('afanasevevgeni','scrypt:32768:8:1$h7RpGekqgsv8vF3j$a588a1df832c905a97c101d79ed7d685409018b1be76d5890b9466a9bd71f0a17830cd05565dd8d7766861249b0740bceb4ab7d03afc4cca19fb3f0af7fdda3f',589,NULL,'student'),('afinogen_72','scrypt:32768:8:1$MLNLGL4mAowaL4GN$0d90bc41b02ec84b92397f2388417bb11753e30ec950879aaa314960865274f95ab1308b1ce8682f95d280aa470ee6280c82be195c3efead18c0fac2ee777a0e',579,NULL,'student'),('agafon1999','scrypt:32768:8:1$iJmoTCqXsw0LqNRh$b02e28f7f4a7a4db3e08e1b17052c34d4515c1f6849453b98c615c0ab3fe73678bc7f22e07dca2fd418ea22b3ecbac972f1afe393e8e40759c71dc53d41c9fa6',637,NULL,'student'),('agafonovignati','scrypt:32768:8:1$iI3EKQe4FTEI2fdN$146d8ce7ed7161fac00282c3424f5acb99892e8c98fdf76f8f30c82dafaff55250ab8594cd9b8f3ede6662f225257f043d3426c53f5df2b569a573f2d216c2e2',585,NULL,'student'),('amvrosi_1990','scrypt:32768:8:1$b1OF0xu16SAkqE3J$911bdd2ca502bce8108ee98dba1a66d34bffbe0b62a48f87509ab9ca1b327baa80a8b654832eba98033e29ea5298df54be0c7a38a50f6d9f989992b900aa2bd7',603,NULL,'student'),('aristarh_80','scrypt:32768:8:1$Sq6541c80iQNLD14$24b21afa52bedc8a4cc1616b4f716178f8da2f0c90dd5170aa649d1bbabb6b894b6250ad81e3f1910a493d0b2376ad8797eae5ef1bcb6e26efdd70f208d582a1',638,NULL,'student'),('azari1977','scrypt:32768:8:1$IR3gXGYmZk58B863$d44b6ae0a55c138ee093e21924456e7ac2b851984ad2d3efd56bb15fe245db061e1c167813faf3b255987b2a542c04467306b8fec798315596bc5bc06f6ca2df',639,NULL,'student'),('bikovirakli','scrypt:32768:8:1$CvQ1QlIcgHkcNW8q$8301846aae492314bedd4803b2e2bed3a64cef7f8b544be0d1f522175061dc6bc856cd60f74c777aa395372e64231786e46fb1d27724f7ac6ee83844307481dc',566,NULL,'student'),('birjukovvissarion','scrypt:32768:8:1$Ndt6wRiYkg7GOHWM$bec3c19c7b9c8d3bedad7b330be0bbd10ed944b6b06fa2806fac12776c61c6ec36d6a0e565aea82f7b757c18946d45a3d482beac6f9a34d35beed0972b8cde2a',559,NULL,'student'),('blohinafekla','scrypt:32768:8:1$hUU0cHH31XyvZid8$0a937c0ac6be6f9298b53fe19b750382f34a8f0209e4a34f077e97e8aec2ad69cde8b1de80ae45422062707a4bf2e03f811b24f1d0aca43f9cce0f061d9380c2',629,NULL,'student'),('bobrovdenis','scrypt:32768:8:1$kxb0Z5dT2BylZQ6q$b332cec98d875af7b61dda296f57ea4e6c4adf1f4c0f23d1e6e0c7444518f0bad75bef9e6e238ef5529200169b249ee8bad714db85d78eba7a6ad2948dc958a8',550,NULL,'student'),('danilovaoktjabrina','scrypt:32768:8:1$gOoLEIHA4XHrikXd$746083edb89fee966c52b6f4685b4e144d233d4300568c2b2988c0da14b550c780a3cd891062c2de9a7ba6c1bffc8d53d553b7694364cc552e782776bc4d0765',528,NULL,'student'),('danisimova','scrypt:32768:8:1$US49TJtrqTD528Bh$fb32962c2610939a2ea1aeb9cdba6b8cee431153d9f95decc858dc33eab5d3877fb7f8012149d07e8aeb939dde4a84efe21cea0ec659d046edef3d0fd2b86b78',547,NULL,'student'),('demjanmaksimov','scrypt:32768:8:1$8ntkWt37UEja0Nby$5d89e24c7fb0abb995534d9d7ccc3285b26c5a4cc4ce44d83634faf51b1cf80c3f96fa45e27bcb4ad750e479ba1933d30d776d7998509c8a3f2cbdc657d9f425',635,NULL,'student'),('denistsvetkov','scrypt:32768:8:1$ja5h7O4nxisbH6rz$833fad68ee8e9df49455a4d40efe3aef9a8e8fe98d417e73a910af68e0e6f26e06a911196faecf7695ee84cb0eb53381ebcbbbc0d01f81bd3e702739a05b519c',617,NULL,'student'),('dobroslav2018','scrypt:32768:8:1$AhxbSm3yrx8VYAX5$8cbb3f8cb324f1c8619fb39d5b6c1270b4e3d8c5219d13781a8b245873f75e083da77efe01ed7d5c2c8588f1e1eaa4d2582a97ab41d9f2f2ef4b7acacce9b4c5',545,NULL,'student'),('dvinogradova','scrypt:32768:8:1$o0ZnXqjrueGLnvDi$987ee850fa4c0aaa83776e6782b8a78336778944aa88db49e7b647c7dd7a78c48cbc48c85ba2ae1d7d5af059aa2ff58a31b1be5d1fe5d5bd9b2404dcccbde182',627,NULL,'student'),('efimovaraisa','scrypt:32768:8:1$z5NRVcu8iEVZsHQc$6db195395c5870aed27b8acf3990773e4005d2643569bad87e541407ed5be66009749a13996b14ed27e1ea3ad4e687f4f259dfc4a13e099c658b28a1c12e104c',640,NULL,'student'),('efremovvsevolod','scrypt:32768:8:1$XJVA5RNgAeTUknK8$1051f15d08eef3c042945d058c60acd42c1776b676e0c7508f5ef52e5b82b78dff7f257b781345651ef0031e6b6646a53387e0f129c1997e6856529adcaa96ff',618,NULL,'student'),('emmanuil_1998','scrypt:32768:8:1$lFfY2Crr80rV0sd2$8a7855a002c062adec5b2d32b23e72e0082ac541d4509eea07e2fce7a4b3f39b3255862c96d94691c6f102871b06e01027e16f425ce881cceb41c40bed9b5f9f',646,NULL,'student'),('ereme55','scrypt:32768:8:1$MILe2Wda1mDWPUl0$44909da73bb64ed0d0bf3b1f325e034a888f2397009c5626463ec207659036d6252865c61eef3b0cd9419194690aecc934d120eae5144675e04ef8a9c37433e9',560,NULL,'student'),('ermola_1971','scrypt:32768:8:1$pSqC7dtudMOXmglJ$3f76612f918c75394e76dfdadb937087bb94e39be30972f7a4cc12184582820496914b465def39ea1b1e6517448164518d7ea092ad304ee285834f2caca681ce',600,NULL,'student'),('ermola43','scrypt:32768:8:1$nPcVzQOk92sGzacS$868ffc0dc6aa2f8d0a43b8804b97c20bb88f8d5605b93160d9ac0889c5a4bd1c1ecbe6740c8c4629c2a2cd0db8746c9c1fe04c2503704ad2271afa06153ad83b',623,NULL,'student'),('ernst_2009','scrypt:32768:8:1$n4uNo1g9qpigPfQN$f981cb66af705f7ce961fe1241fd97799890b6dfaae623455fd7fc7b9f8da3935fc59b4545f8059f02dcf48ffa3f6f17ea2f06111dcb08d6a9caf61dd51f171b',633,NULL,'student'),('evdokim_71','scrypt:32768:8:1$20bJDhLuFCA9B1jt$42fae3d523490f4cb0703e653c06003f92fd07c3d04e55c77c4b84cb86448a91e64988804e39e2a5d12fe21d19af59842a394e9f17ec3c79e64993724629bb9f',542,NULL,'student'),('evgenija_33','scrypt:32768:8:1$nzZTLlDDpP7HI8g6$a153c475d57efb95ddc972917025c4f0b1f55ad43d65cdb2443e4f22e8d32bff76bb6efa62606b3eac9060b0decd9273992945f54fc5d6c51ae1d9f3c3fc2120',582,NULL,'student'),('fade_1991','scrypt:32768:8:1$FmVtWx8HooQ8ZBVk$f548381d5c20c86bf2559aaa904ebe3dbfb8f6b31b4fa45c0e09701db1cb459bfe65e28cc51df971a271df03d05dd2bca5d5d74eaa4df0e97764c4bbda530f6c',548,NULL,'student'),('fade_75','scrypt:32768:8:1$GiOtLbBrfPXWiQD4$4ee6d8dc15e7e66f4db8422edd23e0dd0f20af5a96cfc423622324cda5e18eb16995a1502ba694a6848580b1915226e7f32584180bead8e29f7c6bf980c63fd2',602,NULL,'student'),('fedoseevviktor','scrypt:32768:8:1$h5au6SxEjI0jK8vI$0d1a5a355a01780ddefe437d84a43dc70357c7b29c15d7b1555543d9bff4be552b2ff914570851f07dec1b065071e4add5cecfaa417468b8065310babb45926d',594,NULL,'student'),('fekla1980','scrypt:32768:8:1$XcGGbiyzj1RwhE8p$64a0bc4c614f9307c3f3651bc2f059fa9ceac4fa73ee0d6993fbb111ad9e00aede1cae7c0ebf1cc392047a02756c0aae7bed24662ff0fbaddcfd00867dcedf0d',555,NULL,'student'),('ferapont_68','scrypt:32768:8:1$E9YAhORJwjWMSfqN$8d21f25474847a92a8ad2f4c07be65cc05eba6b5f376fe48f986768dd2634b9754d12084a3569c9098a74e2ea3b9735c03eebe4917e5b946a1b2b85dd9a12191',631,NULL,'student'),('filatovaregina','scrypt:32768:8:1$ZyMwJBz459Oxig7R$fbd0e0cc967b7afbe68942e28f6679e2f0cd12242172492bc81536a1a2ae3b3e1c3ed21a422b77524d761eaf16e4956b24a848b3324529aa134b2a5105208129',NULL,52,'teacher'),('fortunat62','scrypt:32768:8:1$nN4BAKOggcIpjAHU$39d0c9266aeb94c914ed88f556757e3aa9841673ab8f0b0144ac2c7f684afe1d1ef5489587a459c7e74b97bb4b283ba3fd4ae6ec14454906c445614f3f932f8f',546,NULL,'student'),('fpopov','scrypt:32768:8:1$VfGVLuh21njFMwkn$7b5fb459650c939436211389dd4dfaf1fb522f69741a9a0105ae186dce63acac248a3795d9d2a07e10025037aab74f7afe410d66aeccc35dbb54d17e53a573a5',591,NULL,'student'),('gedeon2001','scrypt:32768:8:1$m2efA2RwSSGIO5gb$b4b6f6c72d8fbda5d9200269883c3238eb2c8f94a4d54306820b1462739a209769802b998284b0b0edc43645de43fc02c7b91f2479f72518576dd78b4196a53c',554,NULL,'student'),('germansamolov','scrypt:32768:8:1$t6u5GIWUtSany3o8$a5018ed4677c74747d08b63954fd6966c0229997d7d3b2b9735bb5b8865df09dc613fe52df4a3905b80d416a4204a5aa94a58beb4bab85f4d6a2b0831b1470aa',644,NULL,'student'),('gorbunovalarisa','scrypt:32768:8:1$6hEppjTt0xRZzKB2$4acd05191f25108920b74b76b9108101f41e5acec76503abc1a20bf54c956f8e21ad54eec3632ca956cf2ff9c5de959a6234439a6e2f0de86288b68005fa8620',593,NULL,'student'),('gorshkovanatalja','scrypt:32768:8:1$e1rhrXvtHLZfvBLt$08e32eb3aa17688ad85f089fcd8bec9a5dc63b8698e9299aa7d677c30b6cb14dd1d8cdb235b240f373859890e5c27607466f28e8d47b665344be65b1a0160242',570,NULL,'student'),('gromovnikon','scrypt:32768:8:1$JjWJkystLN4yndJ8$cfa41b4d86a94facb1f903defa57546f34e321a484a29428b06399ce1a9f3f2cc93b0727c761784597aa57f3e358dcf007b157e812d5b3721534f014ceacbe07',534,NULL,'student'),('harlampimoiseev','scrypt:32768:8:1$h3No3DvTdrpzjAy5$4755a4300f574f098972c6b87b3eecca6b9ffbc9d0039d90ae064c3036e200545cf9ff3a674f6acd2334df8828d03ad73214268e890ef96d6ccaeb2cece85d53',562,NULL,'student'),('ija2007','scrypt:32768:8:1$nHX8f6QDoaVEFSWV$332901b804d325848a322f74ff1c8910d8392d9af00fc6689f68bd7f3459c065fc8ab84bd31a80d7ae49d25f55f00e402ea821c72a96ce48a057ac77f78c8261',578,NULL,'student'),('irakli_2008','scrypt:32768:8:1$pSNT7wlgw49wer5E$9c5a0c610037738c4e3a438fd271869dee05ab7b359e04a8cf0bb548ca14165105441d72c041ac4e35710bcb23cd3cffe1c4b4bc09b78c7da613da8a57c2a20f',607,NULL,'student'),('ititov','scrypt:32768:8:1$C3o5LxDC93MUPC5R$66b83c01df7fcd13f68d4833996c69529bf9cd78034504fee8395491badbdfa73884a4378f7a84ce718409729805067404688c4fd49f8c6a48ebb4d6f9d65663',NULL,51,'teacher'),('jlavrentev','scrypt:32768:8:1$uBQFBXxqFC1aQdZw$7b7b70c64859151b9b7352ed2020db7864e57d68fb19b9556e0959ceaa14296802bea6af6d13d55f3f9a5799b1dbe98885cd3a3377bfc1e69e9b9d7f2d66d0fb',572,NULL,'student'),('jmamontova','scrypt:32768:8:1$dT3GIrtIp3cjRQUk$74ee4dc8eadd663b32ae1edbabf6e85bafab17c060849d6fe5f31c03ee1b79b4539b1ad6db4eef4d4602c6500cdcb2368bec5e9deb3e628c01903d9c665ad4ba',606,NULL,'student'),('kapustinmihail','scrypt:32768:8:1$5Mvnk4nmAVt8Z0UO$efe91acefba714f4f984c254e367d7c7c2212f80125b899bcd2082a819431523a43c3901d0340b63855faa4e97e5339845c94e43945104939e7877b3262ae417',NULL,55,'teacher'),('kim2014','scrypt:32768:8:1$DN4CGl2RfibVH8fN$e7ead5ea0218a7eefbf0cf3e1233f04a60f53c87214a1ce3fee30d43ba2103d0880ae5c7d9335c69712275f6b5d9da9488b281f321b69425a270cf81c033a6ad',563,NULL,'student'),('kirill13','scrypt:32768:8:1$jYAqPbyjHDVwGExJ$f041438f2f1fe6b62d872033a4b344887ef6ada62349c98f37e408c66539fe9c6f1ba7aa0786a19e3dcbb0596cab7ca90b6e860a007fb7602e98bc0c3de5ae77',NULL,50,'teacher'),('kolobovfeofan','scrypt:32768:8:1$09ecQ5C01AetxWUd$868ed7c9518b7bf80efbd015c83deb8df52a0d9e301084f57ea7e84add55ef891e1847b37f8837186a4515eb9bef92d0c08adc46f5c066817fdb1e949705a99e',530,NULL,'student'),('komissarovkapiton','scrypt:32768:8:1$aA4Wj3Kt0YbLlhTy$b193eceab98af9c6c66900b968de590b0cc3c667a4ab448d3971181e0bd851d0d6b5708180c5391153e22e5eb4e95705de00ff777458cbd4ddec141ca12caeba',610,NULL,'student'),('kondrat_1970','scrypt:32768:8:1$VhC4raC2ynIomXkK$42a0e2b2c47e34d0e444d5c7e52553536c347c8d677e1258773702b9aa27a9add47d2c89804d60958105ebd39a3a21032b2dec5b013d791149292059b605b986',543,NULL,'student'),('kondratimoiseev','scrypt:32768:8:1$8f6mEboo55KeSwBP$b6c34bb68759d0f03dc542b6a0536b65cd58505cd05f706e4482735f1e2ed1bfbbed2b7812bf56d1bc0e347c1809c4a04d72c3584778b206b2554bb9014950f2',612,NULL,'student'),('kononovzosima','scrypt:32768:8:1$glwEhjAB1PTpmwNr$4d39c47ef98aecb7baca9bffb831a8d21cffb85ea21d711050758a841402a0ac9e45734196cd0a804d2ff11b619d9317f55d76ed755caa7895130896b2b114b5',NULL,56,'teacher'),('kopilovaninel','scrypt:32768:8:1$gGR51oIEjBWxyBr7$26cd431681ed86f81061c64808569bc2cb00b81f17c54b81edba34e8261b07eebbaa49d064f8367f198489a26e8544ed9590adcf7de9c63c8e9d635e6d6e9b5e',553,NULL,'student'),('kostinaraisa','scrypt:32768:8:1$43X0w6PGsfMUiDsx$8fa0f06967911c5b2abf64d36105528d46d709ca7e8636092ba4385d82e569f4791d632122828d2465cf8147f7919481df4933fdaf2bad946a25b7970fce68f2',531,NULL,'student'),('kotovboris','scrypt:32768:8:1$HgOuV3FvQoMEz3ML$c2304e6d20ce60878ef407df2b529ce670377876e113f9c98621f30f583d9ed0b61094a72a001713e3773ef28933109429cfd7a39aac2dad4a6f4376d2238705',595,NULL,'student'),('krjukovanatalja','scrypt:32768:8:1$gILS1IRToVa5aUDg$71e5520ae4af76d5350d5cd1c2c873c2851842f7dd3615bfae2852320daf9e0d2f320c8f6d79af0a0a1add13d8249d43347a252d3edd4d87c29292235a16f29e',621,NULL,'student'),('kromanova','scrypt:32768:8:1$JKgcWYwoa4PtaUPv$871d5e64f1af4496fb6564cec5cadc75a34014abe11f2b2527ac12467a781b685496611d55b11aca85eb3668ba3e8ba8120c5b06b17cc507fa29fcd04df44f3a',574,NULL,'student'),('larisa78','scrypt:32768:8:1$hgJDeRyifJ8JlxYS$02ae8b3a4de344f2798df99562dbca0897421bbbdf8804a36274ea66e3318eee20700bd59870c049a2bd66fcfdd6af8e4338419ed423f65fab3f78f4cb6d161e',567,NULL,'student'),('lavrgorbunov','scrypt:32768:8:1$f8jWb7FgncYimrS8$e0480c0f5837d6df0d58211e731d1c4ec212aa67465f5021da5def688cb4f2fd20a9186089a694bc4b0786499d3423fd04ecbde9b447b5629319a43de5ebb642',592,NULL,'student'),('leonid1981','scrypt:32768:8:1$e9NEFdM5C8dmJkNx$119a10c01f28e5253d405eda07fee7de79effd1272f085d2988d6f71aa3d8a8a46d849df7b0454d7e991bfe8075a50a4b36c987654f5f5db6da46984df98d843',609,NULL,'student'),('leontikapustin','scrypt:32768:8:1$1IB3HUAWouyiV8ex$799757a04c99f9bf4dbbc3c5557a3c6a3758b9eb150c4ac37cbf2aa7133abaf94349473b915eb78f7232c3e4a38c418dbd2eb060e361dc0fcde450ce11e94cc4',630,NULL,'student'),('lfedorova','scrypt:32768:8:1$xdq3BfMmeEPzSIvj$8332a97fb493b326febaf1d468d6bf33b72572811416e11bb724c6e2b12a8b7a0ac7d0289f4143862986dee219f80b01afd8fb93f5c7ee6391f3f7f2b743a46f',628,NULL,'student'),('ljubov2015','scrypt:32768:8:1$FaS8CqdWllOhfyzB$892f29c0bd26df359fd34b11f68559e7261a7bc141156d5c9933131cda92a1ec3be143f4336de82de44add820da22db061028f4eaa6069024bcaca11ddd0edc4',605,NULL,'student'),('ljudmila29','scrypt:32768:8:1$Ndyi1jlF8NnU2Wjm$cf937ed1f6272ce96758cce90051b048052dd9ad7e5d5818664c94e58d1fb6a1435839304cc448a864d9445d41945ff203dbd4448c4564641d4a06c272c32688',541,NULL,'student'),('lmironova','scrypt:32768:8:1$w68kXXwYZhrCfc8a$3837b56a3ba392a97547f62585096863daa2201cad59e9f14c0ab98f9c8e39096372b90b54d6ca9012a094310d9fc4a199735188099554984567448e00ce54f7',544,NULL,'student'),('lobanovelizar','scrypt:32768:8:1$qkQDkatkhei80M9K$618067e0c42cca3fc0dc89ada58f569017c2c55574d791bcaf457efb788a60a3a01f82349a1df48102eb1ea6f157f434f64f802ea8ab8b7d63992a23afe1adc7',529,NULL,'student'),('makar_2006','scrypt:32768:8:1$j3b3W2UQ97nCbKc5$d829f5188b1b54171ba38f9ae1ccea4d378cf1ad83bb3ee5079906f3d3e538cf8fea9a162b2a7a691ca34e5b625d6096a4bc925fcad7c81e2c827191e55cc479',551,NULL,'student'),('maksenov','scrypt:32768:8:1$4wK8G0EjSnOn3JUq$1dcb9146406caadc7229ca564e89e24a0a71146bfe042547ec031a139ed7952527116c580a09f7484efabc37d08a0756af8d5a52a7ec3df76584751612a70aff',597,NULL,'student'),('mamontovernst','scrypt:32768:8:1$qQuTnYDrmWYfjPwL$bbdfa696e0b4174986f6bfc6203ab221ecbd4d10a23a23d0b69128642d9377f5f67f61ca358e0db4e499a6c007329beb543a9ffef85bc75681417e7637593a34',588,NULL,'student'),('marian44','scrypt:32768:8:1$M28fJIaL9cAwIpva$cf38d29458b986e5c1722c107692ec45af8b0f958e89155fa26950077d158f4d6d2c47246182fc896d829d7276e257aada6c69ebc82ab17d46e5f9438f0b1683',581,NULL,'student'),('marija2005','scrypt:32768:8:1$SUQz4l6F9O69JnS5$a635e0dbe64f63062dbf1ed88627d0c406a365547cd45913a830f151d2dabdb848a6e16dfe1bdad4b47ac8daee172b733fa0eca9350763f9193425e279a6311b',575,NULL,'student'),('matve77','scrypt:32768:8:1$AomxabfrWIMgd4zN$65b5999f1af42a91b58fec8e9a66ab54b50129326bf112ab234fb74d7a2010a91ff47797f8895f42b5965c946dacb26a5ccda2605a69898a0e7b5b756ad084a7',535,NULL,'student'),('merkushevfortunat','scrypt:32768:8:1$P63N1Pilbj5fnAeC$a98cb287dcc40626765c00040d1ef25fe3608758cce3cd1a4df5048080c598ad3985e305702cfb062c6ac287423d898a980ddcd099639d8f7e0ab8dfb25a4d42',552,NULL,'student'),('mihe_98','scrypt:32768:8:1$70UMPKyolYVIqLjX$125c9e21588720bf05b4691f1b7ef6c2f361b02a7f2261da9e8d3f6e79fa0b1693dc164d6464a5bee87d95ddff5e931032c3244cadcc8f1a798472dc1402c18f',616,NULL,'student'),('minaafanasev','scrypt:32768:8:1$67A23I24KTsgH9Nf$c730067d49fe17acac4533eb67b3e09a04c429dcc565a808dc5398d4f52f4bb70b187df1118a4262740e785e2c8e9a8b56a9b5b9d452810456118dec5c5e87e7',626,NULL,'student'),('mstislav66','scrypt:32768:8:1$L3YOeVaPOFKLOMDR$aad5b451b2a6ca0b8083eb570bed067bed498a95be5ba9f9530b09a134fd075d7b07e77525a679c42294c18cd3d3c4321ef0b9afef9940f8f6a09aacd4930f06',587,NULL,'student'),('nadezhda1996','scrypt:32768:8:1$lRyxEUK2cYvG1Zz7$3c9bb5832bef5f2aae7d3019e42d97f36e80981db62bc063a3b845fc178bd9454596fc0f2dc5e5993fc50a9b57f91266d8350b8a376fb372b6456082294e826c',571,NULL,'student'),('naina_2016','scrypt:32768:8:1$Qfv1I7N0xQWP3fW0$31534a990123525c3aa9e890aca6fa1faacc931af8b500f95be669b04f4f8b764090fb3a4cd562cdb0309070b254734d4a2d74c4549fca4144d797cdb4646d97',NULL,57,'teacher'),('natalja_2018','scrypt:32768:8:1$uYz3d4fVFNZTez3X$66fe3b63fbeb6e580f359eb195829b7e87cb779c35321a5123115af2b2de8ffd211b40df016fdbd7e69ebae1df644ab184f1950b6e71b4994ecf888f52a2be7a',608,NULL,'student'),('nfedorov','scrypt:32768:8:1$9ZeEd8NsbC1kijma$c754446ed97b65da2afd8736c02e4f499e0c08871993451583127714a3d62be83645be820ee66d1df23f7e8ecb809e381328ebc1aeb8c2fd66785efdaa12ce10',641,NULL,'student'),('nikifor_2008','scrypt:32768:8:1$ZBptPoTRHctNtTLM$c4c282c12b1ff880db7e32e5edbc396868b5fde26600dec32d1005a2b09c4205bba61885c05b174cf406384f66cf2079a65ac54b488d68ea5102ac380836d654',590,NULL,'student'),('nikola_1971','scrypt:32768:8:1$zpUhhoQhwNkT417c$8d94cad1f60085009bbcbe182bda85e1f6429885e5063eff4cabf4febcd4cb59aa945ffeaa4abb601afe58d5e19e5cc6026cc0750abada4f061750cccf2af3d0',576,NULL,'student'),('nina2009','scrypt:32768:8:1$YAHYpQ9t3EabFLVa$a0bd9e8f7b8c198548d82eecf07fa2fb330315462067d1edd013299c0ed218be57e8d9ccb38f0069d310d733a793cf634188e6be748d263a7cc7ccbf9808159d',568,NULL,'student'),('nlavrentev','scrypt:32768:8:1$2Fk5o2EEoAPKuCkQ$3fcf9f7296ad20e37381f7c6111d434994d88c66843a60efbf29c604ccb024f7177400d304e33acab77c141b1305b0fc5277abba78e2e4ab9f2fdf760956e327',558,NULL,'student'),('noskovaveronika','scrypt:32768:8:1$SoQUhKsKvqRfIm0N$671ec3f5bd3835e1adc2ce18a6cb4285602b9f3983a27a2b31709f58ca935e88623bed6bd2be0cf4fa65997f212b11124687ece36453bad1718b7576faa4b0eb',NULL,49,'teacher'),('oksana_1994','scrypt:32768:8:1$txUzvBvNASbOLjZs$947382535ac241343f5d24c632e5b2e8f4ac554dc2788fcc36fe4cf28b744643aee133ada970b82fe61f496b3741f1575860e2bab71e9e48daf4853cd095eb6f',632,NULL,'student'),('olarionov','scrypt:32768:8:1$OvJg4s6CZRiOwHoZ$ade737c79bf53fdadf9cf0433302ac7484456fed024f26e19d6f5a5b9118ff94a630b1bb984260b3124eb1f15c59a234dc660e271750df2798ba7a9b12c978e7',564,NULL,'student'),('osipovnarkis','scrypt:32768:8:1$zi7HHTh8kJspj6Vv$fd2bc25a9b2cd4045ae801ada789cf4305bf9ac607dba3b8aa83ed489e629d18fc455d6a7dd22821d5614405cf08aab794f6fd410ebaf1b940182f0bc0a520a8',614,NULL,'student'),('ostromirdjachkov','scrypt:32768:8:1$33iMFz9wgJDa22lH$e4acc046db469d1e804bf47437da9dbe81db058143e1914dab2f4b931fc00c2afd6e1ec3c6e40e68b1ba86313f7a787937a31b67e03431bf22f6abcfbfc99c97',613,NULL,'student'),('pantelemon_2010','scrypt:32768:8:1$qAJi1CmAdodqMxMf$d4144356a0c14bf6f5c9f0cc3c7303adf58ccf01dc4d728e350fbe2090f18945ec82aac30ba5204cdd776bd8b87e103884ce4cba2a44d6ea6547e37596899a8c',643,NULL,'student'),('pavel18','scrypt:32768:8:1$1THfkdfd58MTuXPo$26eac7efa729750118a3230e2839743641772b564bf072bd95f1914bab5cc3bb952942fe087c7387b440f451a5d86ca36cee743e5bbe0464f324b4812800e13e',596,NULL,'student'),('pavlovsilanti','scrypt:32768:8:1$sLyrk0CTooTb3d2A$a18a04d387ab4c919d74b110a3d45c247228aac8fd6a4d43aa71edeb77b86540711d9ed313e8758b94699d443f1fa51d05cead0eb8c308a61f17b0e8f79ad5a9',620,NULL,'student'),('radim_04','scrypt:32768:8:1$xrqYJdkC1KAnODun$418693019287c342c0e15082a82225e02e709850648fcecc61b46d81331f10c89b56958f2b730303a7150c8c27802b63df66b78b7c7c9c821392601fb05dc2de',625,NULL,'student'),('rbirjukova','scrypt:32768:8:1$3q6ES04Rp8wWrZKI$b309f56d1b6b876f05e075ce959d8f27158251eca2ba4809e2843a2fb684a225f0b51a58309f0a4539e2962bef6cd023015130e6ac275509eab24af9d2dac2f3',549,NULL,'student'),('rjurikzinovev','scrypt:32768:8:1$Y16FSBN50LCGbWdS$22c81c2d3f1d484f36a13920269ed5ccae7f989f74156e512cf457f3e4d91da7f332eb0825d1c20eb8017005d839cde4b92c2a1ed9b48b8b0c16d80cb20db62f',647,NULL,'student'),('rodionovignati','scrypt:32768:8:1$XjgjuUfjM1GOmOHd$90be70b03de59f111db1bff19f86840f337c96d2af1bd1670ea365c019e86500575ba7b8a7cb34778577d081a35a2c699b9ff4eef95b34bbc994e2d7e3f2d70a',561,NULL,'student'),('rusakovaverki','scrypt:32768:8:1$Jx35sYVQ3rQ1FiRL$47d912c0c166f93a88246ee98a1b1f0d0c8ab5d79199e303cbdff567a491822e035887eebec0a372b0410be39a303d33a263fffe03147b6d422a5ddd5dbff991',540,NULL,'student'),('ruslaneliseev','scrypt:32768:8:1$JJiseBJcfSCOVCg8$e93911ee800379404913d5db8c1a9893aba0610671a812ff1351119a4faf326966d7c148fd857eba95ea8d51ca45bcc8e58dd33a738ae9a2de699226c6bf5cb3',604,NULL,'student'),('s','scrypt:32768:8:1$Sj3b6QwS2PBWEZZr$f2b3602c09b64a06f60675f88cec8b10a2d91f1ab8e8bf894b4bd12242dd76638851d15eadfde7f9cc38a5015aac4d6d4a4f954932bf36b299ef878c9c9bc17d',527,NULL,'student'),('samuil_2021','scrypt:32768:8:1$R1Hwbe1eBwJTxOee$b7a89ebe06406cbd3e8ed4b942bb2c9466aad05f644d8539c16af1cbae637d6182e01954b2ee5d8571b37585300529022916141a562afc29a415af12f51beb80',556,NULL,'student'),('saveli_48','scrypt:32768:8:1$DbXCuBDMYADva66e$70e6b62e96c53a130aaf4e903705a720154c3643c620b5905b91ef712a68a7419f1845abb8401a7f0714ead988314055f2b6657eba0225b762edbd2e67eb6354',642,NULL,'student'),('savinapraskovja','scrypt:32768:8:1$3hDWPO7LMXvNcxTU$09bec5e79084e0b2c44e90fbacb2728ef897112305cad587d066b84b72ee74bd7a7dc28967a90fa90ecb934b22da1edf183ac19602b578e186afff2daaa54ea4',539,NULL,'student'),('serafimkoshelev','scrypt:32768:8:1$sgrCnCBx6ftNrcHa$ea4c10abe16994424520985fbd149dd7cf6679f5b5808c107e99f06f1513a13e002ee61a1214720017887ee0dacf4c2d7ad3bde1805cb3080a76323c3686bfc2',624,NULL,'student'),('sharapovpanfil','scrypt:32768:8:1$hC2aGD7dfxX96XKT$af8c7646f9b6ad3591a361f059dfefed2a257f597871bd0fab2c214d389a345db47625f1c19f219a7ce4fc4123105116710e3c5ae620b91bf4558f29a3a0574a',634,NULL,'student'),('shcherbakovtvorimir','scrypt:32768:8:1$d0Y8lyR867JopY4m$1477be63f3211a52791677e26f77d1ce57dfa4c96b7aff613b016861bab4549f684e85c6b998498d7b337b82abd93668c4101d692de9dac861661ea2ed588ddc',536,NULL,'student'),('skorolev','scrypt:32768:8:1$0sZ9L3yqrbPn8TjE$9de3d547ce0a96894be11e1c5a09c331a5093cf07a8dc6c45269063bd64219d32b121ec3efff189f41d59da6e39fa862b79f80df368505b8a898760441b5851b',NULL,48,'teacher'),('solovevamarina','scrypt:32768:8:1$jrj517kO74DMOWky$d5b6b9b1cdf9be0419b2c0a4d169e37003d841bd5b030efa3e08f28b42c0097977c9d9e0fe51d45c3eb460362d9663826a31ad265e0f46b48c262ac0a9bf0f9a',583,NULL,'student'),('spartak71','scrypt:32768:8:1$w0ip21BWN6vQYpNZ$84be8b35a99731ea46532ddf3ef128cfe041ff46b1d148aebc7c1a42fe751b0858c3a4800e09417eaf875e853deb30086db17cb39d3d383ffe9fc26359ba7822',584,NULL,'student'),('stepan_71','scrypt:32768:8:1$8jsZKH7tbepPNOQ3$32bf7708718b4b5912effbc3a8444750dcc5b13e787a8da77a4e742c53854f998ed0a3fd235a78ebd97802dcbd05275a643474cc83dfef4f9cc8a5c2f2934145',645,NULL,'student'),('stojan_1998','scrypt:32768:8:1$qH3eKaUJkJ1xGxSR$d7c9f789258d2a46d8081dd136de5966e8cd73de80533403962f8078cc36aa0526f0390c8d46a9a59db58972e2daa8d202a79a8f257ad8be75d09eb3ac87be02',557,NULL,'student'),('suhanovcheslav','scrypt:32768:8:1$607IEveaZs6K3i7z$122e69db0f799a04dfc1f9084a6afe9f1af8b15c1c1ff0b22dce78df11ffd3b66ec576934ec1c0be9a3baa0317455119e2b1e07fe1d6254d51c8b6d4a4b052ad',598,NULL,'student'),('suhanovviktorin','scrypt:32768:8:1$6hVHXFFxWZFSJ0Kd$794033a56948d7f4139fef5fb1ef1866d98048ef0ed247985b16c5df819d84d5132877dddc4d2e1ecadbf2c01d0bf2339fecd9c1a75cfff3ce73243c9fbb9e0f',NULL,53,'teacher'),('svetozar_1975','scrypt:32768:8:1$1XWg3BPj3uWWOdTs$a85dbf04b262f3b3241d113da2df2edd90d06b97a4ed21d4c601b1cc767b142759036ab37085694d09caeff26426cb35644e11a9d38e9f505bd820a0552cc7a2',586,NULL,'student'),('t','scrypt:32768:8:1$Bgdiktrojby9xXcS$7a501a11fc843685c2b2c38234bdd1f33dc9ef52cec0a5b40375f7f5f450b6cceff8e6731096a4ced673a8682256ffa1d4c25c8e529b6ef45648a572c0b650dc',NULL,58,'teacher'),('taisija1991','scrypt:32768:8:1$hmnuatU1ai08LUJp$ba472db94933e266e12debe1f152d1372ccc162e9aa19f051a0aa304c52449cd13eaf396f6b5252d41c793c92ead368effc9582f29807000127e1067bb91d2e6',565,NULL,'student'),('tatjana48','scrypt:32768:8:1$ZpaYDEX4O1O6v6Qi$82a9618ec6d7fe19ec09ca3e4cf34bfc18a82a1e3a0973768dc8f9ef7bac166704840beae47e3a1545abab01993f056f3197e7b6b43a10a2c49a46cf82e81c67',580,NULL,'student'),('tihon_63','scrypt:32768:8:1$yBasbehf6bJATa3Z$fb3fe92a3c5efa8329cc3a4fc4d091fe2167bc2b3f6631e14dca9df8c03d344312bfd2eb4bf108c6e2366126819a439cee487c4c77c15eb59ddb6a6d82d0f175',622,NULL,'student'),('ustinovdenis','scrypt:32768:8:1$SatBuZQbMhwKdtff$6c516fa2e31f32ad421573e58706688e7f0fc9fc4248f11b8ae610209dab1a9b0288e0b0db3ed25c63b4cb4b0a1ea280f52a1c3763b42343ab3378b6031e5fca',619,NULL,'student'),('valerija_1994','scrypt:32768:8:1$kBDuAZF4BwBhsvZw$c9ca7e44a6db4a059c9e3e3bd1426844a281407309e1961825a70550f99bfe9d5428ae0d270c18b3ab559ff1c1b053e622eb4922c41faad652b272b56dc3cacf',599,NULL,'student'),('venedikt_38','scrypt:32768:8:1$QY4UPXUH59Wanm6f$da30efbc3698801f7b9edc18ffe31e8ff438f428e0998a1cda54d93dee4b2d425b58b81dcfecba16172a93e045ecfb17e84145d35506b800d55c73f51fffae25',573,NULL,'student'),('veselovavera','scrypt:32768:8:1$PGXvfGcQJJf6PHnq$19dbaddb09de91bd5d8f54e517f26f699ad9b75b2035d4372acddba52e859ca0c0df6f925ac0003e9ed42d31565068fa4637d86cd5145ec3300bbe5522382565',538,NULL,'student'),('veselovdanila','scrypt:32768:8:1$NcdGRVREIz76SrtT$de14e982deb877643d00b8bbdc2402d7ed983ad12ca95de7689b06c5d2533ee89f4b2f31e3d4d51c9eb68eafb3de3678d00b8d5e10ffae9255fc4d7723b16555',532,NULL,'student'),('viktor_42','scrypt:32768:8:1$bJkllyvRjslpZN38$223f9e32f90cadc656c48f14a2525a5b66199eb449ece96a14718bdf6d221401be41d0b01ffbe6eaf3fb4008d1ab4a4eb36c710a0d2454be09a91948c1ff8732',611,NULL,'student'),('vsemil93','scrypt:32768:8:1$M3ZyhUjIVq9YCCjy$45d51fe9aa4819dcbc46aad780a48be74456ce64678cd17aaf9f7284e24bc44c68374ae9b33e08deabd74c3ee3102fffce4e86eda1b0091d829779719dee7572',NULL,54,'teacher'),('xaleksandrova','scrypt:32768:8:1$FhUlBsQCA7sOlEf1$3c14970b3e490fe401feb0bf34f0d4ed4832f3ae41792569570a7a89d74b637ccf50738019e3fe3b5ac23154215d5282a291117c4da71ddaa6a50d4ca38e24fc',615,NULL,'student'),('zatsevernest','scrypt:32768:8:1$nlAMrO8T6mFuJMXz$f684e694e38fd947f816ef9ecb7b0fca9f6d6c4cc498416678bc5d469b9d95130ce84bf90a768d15db6393884502b95ba46f01214225d8c4160692a1159392ee',537,NULL,'student'),('zhdanovfedot','scrypt:32768:8:1$Z0X0tjkA4CdD04IH$e8e7ae5a6154fa1d3d53613b7b6942e7c923f7b79a572cc0efdc56cd8c63263fb6b2fb893ce44ebeaeb00105fb633bf00950d8862c44a77ed6bd7c609ed51607',636,NULL,'student'),('zhdanovrjurik','scrypt:32768:8:1$gu1XI2OPwBmNXId6$bf36e56cf436b7630810d4588724cc26ddc895a403ffa052cbf0837258227c08749d3ce282ee756aef961247aa26eddbc4370c8e86eed0d2ee7da0851284943d',577,NULL,'student'),('zosima1977','scrypt:32768:8:1$JJlVDWFPwfQFSEFF$dcce7cf5ab278f7c15018766114f41e1234ebf0546d2bd210ec6ef7c721f1287c4fa0d64f840aa5bbb23ab8532f6a9f3a20bb56694fa957e75e89f33d898fea4',533,NULL,'student');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (3,'Новое задание: Задание 1','2024-12-25 19:16:12','Добавлено новое задание: Задание 1. Срок сдачи: 25-12-2024. Описание: 123'),(4,'Новое задание: Задание 2','2024-12-25 19:16:17','Добавлено новое задание: Задание 2. Срок сдачи: 25-12-2024. Описание: 123'),(5,'Новое задание: Задание 3','2024-12-25 19:16:19','Добавлено новое задание: Задание 3. Срок сдачи: 25-12-2024. Описание: 123');
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program`
--

DROP TABLE IF EXISTS `program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `program` (
  `program` varchar(100) NOT NULL,
  PRIMARY KEY (`program`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program`
--

LOCK TABLES `program` WRITE;
/*!40000 ALTER TABLE `program` DISABLE KEYS */;
INSERT INTO `program` VALUES ('Машиностроение'),('Программное обеспечение и разработка'),('Экономика и управление');
/*!40000 ALTER TABLE `program` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program_subjects`
--

DROP TABLE IF EXISTS `program_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `program_subjects` (
  `program` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`program`,`subject`),
  KEY `subject_program_idx` (`subject`),
  CONSTRAINT `program_subject` FOREIGN KEY (`program`) REFERENCES `program` (`program`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `subject_program` FOREIGN KEY (`subject`) REFERENCES `subject` (`subject_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program_subjects`
--

LOCK TABLES `program_subjects` WRITE;
/*!40000 ALTER TABLE `program_subjects` DISABLE KEYS */;
INSERT INTO `program_subjects` VALUES ('Программное обеспечение и разработка','Алгоритмы и структуры данных'),('Экономика и управление','Анализ данных для бизнеса'),('Экономика и управление','Бизнес-аналитика'),('Программное обеспечение и разработка','Введение в машинное обучение'),('Машиностроение','Детали машин'),('Машиностроение','Инженерная графика'),('Программное обеспечение и разработка','Интернет вещей'),('Программное обеспечение и разработка','Компьютерные сети'),('Экономика и управление','Макроэкономика'),('Экономика и управление','Маркетинг'),('Машиностроение','Материаловедение'),('Машиностроение','Машиностроительные технологии'),('Экономика и управление','Микроэкономика'),('Программное обеспечение и разработка','Мобильная разработка'),('Программное обеспечение и разработка','Основы искусственного интеллекта'),('Программное обеспечение и разработка','Основы программирования'),('Экономика и управление','Основы экономической теории'),('Программное обеспечение и разработка','Проектирование программных систем'),('Программное обеспечение и разработка','Разработка веб-приложений'),('Программное обеспечение и разработка','Разработка пользовательского интерфейса'),('Машиностроение','САПР в машиностроении'),('Программное обеспечение и разработка','Системное программирование'),('Машиностроение','Теория машин и механизмов'),('Программное обеспечение и разработка','Тестирование и отладка программ'),('Машиностроение','Технологии 3D-печати в производстве'),('Программное обеспечение и разработка','Управление версиями и DevOps'),('Экономика и управление','Управление персоналом'),('Экономика и управление','Управление проектами'),('Экономика и управление','Финансовый учет'),('Машиностроение','Чертежное дело');
/*!40000 ALTER TABLE `program_subjects` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1,'2024-12-26 08:20:00','222','Анализ данных для бизнеса','Лекция',58,'МШС-102-52-00'),(2,'2024-12-26 10:00:00','222','Администрирование баз данных','Лекция',58,'МШС-102-52-00'),(3,'2024-12-26 11:45:00','222','Алгоритмы и структуры данных','Лекция',58,'МШС-102-52-00'),(4,'2024-12-26 08:20:00','232','Бизнес-аналитика','Лекция',52,'МШС-403-52-00'),(5,'2024-12-26 10:00:00','232','Детали машин','Лекция',54,'МШС-403-52-00'),(6,'2024-12-26 11:45:00','232','Бизнес-аналитика','Лекция',54,'МШС-403-52-00');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `st_groups`
--

DROP TABLE IF EXISTS `st_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `st_groups` (
  `idgroups` varchar(45) NOT NULL,
  `course` tinyint NOT NULL,
  `program` varchar(100) NOT NULL,
  PRIMARY KEY (`idgroups`),
  KEY `program_group_idx` (`program`),
  CONSTRAINT `program_group` FOREIGN KEY (`program`) REFERENCES `program` (`program`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `st_groups`
--

LOCK TABLES `st_groups` WRITE;
/*!40000 ALTER TABLE `st_groups` DISABLE KEYS */;
INSERT INTO `st_groups` VALUES ('МШС-102-52-00',1,'Машиностроение'),('МШС-103-52-00',1,'Машиностроение'),('МШС-104-52-00',1,'Машиностроение'),('МШС-202-52-00',2,'Машиностроение'),('МШС-203-52-00',2,'Машиностроение'),('МШС-204-52-00',2,'Машиностроение'),('МШС-302-52-00',3,'Машиностроение'),('МШС-303-52-00',3,'Машиностроение'),('МШС-304-52-00',3,'Машиностроение'),('МШС-402-52-00',4,'Машиностроение'),('МШС-403-52-00',4,'Машиностроение'),('МШС-404-52-00',4,'Машиностроение'),('ПОР-102-52-00',1,'Программное обеспечение и разработка'),('ПОР-103-52-00',1,'Программное обеспечение и разработка'),('ПОР-104-52-00',1,'Программное обеспечение и разработка'),('ПОР-202-52-00',2,'Программное обеспечение и разработка'),('ПОР-203-52-00',2,'Программное обеспечение и разработка'),('ПОР-204-52-00',2,'Программное обеспечение и разработка'),('ПОР-302-52-00',3,'Программное обеспечение и разработка'),('ПОР-303-52-00',3,'Программное обеспечение и разработка'),('ПОР-304-52-00',3,'Программное обеспечение и разработка'),('ПОР-402-52-00',4,'Программное обеспечение и разработка'),('ПОР-403-52-00',4,'Программное обеспечение и разработка'),('ПОР-404-52-00',4,'Программное обеспечение и разработка'),('ЭУП-102-52-00',1,'Экономика и управление'),('ЭУП-103-52-00',1,'Экономика и управление'),('ЭУП-104-52-00',1,'Экономика и управление'),('ЭУП-202-52-00',2,'Экономика и управление'),('ЭУП-203-52-00',2,'Экономика и управление'),('ЭУП-204-52-00',2,'Экономика и управление'),('ЭУП-302-52-00',3,'Экономика и управление'),('ЭУП-303-52-00',3,'Экономика и управление'),('ЭУП-304-52-00',3,'Экономика и управление'),('ЭУП-402-52-00',4,'Экономика и управление'),('ЭУП-403-52-00',4,'Экономика и управление'),('ЭУП-404-52-00',4,'Экономика и управление');
/*!40000 ALTER TABLE `st_groups` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `st_notification`
--

LOCK TABLES `st_notification` WRITE;
/*!40000 ALTER TABLE `st_notification` DISABLE KEYS */;
INSERT INTO `st_notification` VALUES (578,3,0),(578,4,0),(578,5,0),(616,3,0),(616,4,0),(616,5,0);
/*!40000 ALTER TABLE `st_notification` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=648 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (527,'Колокольчиков Артем Олегович','МШС-403-52-00','2024-12-25',NULL,NULL),(528,'г-жа Самойлова Ульяна Мироновна','ПОР-303-52-00','1974-07-29',NULL,NULL),(529,'Филиппов Кузьма Марсович','ЭУП-102-52-00','1965-05-20',NULL,NULL),(530,'Раиса Андреевна Никифорова','ПОР-402-52-00','1976-02-01',NULL,NULL),(531,'Тамара Александровна Дорофеева','ПОР-103-52-00','1976-05-25',NULL,NULL),(532,'Митофан Ерофеевич Кононов','ЭУП-302-52-00','1977-04-18',NULL,NULL),(533,'Максимов Григорий Всеволодович','МШС-304-52-00','2006-08-04',NULL,NULL),(534,'Спартак Марсович Романов','ЭУП-203-52-00','1982-03-23',NULL,NULL),(535,'Любовь Рудольфовна Никонова','ЭУП-403-52-00','1971-11-15',NULL,NULL),(536,'Суханов Архип Фёдорович','ЭУП-302-52-00','2005-03-09',NULL,NULL),(537,'Лора Сергеевна Баранова','ПОР-404-52-00','1985-12-21',NULL,NULL),(538,'Соболева Глафира Святославовна','ЭУП-203-52-00','1984-04-21',NULL,NULL),(539,'Анатолий Игнатьевич Маслов','ПОР-302-52-00','2005-03-23',NULL,NULL),(540,'Всеслав Анатольевич Куликов','ПОР-304-52-00','1965-03-26',NULL,NULL),(541,'Волков Анисим Юльевич','МШС-103-52-00','1999-07-29',NULL,NULL),(542,'Меркушева Лидия Аскольдовна','ЭУП-303-52-00','1989-01-30',NULL,NULL),(543,'Анисимов Пантелеймон Алексеевич','МШС-303-52-00','1967-10-30',NULL,NULL),(544,'Ким Ярославович Фомин','МШС-104-52-00','1967-04-05',NULL,NULL),(545,'Якушева Лора Архиповна','ПОР-402-52-00','1984-08-31',NULL,NULL),(546,'Софрон Изотович Поляков','ПОР-203-52-00','2004-12-22',NULL,NULL),(547,'Мухина Лора Яковлевна','МШС-104-52-00','1982-10-09',NULL,NULL),(548,'Изяслав Всеволодович Комаров','ЭУП-404-52-00','2003-07-15',NULL,NULL),(549,'Фортунат Филатович Меркушев','ПОР-303-52-00','1997-07-03',NULL,NULL),(550,'Костин Виссарион Яковлевич','МШС-302-52-00','1970-11-19',NULL,NULL),(551,'Федосеева Фаина Васильевна','ЭУП-303-52-00','1998-07-05',NULL,NULL),(552,'Олег Валерианович Рыбаков','ЭУП-304-52-00','1986-10-08',NULL,NULL),(553,'Филиппова Алла Федоровна','ПОР-204-52-00','1976-09-24',NULL,NULL),(554,'Марина Геннадиевна Зимина','МШС-303-52-00','1981-03-05',NULL,NULL),(555,'Лукия Алексеевна Колесникова','ПОР-304-52-00','1989-04-22',NULL,NULL),(556,'Вера Евгеньевна Ильина','ПОР-404-52-00','1982-11-13',NULL,NULL),(557,'Алина Семеновна Шарова','ЭУП-103-52-00','1986-12-25',NULL,NULL),(558,'Мясников Изот Дорофеевич','МШС-304-52-00','1995-09-27',NULL,NULL),(559,'Агафонов Агап Федосеевич','ПОР-104-52-00','2006-03-17',NULL,NULL),(560,'Эммануил Богданович Николаев','ПОР-204-52-00','1985-07-11',NULL,NULL),(561,'Федосеев Валентин Игнатьевич','ПОР-204-52-00','1996-02-11',NULL,NULL),(562,'Анисимова Маргарита Романовна','ЭУП-203-52-00','1983-12-25',NULL,NULL),(563,'Дарья Ждановна Меркушева','МШС-404-52-00','1966-09-16',NULL,NULL),(564,'Белякова Фёкла Георгиевна','ПОР-203-52-00','1964-04-01',NULL,NULL),(565,'Фокина Ольга Юрьевна','МШС-103-52-00','1967-01-11',NULL,NULL),(566,'Кондратьев Мирон Ярославович','МШС-403-52-00','2004-11-02',NULL,NULL),(567,'Анжелика Болеславовна Никифорова','МШС-204-52-00','1982-05-08',NULL,NULL),(568,'Анна Семеновна Костина','МШС-302-52-00','1966-04-26',NULL,NULL),(569,'Лазарев Лучезар Даниилович','ПОР-304-52-00','1992-11-06',NULL,NULL),(570,'Логинов Якуб Алексеевич','ЭУП-404-52-00','1983-02-26',NULL,NULL),(571,'Сафонова Иванна Юрьевна','ПОР-404-52-00','2008-05-21',NULL,NULL),(572,'Котова Таисия Георгиевна','ПОР-104-52-00','1973-07-12',NULL,NULL),(573,'Евдокия Федоровна Колесникова','ЭУП-202-52-00','1985-03-29',NULL,NULL),(574,'Владимир Архипович Афанасьев','ЭУП-202-52-00','1966-09-28',NULL,NULL),(575,'Олимпиада Яковлевна Комиссарова','ПОР-102-52-00','1989-12-20',NULL,NULL),(576,'Исаева Анна Сергеевна','МШС-302-52-00','1969-04-22',NULL,NULL),(577,'Кудряшова Галина Александровна','ЭУП-302-52-00','1984-10-03',NULL,NULL),(578,'Елизавета Кирилловна Смирнова','МШС-102-52-00','1970-03-07',NULL,NULL),(579,'Сорокина Евпраксия Тарасовна','ПОР-402-52-00','1977-07-18',NULL,NULL),(580,'Кир Теймуразович Бобров','ЭУП-104-52-00','1977-11-08',NULL,NULL),(581,'Щукина Лукия Яковлевна','МШС-104-52-00','1989-04-20',NULL,NULL),(582,'Севастьян Валерьевич Белоусов','МШС-303-52-00','1986-01-05',NULL,NULL),(583,'Симонов Доброслав Давыдович','ПОР-403-52-00','1978-08-13',NULL,NULL),(584,'Артемьева Анжела Степановна','ЭУП-102-52-00','1972-03-18',NULL,NULL),(585,'Александра Рудольфовна Шашкова','ПОР-402-52-00','1978-06-05',NULL,NULL),(586,'Гуляев Федор Захарьевич','ЭУП-104-52-00','1977-01-09',NULL,NULL),(587,'Новикова Татьяна Павловна','ПОР-404-52-00','1971-12-10',NULL,NULL),(588,'Абрамов Исидор Ануфриевич','ЭУП-204-52-00','1991-04-08',NULL,NULL),(589,'Поликарп Архипович Мухин','МШС-104-52-00','1980-05-22',NULL,NULL),(590,'Тихонова Кира Борисовна','ЭУП-402-52-00','2007-10-23',NULL,NULL),(591,'Фома Артёмович Ефремов','МШС-302-52-00','1975-01-06',NULL,NULL),(592,'Беспалов Пимен Антонович','ЭУП-104-52-00','1996-06-10',NULL,NULL),(593,'Емельянов Кузьма Давидович','ЭУП-103-52-00','1999-02-18',NULL,NULL),(594,'Беспалова Олимпиада Тимуровна','ПОР-302-52-00','1972-01-30',NULL,NULL),(595,'Ананий Гертрудович Комаров','ЭУП-104-52-00','1969-07-30',NULL,NULL),(596,'Пестова Евдокия Яковлевна','ПОР-302-52-00','2002-04-01',NULL,NULL),(597,'Кириллова Василиса Владимировна','ЭУП-303-52-00','1996-09-05',NULL,NULL),(598,'Ксения Валериевна Лыткина','МШС-302-52-00','1992-03-22',NULL,NULL),(599,'Лидия Степановна Шашкова','МШС-203-52-00','1971-12-16',NULL,NULL),(600,'Красильникова Алла Львовна','ПОР-104-52-00','1968-04-25',NULL,NULL),(601,'Мухин Родион Анатольевич','МШС-302-52-00','1968-07-09',NULL,NULL),(602,'Натан Тихонович Казаков','МШС-202-52-00','1993-02-21',NULL,NULL),(603,'Валентина Станиславовна Рябова','ПОР-104-52-00','1985-04-29',NULL,NULL),(604,'Одинцов Дорофей Елизарович','ЭУП-204-52-00','2006-01-12',NULL,NULL),(605,'Терентьев Поликарп Анисимович','ПОР-302-52-00','1980-11-28',NULL,NULL),(606,'Васильева Нина Тимуровна','ЭУП-202-52-00','2001-07-14',NULL,NULL),(607,'Степан Гурьевич Емельянов','ПОР-402-52-00','1999-06-11',NULL,NULL),(608,'Валентин Валерианович Дроздов','ЭУП-402-52-00','1981-06-19',NULL,NULL),(609,'Комиссарова Олимпиада Кирилловна','ЭУП-104-52-00','1973-01-11',NULL,NULL),(610,'Авдеев Любосмысл Теймуразович','ЭУП-204-52-00','1984-09-03',NULL,NULL),(611,'Гущина Марфа Ивановна','ЭУП-203-52-00','1993-04-15',NULL,NULL),(612,'Ангелина Владимировна Щербакова','МШС-103-52-00','1973-10-14',NULL,NULL),(613,'Овчинников Панкрат Харитонович','ЭУП-302-52-00','1977-07-22',NULL,NULL),(614,'Святополк Аксёнович Рожков','ЭУП-204-52-00','1991-02-11',NULL,NULL),(615,'Филарет Андреевич Капустин','МШС-404-52-00','1992-09-30',NULL,NULL),(616,'Степан Адрианович Григорьев','МШС-102-52-00','1967-01-09',NULL,NULL),(617,'Колобова Ираида Алексеевна','ЭУП-204-52-00','1989-10-30',NULL,NULL),(618,'Зыков Олег Марсович','ЭУП-303-52-00','1991-08-05',NULL,NULL),(619,'Гаврилова Нина Викторовна','ЭУП-402-52-00','1994-06-07',NULL,NULL),(620,'Ирина Ефимовна Лаврентьева','МШС-304-52-00','1990-10-25',NULL,NULL),(621,'Тамара Кузьминична Крюкова','ПОР-102-52-00','1978-03-19',NULL,NULL),(622,'Петр Валерьянович Селиверстов','МШС-202-52-00','1969-03-29',NULL,NULL),(623,'Селиверстов Терентий Архипович','МШС-104-52-00','2002-06-30',NULL,NULL),(624,'Симон Данилович Суханов','ПОР-103-52-00','1986-04-28',NULL,NULL),(625,'Викторин Гаврилович Юдин','ЭУП-302-52-00','1998-07-27',NULL,NULL),(626,'Морозов Азарий Жоресович','МШС-103-52-00','2006-06-19',NULL,NULL),(627,'Бобылева Нинель Валериевна','ЭУП-204-52-00','1975-12-22',NULL,NULL),(628,'Ираида Олеговна Егорова','ПОР-304-52-00','1997-07-09',NULL,NULL),(629,'Дарья Макаровна Суворова','МШС-203-52-00','1989-06-13',NULL,NULL),(630,'Тамара Львовна Ефремова','МШС-104-52-00','1973-04-17',NULL,NULL),(631,'Панова Анна Руслановна','МШС-202-52-00','1990-02-28',NULL,NULL),(632,'Исидор Артурович Борисов','ПОР-402-52-00','1969-07-13',NULL,NULL),(633,'Сысоев Фортунат Валерианович','ЭУП-304-52-00','1967-10-09',NULL,NULL),(634,'Петрова Феврония Константиновна','ЭУП-102-52-00','2008-05-23',NULL,NULL),(635,'Кузьма Филимонович Ильин','ПОР-204-52-00','1975-11-18',NULL,NULL),(636,'Милица Федоровна Тимофеева','ЭУП-404-52-00','1992-12-14',NULL,NULL),(637,'Морозова Варвара Андреевна','ПОР-203-52-00','1970-11-08',NULL,NULL),(638,'Кира Артемовна Волкова','ЭУП-203-52-00','1988-05-10',NULL,NULL),(639,'Вячеслав Артёмович Андреев','МШС-302-52-00','1987-03-10',NULL,NULL),(640,'Екатерина Харитоновна Константинова','ПОР-104-52-00','2001-09-30',NULL,NULL),(641,'Пестов Дорофей Валерьянович','МШС-304-52-00','2007-08-14',NULL,NULL),(642,'Симон Афанасьевич Лебедев','МШС-103-52-00','1964-10-04',NULL,NULL),(643,'Блинов Аникей Архипович','ЭУП-102-52-00','1999-04-12',NULL,NULL),(644,'Христофор Изотович Федотов','ЭУП-402-52-00','1999-11-11',NULL,NULL),(645,'Прасковья Константиновна Михайлова','ЭУП-302-52-00','1980-12-13',NULL,NULL),(646,'г-жа Меркушева Оксана Тимуровна','ЭУП-303-52-00','1978-02-03',NULL,NULL),(647,'Хохлов Тимур Зиновьевич','МШС-203-52-00','1965-09-02',NULL,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `student_tasks`
--

LOCK TABLES `student_tasks` WRITE;
/*!40000 ALTER TABLE `student_tasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_tasks` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES ('Администрирование баз данных'),('Алгоритмы и структуры данных'),('Анализ данных для бизнеса'),('Бизнес-аналитика'),('Введение в машинное обучение'),('Детали машин'),('Инженерная графика'),('Интернет вещей'),('Кибербезопасность'),('Компьютерные сети'),('Макроэкономика'),('Маркетинг'),('Материаловедение'),('Машиностроительные технологии'),('Микроэкономика'),('Мобильная разработка'),('Облачные вычисления'),('Основы информационных технологий'),('Основы искусственного интеллекта'),('Основы программирования'),('Основы экономической теории'),('Проектирование программных систем'),('Разработка веб-приложений'),('Разработка пользовательского интерфейса'),('САПР в машиностроении'),('Системное программирование'),('Теория машин и механизмов'),('Тестирование и отладка программ'),('Технологии 3D-печати в производстве'),('Управление версиями и DevOps'),('Управление персоналом'),('Управление проектами'),('Финансовый учет'),('Чертежное дело');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (48,'Октябрина Артемовна Константинова','1971-01-17','88262031380'),(49,'Стрелкова София Сергеевна','2001-07-19','+7 976 148 27 70'),(50,'Соломон Яковлевич Филиппов','1989-10-30','8 (294) 237-74-44'),(51,'Сидорова Мария Станиславовна','2005-07-11','+7 512 554 9022'),(52,'Зимина Екатерина Степановна','1989-09-25','+7 842 597 7108'),(53,'Анастасия Антоновна Кононова','1965-04-11','+7 651 086 69 77'),(54,'Анжела Ефимовна Андреева','1969-09-20','8 (527) 213-6496'),(55,'Рыбаков Милован Гурьевич','1995-06-01','+7 524 778 04 67'),(56,'Татьяна Ильинична Никифорова','1990-06-30','+7 (756) 947-96-47'),(57,'Максим Всеволодович Гуляев','1984-01-29','+7 (615) 625-01-92'),(58,'Akdjasd','2024-12-25','243445343');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Dumping data for table `teacher_subjects`
--

LOCK TABLES `teacher_subjects` WRITE;
/*!40000 ALTER TABLE `teacher_subjects` DISABLE KEYS */;
INSERT INTO `teacher_subjects` VALUES (48,'Введение в машинное обучение'),(49,'Проектирование программных систем'),(50,'Машиностроительные технологии'),(50,'Облачные вычисления'),(51,'Детали машин'),(51,'Инженерная графика'),(52,'Компьютерные сети'),(53,'САПР в машиностроении'),(54,'Материаловедение'),(54,'Теория машин и механизмов'),(55,'Анализ данных для бизнеса'),(55,'Основы информационных технологий'),(56,'Детали машин'),(56,'Инженерная графика'),(57,'Бизнес-аналитика'),(58,'Администрирование баз данных'),(58,'Алгоритмы и структуры данных'),(58,'Анализ данных для бизнеса');
/*!40000 ALTER TABLE `teacher_subjects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-26  0:56:15
