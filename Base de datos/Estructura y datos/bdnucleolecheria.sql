-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2022 at 02:43 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdnucleolecheria`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumno`
--

CREATE TABLE `alumno` (
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ci_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nombres` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `apellidos` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `edad` int(11) NOT NULL,
  `id_programa` int(11) NOT NULL,
  `nivel` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sexo` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `direccion` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `instrumento_principal` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `alumno`
--

INSERT INTO `alumno` (`cod_alumno`, `ci_alumno`, `nombres`, `apellidos`, `edad`, `id_programa`, `nivel`, `sexo`, `fecha_nacimiento`, `direccion`, `instrumento_principal`) VALUES
('A2030', '27899445', 'Castiel', 'Thompson', 25, 1, 'juvenil', 'M', '1999-12-20', 'Olivos los naranjos', 'Cuatro criollo'),
('A2031', '32445678', 'Benito el bueno', 'dominguez', 12, 2, 'juvenil', 'M', '2010-06-12', 'Casas bote C', 'Flauta transversa'),
('A2032', '30789021', 'Shantal', 'Alberich', 10, 3, 'Infantil', 'F', '2011-01-02', 'Madre vieja', 'Fagot'),
('A2033', '28677899', 'Alejandro', 'Villarroel', 20, 1, 'Juvenil', 'M', '2000-03-02', 'Lechería', 'Mandolina'),
('A2034', '', 'Andrés José', 'Marcano Mendoza', 7, 4, 'Inicial', 'M', '2015-10-01', 'Potocos', 'Canto'),
('A2035', '32400899', 'Juanito Alcachofa', 'Cabezas', 10, 6, 'Inicial', 'M', '2011-01-20', 'Barrio venezuela', 'Canto'),
('A2036', '26980455', 'Emperatriz', 'Del carmen', 24, 2, 'Juvenil', 'F', '1996-01-20', 'Casa bote C', 'Contrabajo');

-- --------------------------------------------------------

--
-- Table structure for table `alumno_asistencia`
--

CREATE TABLE `alumno_asistencia` (
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ausente_presente` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `id_asistencia` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `alumno_asistencia`
--

INSERT INTO `alumno_asistencia` (`cod_alumno`, `ausente_presente`, `id_asistencia`) VALUES
('A2030', 'P', '1'),
('A2030', 'A', '2'),
('A2031', 'P', '1');

-- --------------------------------------------------------

--
-- Table structure for table `asistencia`
--

CREATE TABLE `asistencia` (
  `id_asistencia` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cedula_identidad` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `fecha` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_final` time NOT NULL,
  `id_programa` int(11) NOT NULL,
  `id_clase` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `asistencia`
--

INSERT INTO `asistencia` (`id_asistencia`, `cedula_identidad`, `fecha`, `hora_inicio`, `hora_final`, `id_programa`, `id_clase`) VALUES
('1', '25301157', '2021-10-27', '14:00:00', '16:00:00', 2, '3'),
('2', '12309843', '2021-10-26', '14:00:00', '16:00:00', 2, '8');

-- --------------------------------------------------------

--
-- Table structure for table `cargo`
--

CREATE TABLE `cargo` (
  `id_cargo` int(11) NOT NULL,
  `nombre_cargo` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `cargo`
--

INSERT INTO `cargo` (`id_cargo`, `nombre_cargo`) VALUES
(1, 'Director de núcleo'),
(2, 'Instructor'),
(3, 'Coordinador de área'),
(4, 'Coordinador general'),
(5, 'Secretaria');

-- --------------------------------------------------------

--
-- Table structure for table `clase`
--

CREATE TABLE `clase` (
  `id_clase` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Catedra` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cedula_identidad` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `id_programa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `clase`
--

INSERT INTO `clase` (`id_clase`, `Catedra`, `cedula_identidad`, `id_programa`) VALUES
('1', 'Cuatro inicial', '30090301', 1),
('11', 'Iniciación', '28900334', 4),
('12', 'Mandolina', '24999777', 1),
('13', 'Nivel I', '10225667', 6),
('14', 'Flauta infantil', '27072631', 3),
('15', 'Flauta inicial', '27072631', 6),
('16', 'Flauta Juvenil', '27072631', 2),
('2', 'Violin inicial', '26900789', 6),
('3', 'Flauta juvenil', '25301157', 2),
('4', 'Ensayo orq infantil', '26900789', 3),
('5', 'Ensayo orq alma llanera', '27072631', 1),
('7', 'Ensayo coral adulto', '24999777', 5),
('8', 'Ensayo orq juvenil', '12309843', 2),
('9', 'Cello', '30044247', 3);

-- --------------------------------------------------------

--
-- Table structure for table `clase_alumno`
--

CREATE TABLE `clase_alumno` (
  `id_clase` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `clase_alumno`
--

INSERT INTO `clase_alumno` (`id_clase`, `cod_alumno`) VALUES
('11', 'A2034'),
('12', 'A2033'),
('16', 'A2031'),
('3', 'A2031'),
('4', 'A2032'),
('5', 'A2030'),
('5', 'A2033'),
('5', 'A2035'),
('8', 'A2031');

-- --------------------------------------------------------

--
-- Table structure for table `evaluacion`
--

CREATE TABLE `evaluacion` (
  `id_evaluacion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `fecha` date NOT NULL,
  `id_clase` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `trimestre` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `cedula_identidad` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `evaluacion`
--

INSERT INTO `evaluacion` (`id_evaluacion`, `fecha`, `id_clase`, `trimestre`, `cedula_identidad`) VALUES
('1112', '2021-04-22', '9', '1', '30044247'),
('1222', '2021-10-04', '1', '1', '25301157'),
('1223', '2021-10-27', '1', '2', '30090301'),
('1224', '2021-06-15', '9', '2', '30044247'),
('E21', '2022-06-06', '5', '3', '27072631'),
('E3', '2022-06-14', '14', '3', '27072631');

-- --------------------------------------------------------

--
-- Table structure for table `evaluacion_alumno`
--

CREATE TABLE `evaluacion_alumno` (
  `id_evaluacion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `nota` float NOT NULL,
  `cod_alumno` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `evaluacion_alumno`
--

INSERT INTO `evaluacion_alumno` (`id_evaluacion`, `nota`, `cod_alumno`) VALUES
('1112', 20, 'A2035'),
('1222', 12.5, 'A2030'),
('1223', 20, 'A2030'),
('1224', 14, 'A2035'),
('E21', 20, 'A2030'),
('E21', 18, 'A2033'),
('E21', 10.6, 'A2035');

-- --------------------------------------------------------

--
-- Table structure for table `instrumento`
--

CREATE TABLE `instrumento` (
  `num_serial` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `marca` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `medida` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `accesorio` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `condicion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `ubicacion` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `procedencia` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `comodato_vigente` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `cod_inventario` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `instrumento`
--

INSERT INTO `instrumento` (`num_serial`, `descripcion`, `marca`, `medida`, `accesorio`, `condicion`, `ubicacion`, `procedencia`, `comodato_vigente`, `cod_inventario`) VALUES
('NL20399990', 'Corno', 'Mendini', 'N/A', 'estuche', 'OPERATIVO', 'Depósito', 'FMSB', 'NO', '789009000080'),
('NL23333345', 'Corno Ingle', 'Yamaha', 'N/A', 'Estuche', 'OPERATIVO', 'Nucleo', 'FMSB', 'NO', '789009000002'),
('NL23333346', 'Flauta Tran', 'Arioso', 'N/A', 'estuche', 'OPERATIVO', 'comodato', 'FMSB', 'NO', '904555656436'),
('NL256666674', 'Contrabajo', 'Mendini', '3/4', 'Arco', 'OPERATIVO', 'Núcleo', 'FMSB', 'SI', '789990090909'),
('NL30222223', 'Violin', 'Mendini', '3/4', 'arco', 'OPERATIVO', 'Comodato', 'FMSB', 'SI', '789000900901'),
('NL987777776', 'Mandolina', 'Brokliyn', 'N/A', 'Estuche', 'OPERATIVO', 'Comodato', 'FMSB', 'SI', '789666356667');

-- --------------------------------------------------------

--
-- Table structure for table `instrumento_alumno`
--

CREATE TABLE `instrumento_alumno` (
  `num_serial` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `en_posesion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `instrumento_alumno`
--

INSERT INTO `instrumento_alumno` (`num_serial`, `en_posesion`, `cod_alumno`) VALUES
('NL23333346', 'NO', 'A2031'),
('NL256666674', 'SI', 'A2036'),
('NL987777776', 'SI', 'A2033');

-- --------------------------------------------------------

--
-- Table structure for table `profesor`
--

CREATE TABLE `profesor` (
  `cedula_identidad` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nombres` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `apellidos` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `direccion` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `edad` int(12) NOT NULL,
  `rif` varchar(11) COLLATE utf8_unicode_520_ci NOT NULL,
  `email` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `sexo` varchar(5) COLLATE utf8_unicode_520_ci NOT NULL,
  `id_cargo` int(15) NOT NULL,
  `id_programa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `profesor`
--

INSERT INTO `profesor` (`cedula_identidad`, `nombres`, `apellidos`, `telefono`, `direccion`, `fecha_ingreso`, `fecha_nacimiento`, `edad`, `rif`, `email`, `sexo`, `id_cargo`, `id_programa`) VALUES
('10225667', 'Daritza', 'Barrero', '04218990090', 'Lecheria', '2015-09-07', '1975-07-11', 47, '10225667-0', 'dbarrero@elsistema.org.ve', 'F', 2, 4),
('111111', 'default', 'admin', '', '', '0000-00-00', '0000-00-00', 0, '', '', '', 4, 1),
('12309843', 'Marianela', 'Utrera Garcia', '4126778900', 'Nueva barcelona', '1990-01-01', '1975-07-11', 47, '12309843-0', 'marianela.utrera@elsistema.org', 'F', 1, 2),
('17900320', 'Daniel', 'Sarmiento', '4248999000', 'Barrio venezuela', '2015-09-07', '1980-07-07', 41, '17900320-0', 'lsarmiento@elsistema.org.ve', 'M', 3, 8),
('222222', 'default', 'profesor', '', '', '0000-00-00', '0000-00-00', 0, '', '', '', 2, 2),
('23900458', 'Mario Porte', 'Scalanti Timo', '412890789', 'Portorozo', '1990-12-02', '1968-06-20', 79, '23900456-0', 'm.scala@elsistema.org.ve', 'M', 2, 5),
('24999777', 'Felix Daniel', 'Campos Noza', '4245678990', 'Puerto la cruz', '2010-02-13', '1996-06-15', 25, '24999777-0', 'ffcampos@elsistema.org.ve', 'M', 2, 7),
('25301157', 'Carlos Eduardo', 'Clavier Paéz', '04248293312', 'Nueva barcelona', '2015-09-07', '1996-06-15', 25, '25301157-0', 'cclavier@elsistema.org.ve', 'M', 2, 5),
('26900789', 'Rosnelly', 'Romero', '0412678900', 'Barcelona', '2015-09-07', '1996-09-20', 25, '26900789-0', 'r.romero@elsistema.org.ve', 'F', 2, 4),
('27072631', 'Ariadna de Jesus', 'Alvizu Abreu', '04248507777', 'Barcelona', '2015-09-07', '1999-08-30', 22, '27072631-0', 'aalvizu@elsistema.org.ve', 'F', 2, 1),
('28098332', 'Marielvic', 'Fernandez', '04248760092', 'Nueva barcelona', '2015-09-07', '1996-02-10', 25, '28098332-0', 'm.fernandez@elsistema.org.ve', 'F', 2, 3),
('28900334', 'Ada Valentina', 'Carías Sanchez', '412345688', 'Barcelona', '2015-09-07', '2000-08-20', 19, '28900334-0', 'adita@elsistema.org.ve', 'F', 2, 3),
('30044247', 'Emily ', 'Quilarque', '04245667788', 'Lecheria', '2015-09-07', '2000-06-12', 21, '30044247-0', 'equilarque@elsistema.ofg.ve', 'F', 2, 3),
('30090301', 'Stefania', 'Henriquez', '04146789922', 'Lecheria', '2015-09-07', '2001-01-02', 19, '30090301-0', 'shenriquez@elsistema.org.ve', 'F', 2, 1),
('30455788', 'Emilio', 'Nazoa', '4249802222', 'Clarines', '2010-11-01', '1993-05-10', 25, '30455788-0', 'emiNazo23@gmail.com', 'M', 2, 1),
('30789999', 'Emilo', 'Lestrade', '045678889', 'Camalia', '2012-12-04', '1998-04-20', 23, '30789999-0', 'em.l@elsistema.org.ve', 'M', 2, 6),
('34890778', 'Shantal Viola', 'Lestrade Scarlett', '4135678900', 'Los ventabales', '2021-11-12', '1990-10-06', 32, '34890778-0', 'sh.lestrade@elsistema.org.ve', 'F', 2, 6),
('9034677', 'Maria Alejandra', 'Rojas Rivas', '412356778', 'Puerto la cruz', '1990-08-23', '1972-07-11', 51, '9034677-0', 'mrojas@elsistema.org.ve', 'F', 4, 8);

-- --------------------------------------------------------

--
-- Table structure for table `programa`
--

CREATE TABLE `programa` (
  `id_programa` int(11) NOT NULL,
  `nombre_programa` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `programa`
--

INSERT INTO `programa` (`id_programa`, `nombre_programa`) VALUES
(1, 'Alma llanera'),
(2, 'Sinfónico juvenil'),
(3, 'Sinfónico infantil'),
(4, 'Kinder musical'),
(5, 'Coral juvenil'),
(6, 'Iniciación a la música'),
(7, 'Coral adulto'),
(8, 'Administración'),
(15, 'Afroamericano'),
(17, 'Manos Blancas');

-- --------------------------------------------------------

--
-- Table structure for table `representante`
--

CREATE TABLE `representante` (
  `ci_representante` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nombres` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `apellidos` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `telefono_celular` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `telefono_fijo` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `profesion` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ocupacion` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `vive_con_alumno` varchar(5) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `filiacion_representado` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `direccion` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `representante`
--

INSERT INTO `representante` (`ci_representante`, `nombres`, `apellidos`, `telefono_celular`, `telefono_fijo`, `profesion`, `ocupacion`, `vive_con_alumno`, `filiacion_representado`, `direccion`) VALUES
('10335467', 'Simon Jose Antonio', 'Alvizu Diaz', '04148256406', '02812715891', 'ing mecanico', 'Gerente de operacion', 'SI', 'padre', 'Barcelona, Fundaciòn Mendoza'),
('12456789', 'Maria Josefa', 'Cabezas', '04256789900', '0281345666', 'Pintora', 'Ama de casa', 'SI', 'Tía', 'Madre vieja'),
('13900788', 'Camacaro', 'López', '0424673333', '0281256443', 'Doctor', 'cirujano', 'SI', 'Tío', 'Canto claro'),
('15400988', 'Luz', 'Mendoza', '04246578899', '', 'Veterinaria', 'ama de casa', 'SI', 'Madre', 'Colinas nevery'),
('18809963', 'Adlino', 'Marcano', '0424678999', '0281345666', 'Ing de sistemas', 'gerente', 'NO', 'Padre', 'Canto claro');

-- --------------------------------------------------------

--
-- Table structure for table `representante_alumno`
--

CREATE TABLE `representante_alumno` (
  `ci_representante` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `representante_alumno`
--

INSERT INTO `representante_alumno` (`ci_representante`, `cod_alumno`) VALUES
('12456789', 'A2035'),
('15400988', 'A2034'),
('18809963', 'A2034');

-- --------------------------------------------------------

--
-- Table structure for table `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `privilegio` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `funcion` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`privilegio`, `funcion`) VALUES
('1_admin', 'Administrador'),
('2_profe', 'Profesor');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `nombres` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `apellidos` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `contraseña` varchar(70) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `privilegio` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cedula_identidad` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nombre_usuario` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`nombres`, `apellidos`, `contraseña`, `privilegio`, `cedula_identidad`, `nombre_usuario`) VALUES
('default', 'admin', '1111', '1_admin', '111111', 'admin'),
('Ariadna', 'Alvizu', 'Asi', '1_admin', '27072631', 'Ari'),
('Ariadna', 'Alvizu', '1515', '2_profe', '27072631', 'Ari2763'),
('Carlos', 'Clavier', 'Pal', '2_profe', '25301157', 'Carlos2530'),
('Felix Ramon', 'Campos', '1414', '2_profe', '9034677', 'FelxRM'),
('Leoncio', 'Martinez', 'Palinka', '1_admin', '10225667', 'LeonMart'),
('Mariano', 'Ramírez', '9090', '1_admin', '28098332', 'Ming'),
('Marianela', 'Utrera', '1212', '1_admin', '12309843', 'Nela'),
('default', 'profesor', '2222', '2_profe', '222222', 'profe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumno`
--
ALTER TABLE `alumno`
  ADD PRIMARY KEY (`cod_alumno`),
  ADD KEY `id_programa` (`id_programa`),
  ADD KEY `Unica` (`ci_alumno`) USING BTREE,
  ADD KEY `cod_alumno` (`cod_alumno`);

--
-- Indexes for table `alumno_asistencia`
--
ALTER TABLE `alumno_asistencia`
  ADD PRIMARY KEY (`cod_alumno`,`id_asistencia`),
  ADD KEY `ci_alumno` (`cod_alumno`),
  ADD KEY `id_asistencia` (`id_asistencia`);

--
-- Indexes for table `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `cedula_identidad` (`cedula_identidad`),
  ADD KEY `id_programa` (`id_programa`),
  ADD KEY `id_clase` (`id_clase`);

--
-- Indexes for table `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`id_cargo`);

--
-- Indexes for table `clase`
--
ALTER TABLE `clase`
  ADD PRIMARY KEY (`id_clase`),
  ADD KEY `id_programa` (`id_programa`),
  ADD KEY `cedula_identidad` (`cedula_identidad`);

--
-- Indexes for table `clase_alumno`
--
ALTER TABLE `clase_alumno`
  ADD PRIMARY KEY (`id_clase`,`cod_alumno`),
  ADD KEY `id_clase` (`id_clase`),
  ADD KEY `ci_alumno` (`cod_alumno`);

--
-- Indexes for table `evaluacion`
--
ALTER TABLE `evaluacion`
  ADD PRIMARY KEY (`id_evaluacion`),
  ADD KEY `cedula_identidad` (`cedula_identidad`),
  ADD KEY `id_clase` (`id_clase`),
  ADD KEY `trimestre` (`trimestre`);

--
-- Indexes for table `evaluacion_alumno`
--
ALTER TABLE `evaluacion_alumno`
  ADD PRIMARY KEY (`id_evaluacion`,`cod_alumno`),
  ADD KEY `ci_alumno` (`cod_alumno`),
  ADD KEY `id_evaluacion` (`id_evaluacion`);

--
-- Indexes for table `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`num_serial`,`cod_inventario`);

--
-- Indexes for table `instrumento_alumno`
--
ALTER TABLE `instrumento_alumno`
  ADD PRIMARY KEY (`num_serial`,`cod_alumno`),
  ADD UNIQUE KEY `num_serial_2` (`num_serial`),
  ADD KEY `num_serial` (`num_serial`),
  ADD KEY `cod_alumno` (`cod_alumno`);

--
-- Indexes for table `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`cedula_identidad`),
  ADD UNIQUE KEY `cedula_identidad` (`cedula_identidad`),
  ADD UNIQUE KEY `cedula_identidad_3` (`cedula_identidad`),
  ADD KEY `cedula_identidad_2` (`cedula_identidad`),
  ADD KEY `id_cargo` (`id_cargo`),
  ADD KEY `id_programa` (`id_programa`);

--
-- Indexes for table `programa`
--
ALTER TABLE `programa`
  ADD PRIMARY KEY (`id_programa`);

--
-- Indexes for table `representante`
--
ALTER TABLE `representante`
  ADD PRIMARY KEY (`ci_representante`);

--
-- Indexes for table `representante_alumno`
--
ALTER TABLE `representante_alumno`
  ADD PRIMARY KEY (`ci_representante`,`cod_alumno`),
  ADD KEY `ci_representante` (`ci_representante`,`cod_alumno`),
  ADD KEY `cod_alumno` (`cod_alumno`);

--
-- Indexes for table `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`privilegio`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`nombre_usuario`),
  ADD KEY `cedula_identidad` (`cedula_identidad`),
  ADD KEY `cedula_identidad_2` (`cedula_identidad`),
  ADD KEY `privilegio` (`privilegio`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cargo`
--
ALTER TABLE `cargo`
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `programa`
--
ALTER TABLE `programa`
  MODIFY `id_programa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alumno`
--
ALTER TABLE `alumno`
  ADD CONSTRAINT `alumno_ibfk_3` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id_programa`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `alumno_asistencia`
--
ALTER TABLE `alumno_asistencia`
  ADD CONSTRAINT `alumno_asistencia_ibfk_2` FOREIGN KEY (`cod_alumno`) REFERENCES `alumno` (`cod_alumno`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `alumno_asistencia_ibfk_3` FOREIGN KEY (`id_asistencia`) REFERENCES `asistencia` (`id_asistencia`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `asistencia`
--
ALTER TABLE `asistencia`
  ADD CONSTRAINT `asistencia_ibfk_2` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id_programa`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencia_ibfk_3` FOREIGN KEY (`cedula_identidad`) REFERENCES `profesor` (`cedula_identidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencia_ibfk_4` FOREIGN KEY (`id_clase`) REFERENCES `clase` (`id_clase`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `clase`
--
ALTER TABLE `clase`
  ADD CONSTRAINT `clase_ibfk_1` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id_programa`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clase_ibfk_2` FOREIGN KEY (`cedula_identidad`) REFERENCES `profesor` (`cedula_identidad`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `clase_alumno`
--
ALTER TABLE `clase_alumno`
  ADD CONSTRAINT `clase_alumno_ibfk_3` FOREIGN KEY (`cod_alumno`) REFERENCES `alumno` (`cod_alumno`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clase_alumno_ibfk_4` FOREIGN KEY (`id_clase`) REFERENCES `clase` (`id_clase`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `evaluacion`
--
ALTER TABLE `evaluacion`
  ADD CONSTRAINT `evaluacion_ibfk_1` FOREIGN KEY (`cedula_identidad`) REFERENCES `profesor` (`cedula_identidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evaluacion_ibfk_2` FOREIGN KEY (`id_clase`) REFERENCES `clase` (`id_clase`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `evaluacion_alumno`
--
ALTER TABLE `evaluacion_alumno`
  ADD CONSTRAINT `evaluacion_alumno_ibfk_2` FOREIGN KEY (`cod_alumno`) REFERENCES `alumno` (`cod_alumno`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evaluacion_alumno_ibfk_3` FOREIGN KEY (`id_evaluacion`) REFERENCES `evaluacion` (`id_evaluacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `instrumento_alumno`
--
ALTER TABLE `instrumento_alumno`
  ADD CONSTRAINT `instrumento_alumno_ibfk_2` FOREIGN KEY (`num_serial`) REFERENCES `instrumento` (`num_serial`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `instrumento_alumno_ibfk_3` FOREIGN KEY (`cod_alumno`) REFERENCES `alumno` (`cod_alumno`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `profesor`
--
ALTER TABLE `profesor`
  ADD CONSTRAINT `profesor_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `profesor_ibfk_2` FOREIGN KEY (`id_programa`) REFERENCES `programa` (`id_programa`);

--
-- Constraints for table `representante_alumno`
--
ALTER TABLE `representante_alumno`
  ADD CONSTRAINT `representante_alumno_ibfk_2` FOREIGN KEY (`ci_representante`) REFERENCES `representante` (`ci_representante`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `representante_alumno_ibfk_3` FOREIGN KEY (`cod_alumno`) REFERENCES `alumno` (`cod_alumno`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`cedula_identidad`) REFERENCES `profesor` (`cedula_identidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`privilegio`) REFERENCES `tipo_usuario` (`privilegio`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
