# CUDA solver  - the bruteforce tool for ARweave puzzles that relies on NVIDIA GPUs.

Currently assembled targeting mainly the LINUX systems ( i have not verified / tuned it for WINDOWS )

# Instruction

1. First, you'll need to upload the "sources" folder to your (linux) machine (AND, optionally, the python script "brute_AR.py")

2. The CUDA sources requires compilation with with use of Nvidia CUDA Compiler (nvcc) and so you will need to install/configure the nvcc + nvidia drivers on your machine.

3. Having a correctly installed/configured nvcc - proceed for the solver compilation, that could be done simply in a single line shown below, that will compile the sources into an executable called "cu_brute_ar"

nvcc ./sources/main.cu ./sources/manager.cu ./sources/KernelStride.cu ./sources/GPU.cu ./sources/tools.cpp -arch=compute_75 -code=sm_75 -O3 -o cu_brute_ar

4. This executable ("cu_brute_ar" - compiled from sources described at step 3) can perform a single-gpu bruteforce job specified with command line arguments:

./cu_brute_ar --cuda_device_id=<CUDA_ID> --cuda_grid=<CUDA_GRID> --cuda_block=<CUDA_BLOCK> --loops_num=<CUDA_LOOPS> --msg_file=<MSG_FILE_PATH> --solution_tag=<SOLUTION_TAG> --keys_file=<KEYS_FILE_PATH> --keys_num=<KEYS_NUM> --index_begin=<INDEX_BEGIN> --index_interval=<INDEX_INTERVAL> --log_folder=<LOG_FOLDER>

where:

<CUDA_ID>
<CUDA_GRID>
<CUDA_BLOCK>
<CUDA_LOOPS>
<MSG_FILE_PATH>
<SOLUTION_TAG>
<KEYS_FILE_PATH>
<KEYS_NUM>
<INDEX_BEGIN>
<INDEX_INTERVAL>
<LOG_FOLDER>

For example, it can look like following:

./cu_brute_ar --cuda_device_id=0 --cuda_grid=8 --cuda_block=64 --loops_num=2 --msg_file="./5/message.b64" --solution_tag='"kty":"RSA"' --keys_file="./5/keys.txt" --keys_num=7 --index_begin=229376 --index_interval=1024 --log_folder=./5/

5. Optionaly (and i strongly advise to use this approach), you can use the extra MANAGING layer through the PYTHON script "brute_AR.py". To use it, you will need the python be installed on your system as well, obviously. 

Running its pretty simple - just execute the script with single command line argument - the name of a "JOB" folder where the JOB.cfg (current JOB cofniguration), the keys.txt and the message files lay (if needed - you may play around with their locations too actually):

python brute_AR.py <JOB_folder>

for example:

python brute_AR.py ./5/

This pyhton script will read the JOB.cfg, keys and message files and produce the bruteforce plan for the specified desirable "reporting time" (given by single_thread_speed and average_step_duration_sec parameters). The python would work with multi-GPU system as well if they are accessible under the same console / file system. The produced bruteforce plan would be stored in the file "JOB_list.txt" (you may watch this file as well as the log in order to check current state of a bruteforce routine). On each execution of a script - it will check for JOB_list.txt existance and launch the brutefoce only on those portions of a total bruteforce task that has not been SUCCESSFULLY done before. This way you may follow the long bruteforce configurations with restarts or even exporting the done job into other platforms or share it among different solvers. The fields of the JOB.cfg described below:

JOB.cfg:

cuda_ids                  =0
cuda_grid                 =72
cuda_block                =256
msg_file                  =message.b64
solution_tag              ="kty":"RSA"
keys_file                 =keys.txt
keys_num                  =8
single_thread_speed       =1
average_step_duration_sec =60

CUDA ID, CUDA GRID, CUDA BLOCK - are parameters that has been described previously but here, if you have few NVIDIA GPUs in your system and want to use more than a single GPU - you can specify these parameters separated by comma. For example:

cuda_ids                  =0,1
cuda_grid                 =72,32
cuda_block                =256,128
...
single_thread_speed       =1,2

this way the script will run the manage the working plan among two GPUs feeding them with remained yet unbrutted portions of a job from JOB_list.txt with an appropriate GRID and BLOCK parameters.

single_thread_speed is an approximate brute speed of a SINGLE CUDA core for your GPUs (you may get an approximation during run in the log files) and this parameters needed in pair with average_step_duration_sec to set the desirable SIZE OF A BRUTE WORK PORTIONS - or in else words to set how often the GPUs will report back their work status / how much of a solutional space is brutted in a single reportable step.

The core of this program been composed and shared by an active (puzzle solvers) community member that has his own git - check hiw variant of wrapper [1](https://github.com/Solutio-Cursus/arweave-puzzle-cuda-solver). I have built my own wrapper around this crypto core in order to make it more familliar for me and to my own use, but anyone is wellcome to try it out. Some may found it overload and heavy, i udnerstand this - and i am openned for advices and propositions!


### P.S

If you faced the following error:
```
terminate called after throwing an instance of 'std::runtime_error'
  what():  locale::facet::_S_create_c_locale name not valid
Aborted (core dumped)
```
... you may try to resolve it via updating the locale
```
sudo apt update
sudo apt install locales
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
```

### References:

[1] CUDA core coder - https://github.com/Solutio-Cursus/arweave-puzzle-cuda-solver
