import nfc
import binascii
import sys
sys.path.append("/home/pi/_py/__sd_mod")
import mod_usb_cam_photograph_2 as mod_photo
#*******************************************
def on_startup(targets):
    #print('on_startup')
    for target in targets:
        # nanaco
        # target.sensf_req = bytearray.fromhex("0004c70000")
        # pasmo
        target.sensf_req = bytearray.fromhex("0000030000")
    return targets

#*******************************************
def on_connect(tag):
    #print('on_connect')
    idm = binascii.hexlify(tag.identifier).upper().decode('utf-8')
    print(idm)
    return True

#*******************************************
#while True:
#print('loop')
with nfc.ContactlessFrontend("usb") as clf:
    rdwr = {
        'targets': ['212F'],
        'on-startup': on_startup,
        'on-connect': on_connect
    }
    clf.connect(rdwr=rdwr)
    mod_photo.Take_a_photo(1)
        #break

