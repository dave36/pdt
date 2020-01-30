import sys
import random
sys.path.append('../')
from protocols.ether import EtherRaw
from protocols.s01fd import *
from protocols.cotp import *
from protocols.s7 import *

szl_0000 = "\x32\x07\x00\x00\x06\x00\x00\x0c\x01\x82\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\x00\x00\xff\x09\x01\x7e\x00\x00\x00\x00\x00\x02" \
"\x00\xbb\x00\x00\x01\x00\x02\x00\x03\x00\x0f\x00\x00\x11\x01\x11" \
"\x0f\x11\x00\x12\x01\x12\x0f\x12\x00\x13\x01\x13\x0f\x13\x00\x14" \
"\x01\x14\x0f\x14\x00\x15\x01\x15\x0f\x15\x00\x16\x01\x16\x0f\x16" \
"\x00\x17\x01\x17\x0f\x17\x00\x19\x01\x19\x0f\x19\x00\x1a\x0f\x1a" \
"\x00\x1b\x0f\x1b\x00\x1c\x01\x1c\x02\x1c\x03\x1c\x0f\x1c\x00\x21" \
"\x01\x21\x02\x21\x09\x21\x0a\x21\x0f\x21\x00\x22\x01\x22\x08\x22" \
"\x09\x22\x0f\x22\x02\x22\x00\x23\x01\x23\x02\x23\x0f\x23\x00\x24" \
"\x01\x24\x02\x24\x0f\x24\x04\x24\x05\x24\x00\x25\x01\x25\x02\x25" \
"\x0f\x25\x01\x31\x0f\x31\x01\x32\x02\x32\x0f\x32\x00\x33\x0f\x33" \
"\x00\x36\x01\x36\x0f\x36\x00\x37\x0f\x37\x00\x38\x01\x38\x02\x38" \
"\x0f\x38\x01\x39\x0f\x39\x00\x3a\x01\x3a\x0f\x3a\x00\x3c\x01\x3c" \
"\x0f\x3c\x00\x71\x0f\x71\x00\x74\x01\x74\x0f\x74\x00\x75\x0c\x75" \
"\x0f\x75\x00\x81\x01\x81\x02\x81\x03\x81\x05\x81\x06\x81\x07\x81" \
"\x08\x81\x09\x81\x0a\x81\x0b\x81\x0c\x81\x0f\x81\x00\x82\x01\x82" \
"\x02\x82\x03\x82\x05\x82\x06\x82\x07\x82\x08\x82\x09\x82\x0a\x82" \
"\x0b\x82\x0c\x82\x0f\x82\x00\x90\x01\x90\x0f\x90\x05\x91\x0a\x91" \
"\x0c\x91\x0d\x91\x00\x92\x02\x92\x03\x92\x04\x92\x05\x92\x06\x92" \
"\x0f\x92\x00\x94\x02\x94\x06\x94\x07\x94\x0f\x94\x00\x95\x01\x95" \
"\x0f\x95\x06\x96\x0c\x96\x0c\x97\x0d\x97\x01\x9a\x02\x9a\x0f\x9a" \
"\x0c\x9b\x00\x9c\x01\x9c\x02\x9c\x03\x9c\x0f\x9c\x00\xa0\x01\xa0" \
"\x04\xa0\x05\xa0\x06\xa0\x07\xa0\x08\xa0\x09\xa0\x0a\xa0\x0b\xa0" \
"\x0c\xa0\x0d\xa0\x0e\xa0\x0f\xa0\x00\xb1\x00\xb2\x00\xb3\x00\xb4" \
"\x01\xb5\x02\xb5\x03\xb5\x04\xb5\x05\xb5\x06\xb5\x07\xb5\x08\xb5" \
"\x01\xb6\x02\xb6\x03\xb6\x04\xb6"

szl_0011 = "\x32\x07\x00\x00\x35\x00\x00\x0c\x00\x7c\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\x00\x00\xff\x09\x00\x78\x00\x11\x00\x00\x00\x1c" \
"\x00\x04\x00\x01\x36\x45\x53\x37\x20\x34\x31\x32\x2d\x35\x48\x4b" \
"\x30\x36\x2d\x30\x41\x42\x30\x20\x00\x82\x00\x42\x00\x00\x00\x06" \
"\x36\x45\x53\x37\x20\x34\x31\x32\x2d\x35\x48\x4b\x30\x36\x2d\x30" \
"\x41\x42\x30\x20\x00\x82\x00\x01\x00\x00\x00\x07\x20\x20\x20\x20" \
"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20" \
"\x00\x00\x56\x06\x00\x04\x00\x81\x42\x6f\x6f\x74\x20\x4c\x6f\x61" \
"\x64\x65\x72\x20\x20\x20\x20\x20\x20\x20\x20\x20\x00\x00\x56\x06" \
"\x00\x00"

szl_001C = "\x32\x07\x00\x00\x34\x00\x00\x0c\x01\x82\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\x00\x00\xff\x09\x01\x7e\x00\x1c\x00\x00\x00\x22" \
"\x00\x0b\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x4f\x72\x69\x67\x69\x6e" \
"\x61\x6c\x20\x53\x69\x65\x6d\x65\x6e\x73\x20\x45\x71\x75\x69\x70" \
"\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x00\x00\x05\x53\x56\x50\x46" \
"\x31\x33\x31\x33\x38\x34\x37\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x43\x50" \
"\x55\x20\x34\x31\x32\x2d\x35\x48\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08" \
"\x4d\x43\x20\x53\x56\x50\x46\x35\x30\x30\x33\x30\x37\x36\x20\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x09\x00\x2a\xf6\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x0c\x31\x41\x41\x30\x36\x2d\x30\x58\x41\x30" \
"\x20\x20\x30\x33\x20\x42\x49\x46\x30\x31\x37\x39\x4f\x31\x31\x30" \
"\x31\x32\x34\x39\x20\x20\x00\x0d\x31\x41\x41\x30\x36\x2d\x30\x58" \
"\x41\x30\x20\x20\x30\x33\x20\x42\x49\x46\x30\x31\x37\x39\x4f\x38" \
"\x31\x30\x33\x30\x34\x34\x20\x20"

szl_0037 = "\x32\x07\x00\x00\x35\x00\x00\x0c\x00\x3c\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\x00\x00\xff\x09\x00\x38\x00\x37\x00\x00\x00\x30" \
"\x00\x01\xff\xff\xc0\xa8\x00\x28\xff\xff\xff\x00\xc0\xa8\x00\x28" \
"\x00\x1b\x1b\xbc\xfb\xc4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x8f\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\x00\x00"

szl_0232 = "\x32\x07\x00\x00\x32\x00\x00\x0c\x00\x34\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\x00\x00\xff\x09\x00\x30\x02\x32\x00\x04\x00\x28" \
"\x00\x01\xf8\x04\x00\x01\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00" \
"\x56\x56\x00\x00\x00\x00\x20\x00\xb3\x5f\x02\x56\x00\x00\x00\x00" \
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
szl_error = "\x32\x07\x00\x00\x07\x00\x00\x0c\x00\x04\x00\x01\x12\x08\x12\x84" \
"\x01\x01\x00\x00\xd4\x02\x0a\x00\x00\x00"

class PLCServer():
    def __init__(self, is_llc=False, ether=None):
        self._is_llc_ = is_llc
        if not is_llc:
            self._ether_ = None
            self._socket_ = socket.socket()
            self._socket_.bind(("", 102))
        else:
            self._socket_ = None
            self._ether_ = ether
    def recv_enum(self):
        def recv_enum_filter(x):
            if x.haslayer(SNAP):
                if x[S01FD].type == 0x0500:
                    return True
            return False
        answer = self._ether_.recv(recv_enum_filter)
        answer = filter(recv_enum_filter, answer)
        if len(answer) != 1:
            raise Exception()
        packet = answer[0]
        return packet.src
    def reply_enum(self, dst):
        self._ether_.send(dst, LLC() / SNAP() / S01FD(type=0x0501) / 
        "\x0c\x01\x53\x37\x2d\x33\x30\x30\x20\x43\x50\x00\x1e\x02\x4d\xfc" \
        "\x68\x6c\x65\x28\x32\x29\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x03\x07\x00"
)
    def recv_cr(self):
        if self._is_llc_:
            def recv_cr_filter(x):
                if x.haslayer(COTP_LLC_ConnectRequest):
                    return True
            answer = self._ether_.recv(recv_cr_filter)
            answer = filter(recv_cr_filter, answer)
            if len(answer) != 1:
                raise Exception()
            packet = answer[0]
            self._dst_mac_ = packet.src
            self._dst_ref_ = packet[COTP_LLC_ConnectRequest].src_ref
        else:
            packet = TPKT(self._tcp_conn_.recv(4096))
            self._dst_ref_ = packet[COTP_TCP_ConnectRequest].src_ref
    def send_cc(self, src_ref):
        if self._is_llc_:
            self._ether_.send(self._dst_mac_,
                LLC(dsap=0xfe, ssap=0xfe, ctrl=3) / 
                CLNP(subnet=0) /
                COTP(length=0x0c) /
                COTP_LLC_ConnectConfirm(
                    dst_ref=self._dst_ref_, src_ref=src_ref, class_=0x4, ext_format=1, tpdu_size_value=0x9, options_value=0x02
                )
            )
        else:
            self._tcp_conn_.send(raw(TPKT(length = 22) / COTP(length=0x0c) / 
                COTP_TCP_ConnectConfirm(
                    dst_ref=self._dst_ref_, src_ref=src_ref, class_=0x4, ext_format=1, tpdu_size_value=0x9
                )
            ))

    def recv_s7(self):
        def recv_ak_filter(x):
            if x.haslayer(COTP_DataAcknowledgement):
                return True
        def recv_dt_filter(x):
            if x.haslayer(S7COMM_SetupComm):
                return True
        if self._is_llc_:
            #self._ether_.recv(recv_ak_filter)
            answer = self._ether_.recv(recv_dt_filter)
            answer = filter(recv_dt_filter, answer)
            if len(answer) != 1:
                raise Exception()
            packet = answer[0]
            return packet
        else:
            data = self._tcp_conn_.recv(4096)
            if not data:
                return None
            else:
                return TPKT(data)
    def send_s7(self, data):
        packet = TPKT(length = len(data) + 7) / COTP() / COTP_TCP_Data() / raw(data)
        self._tcp_conn_.send(raw(packet))
    def send_s7_cc(self):
        if self._is_llc_:
            self._ether_.send(self._dst_mac_, 
                LLC() / 
                CLNP() /
                COTP(dst_ref = self._dst_ref_) /
                COTP_DataAcknowledgement()
            )
            self._ether_.send(self._dst_mac_, 
                LLC() / 
                CLNP() /
                COTP(dst_ref = self._dst_ref_) /
                COTP_LLC_Data() /
                S7COMM() /
                S7COMM_SetupCommAck()
            )
        else:
            self._tcp_conn_.send(raw(TPKT(length=27) / 
                COTP() / 
                COTP_TCP_Data() / S7COMM(param_length=8) / 
                S7COMM_Ack() / S7COMM_Job() /
                S7COMM_Job_Connect()
            ))
    
    def run(self):
        if self._is_llc_:
            print "Server is starting in LLC mode..."
            self.reply_enum(self.recv_enum())
        else:
            print "Server is starting in TCP/IP mode..."
            self._socket_.listen(10)
        while 1:
            if not self._is_llc_:
                conn, addr = self._socket_.accept()
                self._tcp_conn_ = conn
                self._tcp_addr_ = addr
            self.recv_cr()
            src_ref = self._dst_ref_
            while src_ref == self._dst_ref_:
                src_ref = random.randint(0, 0xffff)
            self.send_cc(src_ref)
            s7_cr = self.recv_s7()
            self.send_s7_cc()
            while 1:
                s7_request = self.recv_s7()
                if s7_request == None:
                    break
                if S7COMM_Data_ReadSZL in s7_request:
                    szl_request = s7_request[S7COMM_Data_ReadSZL]
                    if szl_request.szl_id == 0x0000:
                        szl_answer = szl_0000
                    elif szl_request.szl_id == 0x0011:
                        szl_answer = szl_0011
                    elif szl_request.szl_id == 0x001C:
                        szl_answer = szl_001C
                    elif szl_request.szl_id == 0x0037:
                        szl_answer = szl_0037
                    elif szl_request.szl_id == 0x0232:
                        szl_answer = szl_0232
                    else:
                        szl_answer = szl_error
                self.send_s7(szl_answer)
            

            
def main(iface="VMware Virtual Ethernet Adapter for VMnet1", is_llc=True):
    if is_llc:
        ether = EtherRaw(iface, "00:00:00:00:00:02")
    else:
        ether = None
    server = PLCServer(is_llc, ether=ether)
    server.run()

if __name__ == '__main__':
    is_llc = False
    adapter  = "VMware Virtual Ethernet Adapter for VMnet1"
    if len(sys.argv) > 1 and sys.argv[1] == "--llc":
        is_llc = True
    if len(sys.argv) > 2:
        adapter = sys.argv[2]
    main(adapter, is_llc)
