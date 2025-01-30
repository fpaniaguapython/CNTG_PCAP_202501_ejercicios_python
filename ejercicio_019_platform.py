import platform

print(platform.platform()) #Windows-11-10.0.26100-SP0
print(platform.platform(aliased=True)) #Windows-11-10.0.26100-SP0
print(platform.platform(terse=True)) #Windows-11

print(platform.machine()) # AMD64

print(platform.processor()) # AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD

print(platform.system()) # Windows

print(platform.version()) # 10.0.26100

print(platform.python_implementation()) # CPython

print(platform.python_version_tuple()) # ('3', '13', '1') -> (mayor, menor, parche)