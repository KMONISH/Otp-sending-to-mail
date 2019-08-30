import math
import random
import genarate
def generateOTP() : 
	string = '0123456789ABCDE'
	OTP = ""
	length = len(string) 
	for i in range(6) : 
		OTP += string[math.floor(random.random() * length)] 
		return OTP
	if __name__ == "__main__" : 
		CONFIRM = generateOTP()
		genarate.subject = 'HI USER{}:'.format(CONFIRM)
		genarate.msg = 'Reqested O_T_P is:{}'.format(CONFIRM)
		genarate.send_email(genarate.subject, genarate.msg)


	
