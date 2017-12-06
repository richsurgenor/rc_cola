from bluepy import btle
import binascii

dev = btle.Peripheral("1c:0f:ea:24:f1:4e")
driveCmd = btle.UUID("0000ffe5-0000-1000-8000-00805f9b34fb")
driveService = dev.getServiceByUUID(driveCmd)

driveUuidConfig = btle.UUID("0000ffe9-0000-1000-8000-00805f9b34fb")
driveConfig = driveService.getCharacteristics(driveUuidConfig)[0]
driveConfig.write(b"\x71\" + b"\x00" + b"\xa0")
