#!/usr/bin/python3

import sys
import os
import os.path
import pathlib

current_path = pathlib.Path().resolve()
if len(sys.argv) < 2:
    print('Incorrect input')
    exit()

for input_file in sys.argv[1:]:
    print('Processing file ' + input_file)
    if not input_file.endswith('.dat'):
        print('You need to provide .dat file')
    
    file = open(input_file, 'r', encoding='ascii', errors='ignore')
    lines_in_file = file.readlines()
    
    line_array = []
    
    for line in lines_in_file:
        line_array.append(line.split())  
    
    output_name = '/home/adam/skola/phd/hivap/HIVAP-CODE/Hivap/adam_MyHivap/data_hivap/' + line_array[4][0] + '_' + line_array[4][2] + '_' + line_array[4][4] + '_' + line_array[4][5] + '_' + line_array[4][6] + '.dat'

    temp_xn_name = 'temp_xn.dat'
    temp_pxn_name = 'temp_pxn.dat'
    temp_2pxn_name = 'temp_2pxn.dat'
    temp_elab_name = 'temp_elab.dat'

    temp_xn = open(temp_xn_name, 'w')
    temp_pxn = open(temp_pxn_name, 'w')
    temp_2pxn = open(temp_2pxn_name, 'w')
    temp_elab = open(temp_elab_name, 'w')
    
    output = open(output_name, 'w')
    
    i = 0
    while i < (len(line_array)-2):
        if len(line_array[i]) != 0 and line_array[i][0] == 'Querschnitte' and len(line_array[i+1]) == 0 and len(line_array[i+2]) != 0 and line_array[i+2][0] == 'E*/MeV':
            i += 2
            while len(line_array[i]) != 0:
                temp_xn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            while len(line_array[i]) != 0:
                temp_pxn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            while len(line_array[i]) != 0:
                temp_2pxn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            if len(line_array[i]) != 0 and line_array[i][0] == 'Z-Verteilung':
                i += 1
                continue
        if len(line_array[i]) != 0 and line_array[i][0] == 'E_lab' and line_array[i][1] == 'A*MeV':
            temp_elab.write(' '.join(line_array[i]) + '\n')
            i += 2
            while len(line_array[i]) != 0:
                temp_elab.write(' '.join(line_array[i]) + '\n')
                i += 1
        i += 1
    
    temp_array = [temp_xn, temp_pxn, temp_2pxn, temp_elab]
    temp_array_name = [temp_xn_name, temp_pxn_name, temp_2pxn_name, temp_elab_name]
    for item in temp_array:
        item.close()

    for item in temp_array_name:
        f = open(item, 'r')
        lines = f.readlines()
        f.close()
        f = open(item, 'w')
        f.write(lines[0])
        for line in lines[1:]:
            if line.strip('\n') != lines[0].strip('\n'):
                f.write(line)
        f.close()

    temp_array_name.pop()
    
    temp_elab = open(temp_elab_name, 'r')
    elab_lines = temp_elab.readlines()

    for item in temp_array_name:
        f = open(item, 'r')
        lines = f.readlines()
        if len(elab_lines) == len(lines):
            for i in range(len(elab_lines)):
                output_line = elab_lines[i].split()[0] + ' ' + lines[i]
                output.write(output_line)
        output.write('\n\n')
        f.close()

os.remove(temp_xn_name)
os.remove(temp_pxn_name)
os.remove(temp_2pxn_name)
os.remove(temp_elab_name)