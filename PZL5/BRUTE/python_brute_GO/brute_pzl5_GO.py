import os.path
import time
from threading import Thread
from threading import Event

import hashlib

import tempfile
import subprocess

from datetime import datetime
def log_str(logfile_name, string_to_log):
    with open(logfile_name, 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string+': '+string_to_log+'\n')


def t_job(t_id, T_FOUND_ev, left, right, answers_list, B_A_ev):
    log_str(f'./LOG/main.log', f'{t_id}: {left}, {right}')  
    
    failsafe_file_closing_flag = 0
    BATCH_SIZE = 2000
    t_start = time.time()
    t_end = t_start
    
    prepared_answer = []
    for Ib in range(0, (right - left) // BATCH_SIZE + 1):
        solution = -1
        
        
        prepared_answer = answers_list[(left + Ib*BATCH_SIZE) : min(left + (Ib+1)*BATCH_SIZE, right+1)]

            # Create a subprocess and set up pipes for input and output
        process = subprocess.Popen(["./pzl5_GOscript"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

            # Prepare the data to be sent to the subprocess
        data = "\n".join(prepared_answer)  # Join your prepared answers with newlines

            # Send the data to the subprocess
        process.stdin.write(data)
        process.stdin.close()  # Close the input pipe

            # Read the result from the subprocess
        result = process.stdout.read()
        process.stdout.close()  # Close the output pipe

            # Wait for the subprocess to complete
        process.wait()

        if ( "1" in result):
            solution = answers_list[(left + Ib*BATCH_SIZE) + result.find("1")]
            
        t_end = time.time()
        t_tau = t_end - t_start
        t_start = t_end
        if ((t_tau > 0.0001) and (len(result) > 0)):
            i = min(left + (Ib+1)*BATCH_SIZE, right+1) - 1
            log_str(f'./LOG/main.log', f'[{t_id}] {round(100 * (i-left)/(right-left), 2)} % | {round(len(result) / t_tau,2)} answers/s')
        
        if solution != -1:
            log_str(f'./LOG/{t_id}_main.log', f'!!!!!!!!!!!! SOLUTION IS: {solution}')
            log_str(f'./LOG/main.log', f'[{t_id}] !!!!!!!!!!!! SOLUTION IS: {solution}')
            T_FOUND_ev.set()
        
            # Wait for Brutted Answers database free to use
        log_str('./LOG/main.log', f'[{t_id}] Wait for B.A. became free to use')
        B_A_ev.wait()
        log_str('./LOG/main.log', f'[{t_id}] Hope THE B.A. to use')
        B_A_ev.clear()
        with open('pzl5_bruttedAnswers.txt', 'a') as f:
            f.write('\n'.join(answers_list[(left + Ib*BATCH_SIZE):(min(left + (Ib+1)*BATCH_SIZE, right+1))])+'\n')
        log_str('./LOG/main.log', f'[{t_id}] ....THE B.A. released to be used')
        B_A_ev.set()
        
        prepared_answer.clear()
            
        with open('failsafe_AR_5.txt', 'r') as f:
            failsafe_file_closing_flag = int(next(f))
                
        if failsafe_file_closing_flag:
            log_str(f'./LOG/{t_id}_main.log', f'Finishing by failsafe')
            log_str(f'./LOG/main.log', f'[{t_id}] Finishing by failsafe')
            break
        if T_FOUND_ev.is_set():
            log_str(f'./LOG/{t_id}_main.log', f'Finishing by event - SOLUTION FOUND')
            log_str(f'./LOG/main.log', f'[{t_id}] Finishing by event - SOLUTION FOUND')
            break



    # Create DIR for LOGs if not exist
if not os.path.exists("./LOG/"):
   os.makedirs("./LOG/")
    # Read the keys
log_str(f'./LOG/main.log', 'Reading the list of keys.....')           
keys_list = []
with open('pzl5_KEYS.txt') as f:
    keys_list = [ list(set(l.strip('\n').split(','))) for l in f.readlines()]
log_str(f'./LOG/main.log', '.........keys have been read.')

    # Read the brutted answers
log_str(f'./LOG/main.log', 'Reading the brutted answers.....')           
brutted_answers = set()
if os.path.exists('pzl5_bruttedAnswers.txt'):
    with open('pzl5_bruttedAnswers.txt') as f:
        brutted_answers = {l.strip('\n') for l in f.readlines()}
log_str(f'./LOG/main.log', '.........brutted answers have been read.')

    # Preapare the semaphore for BRUTTED ANSWERS database (file)
B_A_ev = Event()
B_A_ev.set()

    # Prepare the list of answers to be brutted
skipped_counter = 0
log_str(f'./LOG/main.log', 'Preparing the list of answers....')  
answers_list = []
for k1 in keys_list[0]:
    for k2 in keys_list[1]:
        for k3 in keys_list[2]:
            for k4 in keys_list[3]:
                for k5 in keys_list[4]:
                    for k6 in keys_list[5]:
                        for k7 in keys_list[6]:
                            answer = ''+k1+k2+k3+k4+k5+k6+k7
                            if answer in brutted_answers:
                                skipped_counter += 1
                            else:
                                answers_list.append(answer)
log_str(f'./LOG/main.log', '............ answers list prepared')                             

log_str(f'./LOG/main.log', f'{len(answers_list)} answers to be brutted, {skipped_counter} skipped (already been brutted)')                             


log_str(f'./LOG/main.log', f"Total size of the answers list is: {len(answers_list)}") 

t_num = 6
t = [0] * t_num
T_FOUND_ev = Event()
T_FOUND_ev.clear()
with open('failsafe_AR_5.txt', 'w') as f:
    f.write('%d' % 0)
    
solution_space_size = len(answers_list)
left_right = [(i*((solution_space_size-1)//t_num + 1), min((i+1)*((solution_space_size-1)//t_num + 1)-1, (solution_space_size-1))) for i in range(0, t_num)]

for i in range(t_num):
    t[i] = Thread(target = t_job, args=(i,    T_FOUND_ev, left_right[i][0], left_right[i][1],  answers_list, B_A_ev) )
    t[i].start()
    time.sleep(3)
    
for i in range(t_num):
    t[i].join()
       
print('FINISH')








