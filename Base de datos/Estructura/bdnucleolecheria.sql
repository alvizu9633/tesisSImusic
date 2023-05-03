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

-- --------------------------------------------------------

--
-- Table structure for table `alumno_asistencia`
--

CREATE TABLE `alumno_asistencia` (
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ausente_presente` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `id_asistencia` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `cargo`
--

CREATE TABLE `cargo` (
  `id_cargo` int(11) NOT NULL,
  `nombre_cargo` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `clase_alumno`
--

CREATE TABLE `clase_alumno` (
  `id_clase` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `evaluacion_alumno`
--

CREATE TABLE `evaluacion_alumno` (
  `id_evaluacion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `nota` float NOT NULL,
  `cod_alumno` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `instrumento_alumno`
--

CREATE TABLE `instrumento_alumno` (
  `num_serial` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `en_posesion` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `programa`
--

CREATE TABLE `programa` (
  `id_programa` int(11) NOT NULL,
  `nombre_programa` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `representante_alumno`
--

CREATE TABLE `representante_alumno` (
  `ci_representante` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cod_alumno` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `privilegio` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `funcion` varchar(15) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

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
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `programa`
--
ALTER TABLE `programa`
  MODIFY `id_programa` int(11) NOT NULL AUTO_INCREMENT;

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
