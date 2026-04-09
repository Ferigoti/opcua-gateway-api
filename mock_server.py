import asyncio
import random
from asyncua import Server

async def main():
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("Servidor Mock")

    uri = "http://mock.io"
    idx = await server.register_namespace(uri)
    objects = server.nodes.objects

    # Criando RTG_01
    rtg_01 = await objects.add_object(idx, "RTG_01")
    t1_balanca = await rtg_01.add_variable(idx, "Balanca", 0.0)
    t1_sensor = await rtg_01.add_variable(idx, "Acoplamento", False)
    await t1_balanca.set_writable()
    await t1_sensor.set_writable()

    # Criando RTG_02
    rtg_02 = await objects.add_object(idx, "RTG_02")
    t2_balanca = await rtg_02.add_variable(idx, "Balanca", 0.0)
    t2_sensor = await rtg_02.add_variable(idx, "Acoplamento", False)
    await t2_balanca.set_writable()
    await t2_sensor.set_writable()

    print(f"Mock rodando. NodeIDs RTG_01 -> Balanca: {t1_balanca.nodeid}, Sensor: {t1_sensor.nodeid}")
    print(f"Mock rodando. NodeIDs RTG_02 -> Balanca: {t2_balanca.nodeid}, Sensor: {t2_sensor.nodeid}")

    async with server:
        while True:
            # Atualiza RTG 01
            await t1_balanca.write_value(round(random.uniform(10.0, 40.0), 2))
            await t1_sensor.write_value(random.choice([True, False]))
            
            # Atualiza RTG 02
            await t2_balanca.write_value(round(random.uniform(20.0, 50.0), 2))
            await t2_sensor.write_value(random.choice([True, False]))
            
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())