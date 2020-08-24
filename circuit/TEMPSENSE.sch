EESchema Schematic File Version 4
LIBS:TEMPSENSE-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "TEMPSENSE v0.2"
Date "2020-08-24"
Rev "0.2"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L TEMPSENSE:MAX31855 U1
U 1 1 5F04AC2E
P 4400 2200
F 0 "U1" H 4778 1846 50  0000 L CNN
F 1 "MAX31855" H 4778 1755 50  0000 L CNN
F 2 "TEMPSENSE:Max-31855-board" H 4400 2200 50  0001 C CNN
F 3 "" H 4400 2200 50  0001 C CNN
	1    4400 2200
	1    0    0    -1  
$EndComp
$Comp
L TEMPSENSE:MAX31855 U2
U 1 1 5F04AF18
P 5350 2200
F 0 "U2" H 5728 1846 50  0000 L CNN
F 1 "MAX31855" H 5728 1755 50  0000 L CNN
F 2 "TEMPSENSE:Max-31855-board" H 5350 2200 50  0001 C CNN
F 3 "" H 5350 2200 50  0001 C CNN
	1    5350 2200
	1    0    0    -1  
$EndComp
$Comp
L TEMPSENSE:MAX31855 U3
U 1 1 5F04B0BE
P 6300 2200
F 0 "U3" H 6678 1846 50  0000 L CNN
F 1 "MAX31855" H 6678 1755 50  0000 L CNN
F 2 "TEMPSENSE:Max-31855-board" H 6300 2200 50  0001 C CNN
F 3 "" H 6300 2200 50  0001 C CNN
	1    6300 2200
	1    0    0    -1  
$EndComp
$Comp
L TEMPSENSE:MAX31855 U4
U 1 1 5F04B7B2
P 7300 2200
F 0 "U4" H 7678 1846 50  0000 L CNN
F 1 "MAX31855" H 7678 1755 50  0000 L CNN
F 2 "TEMPSENSE:Max-31855-board" H 7300 2200 50  0001 C CNN
F 3 "" H 7300 2200 50  0001 C CNN
	1    7300 2200
	1    0    0    -1  
$EndComp
$Comp
L TEMPSENSE:FT232H U5
U 1 1 5F04E877
P 6000 800
F 0 "U5" H 6000 915 50  0000 C CNN
F 1 "FT232H" H 6000 824 50  0000 C CNN
F 2 "TEMPSENSE:FT232H-socket" H 6000 800 50  0001 C CNN
F 3 "" H 6000 800 50  0001 C CNN
	1    6000 800 
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 1550 4150 1550
Wire Wire Line
	5700 1650 5050 1650
Wire Wire Line
	5700 1750 5250 1750
Wire Wire Line
	5250 1750 5250 2150
Wire Wire Line
	5250 2150 5950 2150
Wire Wire Line
	5950 2150 5950 2750
Wire Wire Line
	5950 2750 6300 2750
Wire Wire Line
	5700 1850 5450 1850
Wire Wire Line
	5450 1850 5450 2050
Wire Wire Line
	5450 2050 6900 2050
Wire Wire Line
	6900 2050 6900 2750
Wire Wire Line
	6900 2750 7300 2750
Wire Wire Line
	5350 2750 5050 2750
Wire Wire Line
	4400 2750 4150 2750
Wire Wire Line
	5050 1650 5050 2750
Wire Wire Line
	4150 1550 4150 2750
$Comp
L power:GND #PWR0101
U 1 1 5F05EFA2
P 6150 3000
F 0 "#PWR0101" H 6150 2750 50  0001 C CNN
F 1 "GND" H 6155 2827 50  0000 C CNN
F 2 "" H 6150 3000 50  0001 C CNN
F 3 "" H 6150 3000 50  0001 C CNN
	1    6150 3000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5F05F59F
P 7200 3000
F 0 "#PWR0102" H 7200 2750 50  0001 C CNN
F 1 "GND" H 7205 2827 50  0000 C CNN
F 2 "" H 7200 3000 50  0001 C CNN
F 3 "" H 7200 3000 50  0001 C CNN
	1    7200 3000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 5F05FBDB
P 5200 3000
F 0 "#PWR0103" H 5200 2750 50  0001 C CNN
F 1 "GND" H 5205 2827 50  0000 C CNN
F 2 "" H 5200 3000 50  0001 C CNN
F 3 "" H 5200 3000 50  0001 C CNN
	1    5200 3000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 5F05FD17
P 4250 3000
F 0 "#PWR0104" H 4250 2750 50  0001 C CNN
F 1 "GND" H 4255 2827 50  0000 C CNN
F 2 "" H 4250 3000 50  0001 C CNN
F 3 "" H 4250 3000 50  0001 C CNN
	1    4250 3000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5F05FF09
P 5150 1200
F 0 "#PWR0105" H 5150 950 50  0001 C CNN
F 1 "GND" H 5155 1027 50  0000 C CNN
F 2 "" H 5150 1200 50  0001 C CNN
F 3 "" H 5150 1200 50  0001 C CNN
	1    5150 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 1050 5150 1050
Wire Wire Line
	5150 1050 5150 1200
Wire Wire Line
	4400 2550 4250 2550
Wire Wire Line
	4250 2550 4250 3000
Wire Wire Line
	5350 2550 5200 2550
Wire Wire Line
	5200 2550 5200 3000
Wire Wire Line
	6300 2550 6150 2550
Wire Wire Line
	6150 2550 6150 3000
Wire Wire Line
	7300 2550 7200 2550
Wire Wire Line
	7200 2550 7200 3000
$Comp
L power:+5V #PWR0106
U 1 1 5F06129F
P 5500 800
F 0 "#PWR0106" H 5500 650 50  0001 C CNN
F 1 "+5V" H 5515 973 50  0000 C CNN
F 2 "" H 5500 800 50  0001 C CNN
F 3 "" H 5500 800 50  0001 C CNN
	1    5500 800 
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0107
U 1 1 5F0616EE
P 4300 2250
F 0 "#PWR0107" H 4300 2100 50  0001 C CNN
F 1 "+5V" H 4315 2423 50  0000 C CNN
F 2 "" H 4300 2250 50  0001 C CNN
F 3 "" H 4300 2250 50  0001 C CNN
	1    4300 2250
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0108
U 1 1 5F061CF1
P 5150 2200
F 0 "#PWR0108" H 5150 2050 50  0001 C CNN
F 1 "+5V" H 5165 2373 50  0000 C CNN
F 2 "" H 5150 2200 50  0001 C CNN
F 3 "" H 5150 2200 50  0001 C CNN
	1    5150 2200
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0109
U 1 1 5F0620FD
P 6150 2250
F 0 "#PWR0109" H 6150 2100 50  0001 C CNN
F 1 "+5V" H 6165 2423 50  0000 C CNN
F 2 "" H 6150 2250 50  0001 C CNN
F 3 "" H 6150 2250 50  0001 C CNN
	1    6150 2250
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0110
U 1 1 5F062399
P 7100 2250
F 0 "#PWR0110" H 7100 2100 50  0001 C CNN
F 1 "+5V" H 7115 2423 50  0000 C CNN
F 2 "" H 7100 2250 50  0001 C CNN
F 3 "" H 7100 2250 50  0001 C CNN
	1    7100 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 950  5500 950 
Wire Wire Line
	5500 950  5500 800 
Wire Wire Line
	4400 2350 4300 2350
Wire Wire Line
	4300 2350 4300 2250
Wire Wire Line
	5350 2350 5150 2350
Wire Wire Line
	5150 2350 5150 2200
Wire Wire Line
	6300 2350 6150 2350
Wire Wire Line
	6150 2350 6150 2250
Wire Wire Line
	7300 2350 7100 2350
Wire Wire Line
	7100 2350 7100 2250
NoConn ~ 7300 2450
NoConn ~ 6300 2450
NoConn ~ 5350 2450
NoConn ~ 4400 2450
Text GLabel 5500 1150 0    50   Input ~ 0
CLK
Text GLabel 4050 2850 0    50   Input ~ 0
CLK
Text GLabel 5000 2850 0    50   Input ~ 0
CLK
Text GLabel 5950 2850 0    50   Input ~ 0
CLK
Text GLabel 6950 2850 0    50   Input ~ 0
CLK
Wire Wire Line
	5700 1150 5500 1150
Wire Wire Line
	4050 2850 4400 2850
Wire Wire Line
	5000 2850 5350 2850
Wire Wire Line
	5950 2850 6300 2850
Wire Wire Line
	6950 2850 7300 2850
Text GLabel 5550 1350 0    50   Input ~ 0
MISO
Wire Wire Line
	5700 1350 5550 1350
Text GLabel 4050 3000 0    50   Input ~ 0
MISO
Text GLabel 5000 3000 0    50   Input ~ 0
MISO
Text GLabel 6000 3000 0    50   Input ~ 0
MISO
Text GLabel 6950 3000 0    50   Input ~ 0
MISO
Wire Wire Line
	4400 2650 4200 2650
Wire Wire Line
	4200 2650 4200 3000
Wire Wire Line
	4200 3000 4050 3000
Wire Wire Line
	5350 2650 5150 2650
Wire Wire Line
	5150 2650 5150 3000
Wire Wire Line
	5150 3000 5000 3000
Wire Wire Line
	6300 2650 6100 2650
Wire Wire Line
	6100 2650 6100 3000
Wire Wire Line
	6100 3000 6000 3000
Wire Wire Line
	7300 2650 7100 2650
Wire Wire Line
	7100 2650 7100 3000
Wire Wire Line
	7100 3000 6950 3000
NoConn ~ 5700 1250
NoConn ~ 5700 1450
NoConn ~ 6300 950 
NoConn ~ 6300 1050
NoConn ~ 6300 1150
NoConn ~ 6300 1250
NoConn ~ 6300 1350
NoConn ~ 6300 1450
NoConn ~ 6300 1550
NoConn ~ 6300 1650
NoConn ~ 6300 1750
NoConn ~ 6300 1850
$EndSCHEMATC
