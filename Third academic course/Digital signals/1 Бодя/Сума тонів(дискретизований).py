import pyaudio
import math
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

fd = 88200   
f = 500  
t = 0.001       
v = 100

y = (v*(np.sin(2*np.pi*np.arange(fd*t)*f/fd)+np.cos(2*np.pi*np.arange(fd*t)*f*10/fd))).astype(np.float32)
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=fd, output=True)

# stream.write(y)
# stream.stop_stream()
# stream.close()
# p.terminate()

x = [0]
td = t*fd
i = 1
xd = 0

while i < td:
	xd += 1/fd
	i += 1
	x.append(xd)

print('Build function sin(t), only (d) \n')

plt.ioff()

fig, ax = plt.subplots()

ax.plot(x, y, 'b', linestyle='solid')

lgnd = ax.legend(['sin(t) + cos(t) (d)'], loc='upper center', shadow=False)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()
