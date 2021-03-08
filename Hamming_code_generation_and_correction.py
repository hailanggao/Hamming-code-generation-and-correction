#This project id for:
#1.Get hamming distance between two codewords
#2.determine the correct codeword IFF there are any errors in received data
#3.hamming code generation and correction


def hamming_distance(codeword1, codeword2):
    count = 0
    for i in range(len(codeword1)):
        if(codeword1[i] != codeword2[i]):
            count += 1
    return count

#determine the correct codeword IFF there are any errors in received data
def checking_codewords(codewords, received_data):
    words_dist = float('inf')
    dist = float('inf')
    correct_word= ''

    # Get the codewords hamming distance
    i= 0
    if i < len(codewords):
        for j in range(i+1, len(codewords)):
            count = hamming_distance(codewords[i], codewords[j])
            if words_dist > count:
                words_dist = count
        i += 1

    for word in codewords:
        count=hamming_distance(word, received_data)
        if dist > count:
            dist = count
            correct_word = word

    if words_dist < dist * 2+1:
        return "error detected"
    return correct_word

#words =  ['1010111101', '0101110101', '1110101110', '0010110010', '1111000110', '1100101001']
#data =  '1000011100'
#print(checking_codewords(words, data))


#hamming_list = [None, None, '1', None,'0','1','1', None, '0', '1']
#bin_list = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010']
#index_bit = 1,2,4,8
def parityBits_generator(hamming_list, bin_list,index_bit):
    bin_index = '{:08b}'.format(index_bit) #convert index_bit into binary and fix the length as 8
    index_one = bin_index.find('1') - 8 #got the '1' position in bianry of index_bit(-1 for 0001(1), -2 for 0010(4), -3 for 0100(4))
    parity_bits=[]
    for i in range(len(bin_list)):
        if(i+1 != index_bit) and bin_list[i][index_one] == '1': #skip the index_bit itself and find all parity bit
            parity_bits.append(int(hamming_list[i])) #store all parity bits into bit_parity list
    return parity_bits

def bin_list_generator(length):
    bin_list = []
    for i in range (length):
        bin_list.append('{:08b}'.format(i+1))
    return bin_list

#get Number of check_num
def check_num_generator(codeword):
    check_num = 0
    while (2**check_num < len(codeword) + check_num + 1):
        check_num += 1
    return check_num

#sotre each check_num
def check_list_generator(check_num):
    check_list = []
    for i in range(check_num):
        check_list.append(2**i)
    return check_list

from functools import reduce
def hamming_code_generator(codeword):
    check_list=[]
    pointer = 0
    
    check_num = check_num_generator(codeword)
    #length of hamming code
    hamming_list = [None] * (check_num + len(codeword))
    bin_list=bin_list_generator(len(hamming_list))
    #put codeword into the hamming list with correction position
    #create bin_list to restore binary of 1-length
    for i in range(len(hamming_list)):
        if (i & i+1) != 0: #check whether the current position is the power of 2
            hamming_list[i]=codeword[pointer]
            if(pointer < len(codeword)-1):
                pointer += 1

    #get each check_bit and put them into hamming_list
    for i in range(check_num):
        parity_bits = parityBits_generator(hamming_list, bin_list, 2**i)
        parity = reduce(lambda x,y:x^y, parity_bits) # Xor all parity bit
        hamming_list[2**i - 1] = str(parity)
    #convert the hamming_list into int
    hamming_code = int(''.join(hamming_list))
    return hamming_code

#For checking if there are any errors in the received_data
#and find the position of the error
def hamming_code_error_detection(received_data):
    hamming_list = list(received_data)
    bin_list = bin_list_generator(len(hamming_list))
    check_num = -1
    error_list=[]
    #get the check numbers of received_data and store them into a list 
    while(2**check_num < len(hamming_list)):
        check_num += 1
    check_list = check_list_generator(check_num)

    #Xor each parity_bits and store them into error_list
    #reverse error_list and convert it into decimal(err_position)
    #If erro_position is 0 means parity is even, which means no error found
    #otherwise, return the position of error
    for check in check_list:
        parity_bits = parityBits_generator(hamming_list, bin_list, check)
        parity_bits.insert(0,int(hamming_list[check-1]))
        parity = reduce(lambda x,y:x^y, parity_bits)
        error_list.append(str(parity))
    
    error_list.reverse()
    err_position = int(''.join(error_list),2)
    if(err_position == 0):
        return("No error found.")
    return ("Error position is at " + str(err_position))
