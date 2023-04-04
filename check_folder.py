# 17454 quarter note

import os
import random

sample_start_cv = "1A"
sample_cv_amount = "1.00"
bit_rate = "12"
alias = "89"
play_mode = "1"
loop_mode = "1"
mix_level = "-3.0"
channel_mode = "1"
xfade_group = "A"
xfade_a_cv = "1C"
xfade_a_width = "5.00"
zones_cv = "1B"

# folder path
dir_path = "C://Users//shawn//Desktop//assimFiles"

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path.endswith('.wav'):
            res.append(path)

random.shuffle(res)
count = 0
preset_num = 1
preset_name = ""
while count < len(res):
    i = 1
    preset_filename = "prst" + "{:03d}".format(preset_num) + ".yml"
    preset_name = "pyPre " + "{:03d}".format(preset_num)
    print(preset_filename)
    cur_file = open(dir_path + "//" + preset_filename, "w")
    cur_file.write("Preset " + "{:03d}".format(preset_num) + " :\n")
    cur_file.write("  Name : " + preset_name + "\n")
#    cur_file.write("  XfadeACV : " + xfade_a_cv + "\n")
#    cur_file.write("  XfadeAWidth : " + xfade_a_width + "\n")
    while i <= 8 and count < len(res):
        print(res[count])
        cur_file.write("  Channel " + str(i) + " :\n")
        cur_file.write("    Bits : " + bit_rate + "\n")
        cur_file.write("    Aliasing : " + alias + "\n")
        cur_file.write("    PlayMode : " + play_mode + "\n")
        cur_file.write("    MixLevel : " + mix_level + "\n")
        cur_file.write("    SampleStartMod : " + sample_start_cv + " " + sample_cv_amount + "\n")
        if i != 1:
            cur_file.write("    ChannelMode : " + channel_mode + "\n")
        cur_file.write("    LoopMode : " + loop_mode + "\n")
#        cur_file.write("    XfadeGroup : " + xfade_group + "\n")
        cur_file.write("    ZonesCV : " + zones_cv + "\n")
        j = 1
        while j <= 8 and count < len(res):
            cur_file.write("    Zone " + str(j) + " :\n")  # Zone Line Here
            cur_file.write("      Sample : " + res[count] + "\n")
            if j < 8:
                cur_file.write("      MinVoltage : " + str(float(5 - (j * 1.25))) + "\n")
            j += 1
            count += 1
        i += 1
    preset_num += 1
