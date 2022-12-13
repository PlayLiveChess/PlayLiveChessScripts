import urllib.request
import json
import websockets
import asyncio
import nest_asyncio
import asyncio
nest_asyncio.apply()

URL="http://13.235.79.128:8000/available-gameserver/"



#fetch 
x = urllib.request.urlopen(URL)
ipToHit=json.loads(x.read())['available'] 
print(ipToHit)




async def firstWorker():
    actualUrl=f"ws://{ipToHit}/ws/connect/"
    async with websockets.connect(actualUrl) as ws:
        msg=await ws.recv()
        print(msg)




loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(firstWorker())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
