import asyncio
import bleak

async def main():
	devices = await bleak.BleakScanner.discover()
	for d in devices:
		print(d)

asyncio.run(main())