#/usr/bin/python

import sys
import argparse
import nacl.secret
import nacl.utils

def main():
	key, input_file, output_file, flag = get_args()	
	enc_dec(key,input_file,output_file,flag)

def get_args():
# Getting arguments from the command line. 

	parser = argparse.ArgumentParser(description = 'This is a command line program for file encryption/decryption')
	
	parser.add_argument('-f', '--flag', type=str, help='enc/dec', required = True)
	parser.add_argument('-i', '--inp_file', type=str, required = True)
	parser.add_argument('-o', '--out_file', type=str, required = True)
	parser.add_argument('-k', '--key', type=str, help='KEY for encryption/decryption', required = True)

	args = parser.parse_args()
	
	key = args.key
	input_file = args.inp_file
	output_file = args.out_file
	flag = args.flag
	
	return key, input_file, output_file, flag

def enc_dec(key,input_file,output_file,flag):
#Main encryption/ decryption function
	
	try:
		box = nacl.secret.SecretBox(key) # using the same keysize as defined by NaCl (32 bytes)
	except ValueError:
		print "key must be equal to exactly 32 bytes long"
		sys.exit(2)
	
	try:	
		inp_stream = open(input_file,"rb").read()
	
		if flag == "enc":
			nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE) # random nonce for file encryption
			out_stream= box.encrypt(inp_stream,nonce)
		elif flag == "dec":
			out_stream = box.decrypt(inp_stream)
		else:
			print "Only enc or dec options are available"		
			sys.exit(2)
	except IOError:
		print "Unable to find the file <",input_file,">. Please check the file name"
		sys.exit(2)
		
	try:
		file=open(output_file, "wb")
	except IOError:
		print " Unable to create output file on disk"
	else:
		file.write(out_stream)
		file.close()
		

if __name__ == '__main__':
	main()


