@echo off
set /p PORT=Enter the port (e.g., COM3): 

esptool --port %PORT% erase_flash

esptool --chip esp32s3 --port %PORT% write_flash -z 0 ESP32_GENERIC_S3-20240602-v1.23.0.bin

pause