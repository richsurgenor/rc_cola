from bluepy import btle
import binascii

dev = btle.Peripheral("1c:0f:ea:24:f1:4e")
driveCmd = btle.UUID("0000ffe5-0000-1000-8000-00805f9b34fb")
driveService = dev.getServiceByUUID(driveCmd)

driveUuidConfig = bbtle.UUID("0000ffe9-0000-1000-8000-00805f9b34fb")
driveConfig = driveService.getCharacteristics(driveUuidConfig)[0]
driveConfig.write(bytes("\x71\x00\xa0"))
