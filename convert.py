import glob
import os
for f in glob.glob("data/*.wav"):
    basename = f[:-4]
    print basename
    os.system("gst-launch -q filesrc location=%s.wav ! wavparse ! audioconvert ! vorbisenc ! oggmux ! filesink location=%s.ogg" % (basename, basename))
    os.system("gst-launch -q filesrc location=%s.wav ! wavparse ! audioconvert ! lame ! filesink location=%s.mp3" % (basename, basename))

