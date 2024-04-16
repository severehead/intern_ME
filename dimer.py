from pymodbus.client import ModbusSerialClient
client = ModbusSerialClient(method='rtu', port='COM3',baudrate=9600, stopbits=1, bytesize= 8 )
print(client.connect())
dis=client.read_discrete_inputs(0x0000, 1, slave=1)
print(dis.registers)
hold=client.read_holding_registers(0x0000, 7, slave=1)
print(hold.registers)
led1=client.write_register(0x0001, 0x20ff, slave=1)
led=client.write_register(0x0004, 0xFFFF, slave=1)
