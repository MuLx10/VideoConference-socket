import pyaudio

class AudioFeed:

    def __init__(self):
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 10240
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        output = True)

    def get_data(self):
        data = self.stream.read(self.chunk)
        return data


    def set_data(self, data):
        self.stream.write(data) 

if __name__=="__main__":
    af = AudioFeed()
    while 1:
        m = af.get_data()
        af.set_data(m)

