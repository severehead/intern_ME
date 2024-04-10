from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time


client = ModbusClient(method='RTU', port='COM3', bytesize=8, stopbits=1, timeout=500, baudrate=9600, slave=1, parity='N')
connection = client.connect()
print(connection)
recoil = client.read_coils(0x0000, 3, unit=1)
print(recoil.bits)
dis=client.read_discrete_inputs(0x0001, 1, unit=1)
print(dis.bits)
hold = client.read_holding_registers(0x0000, 8, unit=1)
print(hold.registers)
inp = client.read_input_registers(0x0000, 8, unit=1)
print(inp.registers)
i=0x0000
k=1
while (i>=0x0000 and i<=0x0007):
    print(i,k)

    if k>=8:
        x = client.write_coil(i, 0, unit=1)
        i = i - 0x0001
    else:
        x = client.write_coil(i, 1, unit=1)
        i = i + 0x0001
    k += 1
    time.sleep(1)

print('Rele 8: on')
client.close()
