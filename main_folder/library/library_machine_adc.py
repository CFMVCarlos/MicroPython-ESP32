from machine import ADC, Pin

# ADC.ATTN_0DB: No attenuation (100mV - 950mV)
# ADC.ATTN_2_5DB: 2.5dB attenuation (100mV - 1250mV)
# ADC.ATTN_6DB: 6dB attenuation (150mV - 1750mV)
# ADC.ATTN_11DB: 11dB attenuation (150mV - 2450mV)

# ADC.WIDTH_9BIT: 9 bits (0-511)
# ADC.WIDTH_10BIT: 10 bits (0-1023)
# ADC.WIDTH_11BIT: 11 bits (0-2047)
# ADC.WIDTH_12BIT: 12 bits (0-4095)

adc = ADC(Pin(13))  # create an ADC object acting on a pin
adc.atten(ADC.ATTN_11DB)  # set the attenuation
adc.width(ADC.WIDTH_12BIT)  # set the resolution
val = adc.read_u16()  # read a raw analog value in the range 0-65535
print(f"Raw ADC: {val}")
val = adc.read_uv()  # read an analog value in microvolts
print(f"Voltage: {val*1e-6}")
