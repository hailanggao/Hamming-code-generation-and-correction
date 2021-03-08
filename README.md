# Hamming-code-generation-and-correction
#This project id for:
#1.Get hamming distance between two codewords
#2.determine the correct codeword IFF there are any errors in received data
#3.hamming code generation and correction

#For quick running example:
codeword = '101101'
check_num = 4
hamming_list = [None, None, '1', None,'0','1','1', None, '0', '1']
bin_list = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010']
index_bit = 1,2,4,8
check_list = [1,2,4,8]
