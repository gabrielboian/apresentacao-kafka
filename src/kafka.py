import asyncio
import json
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
loop = asyncio.get_event_loop()


def _read_message(msg):
    return json.loads(msg.value.decode('utf-8'))


async def _switch(message):
    msg = _read_message(message)
    if message.topic == 'apresentacao.1':
        print('tópico 1', message)
        print('topico em json', msg)
    else:
        print('tópico 2', message)
        #print('topico em json', msg)


async def consume():
    consumer = AIOKafkaConsumer(
        loop=loop,
        bootstrap_servers="localhost:9193",
    )
    consumer.subscribe(
        ['apresentacao.1', 'apresentacao.2'])

    try:
        await consumer.start()

    except Exception as e:
        print(e)
        return

    try:
        async for msg in consumer:
            await _switch(msg)
    finally:
        await consumer.stop()


async def producer():
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers="localhost:9193")

    try:
        await producer.start()
    except:
        return

    finally:
        await producer.stop()
