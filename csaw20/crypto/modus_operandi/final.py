import socket

class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 256):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(256)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()


def find_repeating_blocks(cip: bytes) -> int:
    """ takes cipher, breaks them into chunks (blocks of text)
        and returns the number of repeated chunks

        text is divided into 16 bytes of data which is standard 
        for ECB

    param1: gets the cipher text
    returns the amount of repeated chunks 

    """

    chunk_tex = chunks(cip,16)
    
    repeat = len(chunk_tex) - len(set(chunk_tex))
    return(repeat)

def chunks(text:bytes,blocksize:int)->bytes:
    """
    pram1: whole encrypted messages 
    pram2: amount of chunks needed 
    return array of chunks of data
    """
    chunk_data = b''
    chunks = []
    for i in range(0,len(text),blocksize):
        chunk_data = text[i:i+blocksize] 
        chunks.append(chunk_data)
    return chunks



if __name__ == '__main__':
    nc = Netcat('crypto.chal.csaw.io', 5001)
    final = b''
    for i in range(200):
        
        print('I=',i)
        if i < 175:
            string = nc.read(256)
            print(string)

            #crafted plaintext which gives same cipher in ECB
            content = 'AAAAAAAAAAAAAAAA'*4 + '\n' 
            nc.write(content.encode())
            string = nc.read(256)
            
            if len(string) == 0:
                print('error')
                break
            string = str(string[16:-14]) 
            
            repeat = find_repeating_blocks(string)
            
            if repeat != 0:
                res = 'ECB'+ '\n'
                final = final + b'0'
            else:
                res = 'CBC'+ '\n'
                final = final + b'1'
            
            if i == 174:
                print(final)
            nc.write(res.encode())
