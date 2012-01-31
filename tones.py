import math
import wave
from array import array

SAMPLE_RATE = 44100.0

def sine(f,t):
    return math.sin(2*math.pi*f*t)

def square(f,t):
    return round(math.sin(2*math.pi*f*t))

def sawtooth(f,t):
    return 2.0*math.fmod((t*f)+0.5,1.0)-1.0

def triangle(f,t):
  q = 4*math.fmod(t*f,1)
  q = (q,2-q)[q > 1]
  return (q,-2-q)[q < -1]

def write_wav(filename, samples):
    wav_file = wave.open(filename, "w")
    wav_file.setparams((1, 2, int(SAMPLE_RATE), len(samples), "NONE", ""))
    wav_file.writeframesraw(array("h", samples))
    wav_file.close()

    print "%s" % filename

def gen_sound(freq=440, length=0.3, func=sine):
    n_samples = SAMPLE_RATE*length
    amp = 16000.0
    samples = []

    for t in range(int(n_samples)):
        samples.append(square(f, t/SAMPLE_RATE))
    fade_length = int(SAMPLE_RATE*0.3)
    for i in range(fade_length):
        samples[-i] = samples[-i]*((i/float(fade_length)))
    samples = [int(s*amp/2) for s in samples]
    return samples

fs = [27.5 * 2.**((k + 44)/12.) for k in range(16)]
length = 0.3

for i, f in enumerate(fs):
    write_wav("data/square_%s.wav" % i, gen_sound(f, length, square))
    write_wav("data/saw_%s.wav" % i, gen_sound(f, length, sawtooth))
    write_wav("data/sine_%s.wav" % i, gen_sound(f, length, sine))
    write_wav("data/tri_%s.wav" % i, gen_sound(f, length, triangle))

