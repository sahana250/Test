import sys
import ctypes
import time
import os
from ctypes import *
libc = ctypes.CDLL("/usr/lib/libOBD2.so")
i=0
while i < 5:

	rc = (libc.init(0))
	print("INIT FUNCTION")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	
	rc = (libc.i_battery_init())
	print("Battery Init")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	
	bat_volt = c_double()
	rc = (libc.i_battery_get_voltage(byref(bat_volt)))
	print(bat_volt.value)
	print("Battery Voltage")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	cpin = create_string_buffer(4)
	cpin.value=b'0000'
	cpin.value
	print(sizeof(cpin))
	rc = libc.gsm_modem_on(ctypes.byref(cpin), 4)
	print("GSM MODEM ON")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	cpuid = create_string_buffer(25)
	rc = (libc.get_cpu_id(ctypes.byref(cpuid),ctypes.sizeof(cpuid)))
	print("CPUID :",cpuid.value)
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.eth_init( )
	print("ETHERNET RC")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.ble_init()
	print("Bluetooth Init")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	rc = os.system('hciconfig')

	#mac = create_string_buffer(4)
	#mac.value=b'hci0'
	#mac.value
	#mac1 = c_char()
	#rc=libc.get_mac_address(ctypes.byref(mac),byref(mac1))
	#print("Bluetooth MAC ADDRESS")
	#print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.wifi_init(1)
	print("WIFI Init")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	rc = os.system('ifconfig')

	#wifi = create_string_buffer(10)
	#wifi.value=b'wlan0'
	#wifi.value
	#wifi1 = c_char()
	#rc=libc.get_mac_address(ctypes.byref(wifi),byref(wifi1))
	#print("WIFI MAC ADDRESS")
	#print(hex((rc + (1 << 32)) % (1 << 32)))

	iccid = create_string_buffer(25)
	rc = (libc.get_gsm_sim_iccid(ctypes.byref(iccid),ctypes.sizeof(iccid)))
	print("SIM ICCID")
	print(iccid.value)
	print(hex((rc + (1 << 32)) % (1 << 32)))

	signal_strength = create_string_buffer(10)
	rc = (libc.get_gsm_signal_strength(ctypes.byref(signal_strength),ctypes.sizeof(signal_strength)))
	print("SIGNAL STRENGTH")
	print(signal_strength.value)
	print(hex((rc + (1 << 32)) % (1 << 32)))

	cell_id = create_string_buffer(10)      
	lac = create_string_buffer(10)                                         
	rc = (libc.get_gsm_nw_reg(ctypes.byref(cell_id), ctypes.sizeof(cell_id), ctypes.byref(lac), ctypes.sizeof(lac)))
	print("GSM NETWORK REGISTRATION STATUS")                               
	print(cell_id.value)                    
	print(lac.value)                                                                                                               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	type = 1
	rc = (libc.set_gsm_network_mode(type))
	print("GSM NETWORK MODE")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	#apn = create_string_buffer(10)
	#apn.value=b'idea.com'
	#apd = create_string_buffer(10)
	#apd.value=b'****200##'
	#user = create_string_buffer(10)
	#user.value=b'user'
	#passd = create_string_buffer(10)
	#passd.value=b'123456'
	#rc=libc.gsm_apn_configuration(ctypes.byref(apn),ctypes.byref(apd),ctypes.byref(user),ctypes.byref(passd))
	#print("GSM APN CONFIGURATION")
	#print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = (libc.check_gsm_modem_status())                            
	print("MODEM STATUS")                                           
	print(hex((rc + (1 << 32)) % (1 << 32)))                                                         

	rc = (libc.establish_connection())
	print("ESTABLISH CONNECTION")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = (libc.check_network_connection())
	print("CHECK NETWORK CONNECTION")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	rc = os.system('ping 8.8.8.8 -c 10')

	rc = libc.ntp_server_update()
	print("NTP server update")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = libc.led_enable()            
	print("LED ENABLE")               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = libc.agps_init()            
	print("AGPS INIT")               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = libc.gps_init()            
	print("GPS INIT")               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	nmea1 = ctypes.c_char_p(b'GPRMC')
	nmea = ctypes.c_char_p(b'GPGGA')
	nmea2 = ctypes.c_char_p(b'GPGSA')
	nmea3 = ctypes.c_char_p(b'GPVTG')
	recv_data = ctypes.create_string_buffer(128)
	clen = ctypes.c_size_t()
	clen.value = 0
	i=0
	while i <= 10:
	    rc = libc.get_gps_data(nmea.value, ctypes.byref(clen), ctypes.byref(recv_data), ctypes.sizeof(recv_data))
	    rc = libc.get_gps_data(nmea1.value, ctypes.byref(clen), ctypes.byref(recv_data), ctypes.sizeof(recv_data))
	    rc = libc.get_gps_data(nmea2.value, ctypes.byref(clen), ctypes.byref(recv_data), ctypes.sizeof(recv_data))
	    rc = libc.get_gps_data(nmea3.value, ctypes.byref(clen), ctypes.byref(recv_data), ctypes.sizeof(recv_data))
	    i=i+1
	print("GPS GET DATA")               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = libc.set_gsm_flight_mode_on()                                                                            
	print("FLIGH MODE ON")                           
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = libc.set_gsm_flight_mode_off()                                                                            
	print("FLIGH MODE OFF")                                                                                        
	print(hex((rc + (1 << 32)) % (1 << 32)))

	bat_volt = c_double()
	rc = (libc.i_battery_get_voltage(byref(bat_volt)))
	print(bat_volt.value)
	print("Battery Voltage")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = (libc.i_battery_get_health())      
	print("Battery health")                  
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = (libc.get_power_source())      
	print("Power source")                  
	print(hex((rc + (1 << 32)) % (1 << 32)))

	OFF = 0                                                         
	ON = 1                                                                                                          
	rc = (libc.battery_charge_state_config(OFF))
	print("Battery Charge")                                                                                  
	print(hex((rc + (1 << 32)) % (1 << 32)))

	#rc = os.system('./sensor_test')                                         
	#print("Accelerometer")                                                                                           
	#print(hex((rc + (1 << 32)) % (1 << 32)))

	can = create_string_buffer(5)
	can.value=b'can0'
	libc.can_init(ctypes.byref(can),500000)
	print("CAN INIT")                                
	print(hex((rc + (1 << 32)) % (1 << 32))) 
	rc = os.system('ifconfig')

	rc=libc.acc_init()                                    
	print("ACCELEROMETER INIT")                                                                               
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.gyro_init()                                                                                        
	print("GYRO INIT")                                                                                         
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc = (libc.set_acc_wakeup_threshold(0x89))                                                                              
	print("Accelerometer threshold")                                                                                             
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.set_acc_sampling_frequency(0x70)
	rc=libc.set_acc_low_pass_filter(0x80)
	rc=libc.set_acc_wakeup_threshold(0x81)
	rc=libc.set_gyro_sampling_frequency(0x70)
	print("Accelerometer values")          
	print(hex((rc + (1 << 32)) % (1 << 32)))


	print("######################DEINIT ALL INTERFACES#################")

	#rc=libc.mag_deinit()
	#print("MAGNETOMETER DEINIT")
	#print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.gyro_deinit()
	print("GYRO DEINIT")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.acc_deinit()
	print("ACCELEROMETER DEINIT")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.ble_deinit()
	print("BLE_DEINIT")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	os.system('hciconfig')

	rc=libc.wifi_deinit(1)
	print("WIFI DEINIT")
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.can_deinit(b'can0')
	print("CAN DEINIT")
	print(hex((rc + (1 << 32)) % (1 << 32)))
	os.system('ifconfig')

	rc=libc.led_disable()                                                                                         
	print("LED DISABLE")                                                                                           
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.gps_deinit()                                                                                  
	print("GPS DEINIT")                                                     
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.gsm_modem_off()                                                                                         
	print("MODEM OFF")                                                                                          
	print(hex((rc + (1 << 32)) % (1 << 32)))

	c=libc.deinit()                                                                                         
	print("DEINIT")                                                                                          
	print(hex((rc + (1 << 32)) % (1 << 32))) 

	rc=libc.config_timer_wakeup(1,60)                                                                                         
	print("TIMER WAKEUP")                                                                                           
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.config_acc_wakeup(1)                                                                                         
	print("ACC WAKEUP")                                                                                           
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.config_can_wakeup(1)                                                                                 
	print("CAN WAKEUP")                                                                                           
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.config_ignition_wakeup(1)                                                                                  
	print("IGNITION WAKEUP")                                                  
	print(hex((rc + (1 << 32)) % (1 << 32)))

	rc=libc.push_device_to_sleep()                 
	print("DEVICE TO SLEEP")                                                                         
	print(hex((rc + (1 << 32)) % (1 << 32)))

	i=i+1

rc=libc.restart_device()              
print("DEVICE RESTART")                    
print(hex((rc + (1 << 32)) % (1 << 32)))
