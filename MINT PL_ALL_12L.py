from pymodbus.client import ModbusSerialClient
import time
client = ModbusSerialClient(method='rtu', port='COM3',baudrate=9600, stopbits=1, bytesize= 8, parity="N")
hold=client.read_holding_registers(1009, 6, slave=1).registers
print(hold)
y=client.read_holding_registers(1004, 1, slave=1).registers
print(y)
open=client.write_register(1004, 2048, slave=1)
time.sleep(1)
hold=client.read_holding_registers(1004, 1, slave=1).registers
print(hold)
