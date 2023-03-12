-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2023 at 07:57 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `uid` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `utype` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `access`
--

INSERT INTO `access` (`uid`, `username`, `password`, `utype`) VALUES
('110', 'Devansh Marwaha', '123', 'Admin'),
('111', 'Jatin Sharma', '12345', 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `tstamp` varchar(200) NOT NULL,
  `cname` varchar(200) NOT NULL,
  `cphone` varchar(200) NOT NULL,
  `mname` varchar(200) NOT NULL,
  `mqnt` int(10) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`tstamp`, `cname`, `cphone`, `mname`, `mqnt`, `date`) VALUES
('1676096060', 'Devansh', '8968096689', 'Cetrizine345', 2, '2023-02-11'),
('1676100868', 'Arun', '9814811839', 'Cetrizine345', 2, '2023-02-11'),
('1676101936', 'Ravi', '7890898878', 'Vicks', 10, '2023-02-11'),
('1676115029', 'Rakhi ', '8956743378', 'Paracetamol', 3, '2023-02-11'),
('1676528178', 'Rahul', '7890767789', 'Crocin', 3, '2023-02-16');

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `empid` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `jdate` date NOT NULL,
  `works` varchar(100) NOT NULL,
  `nsalary` date NOT NULL,
  `salary` int(100) NOT NULL,
  `pno` varchar(100) NOT NULL,
  `aano` varchar(100) NOT NULL,
  `pname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`empid`, `name`, `jdate`, `works`, `nsalary`, `salary`, `pno`, `aano`, `pname`) VALUES
(110, 'Devansh Marwaha', '2023-01-01', 'Day', '2023-03-01', 500000, '8968096687', '456734568765', '1676527797InShot_20220802_141709886-min.jpg'),
(111, 'Jatin Sharma', '2023-02-01', 'Night', '2023-03-01', 40000, '7867856678', '567887779089', 'profile_pic.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `medi`
--

CREATE TABLE `medi` (
  `refno` int(10) NOT NULL,
  `medname` varchar(255) NOT NULL,
  `company` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `idate` date NOT NULL,
  `price` varchar(255) NOT NULL,
  `stock` varchar(255) NOT NULL,
  `dose` varchar(255) NOT NULL,
  `pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medi`
--

INSERT INTO `medi` (`refno`, `medname`, `company`, `type`, `idate`, `price`, `stock`, `dose`, `pic`) VALUES
(101, 'Cetrizine345', 'Cipla', 'Normal', '2022-08-08', '245\n\n\n\n', '50', '2 times in a day', '1675947229Cetirizine-Tablets.jpg'),
(102, 'Paracetamol', 'GenPlus', 'Normal', '2022-03-08', '235', '27', '3 times in a day', 'nopic.jpeg'),
(103, 'Crocin', 'GenTak', 'Drug', '2019-02-06', '225', '31', '2 times in a day', 'nopic.jpeg'),
(104, 'Telmisartan', 'BPgen', 'Normal', '2022-02-01', '60', '64', '2 times in a day', 'nopic.jpeg'),
(105, 'Vicks', 'Vicks', 'Normal', '2026-02-13', '300', '50', '2 times in a day', '1676101266vicks-india-veer.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`tstamp`);

--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`empid`);

--
-- Indexes for table `medi`
--
ALTER TABLE `medi`
  ADD PRIMARY KEY (`refno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
