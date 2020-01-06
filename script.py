import subprocess
# training
subprocess.call("hypergan train dataset8/ -s 64x64x3 -f png -c sprite_gen_2 --save_every 50 --sampler static_batch --device '/cpu:0' -b 32 --resize", shell=True)


# sampling
# subprocess.call("hypergan train dataset8/ -s 64x64x3 -f png -c sprite_gen_2 --sample_every 1 --sampler batch --save_samples --device '/cpu:0' -b 32 --resize", shell=True)
