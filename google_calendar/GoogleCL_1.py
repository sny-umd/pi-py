# coding: utf-8
import sys

import http.server
import socketserver
#sys.path.append("/home/pi/_py/__sd_mod")
#import mod_webserver as mod_wb
sys.path.append("/home/pi/_py/__sd_mod/mod_gCalendar")
import mod_gCalendarCtrl as mod_GC



#**********************************************************
def mWebServerRun():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
                
#**********************************************************
def mFileWrite_text(str_filename, str_html_text):
    strNL = '\n'
    str_html_val = '<html>' + strNL + \
                    '<body>' + strNL + \
                    str_html_text + strNL + \
                    '</body>' + strNL + \
                    '</html>'
    str_html_val.encode('shift_jis')
    #print(str_html_val)
    f = open(str_filename, 'w')
    f.write(str_html_val)
    f.close()


#**********************************************************
if __name__ == '__main__':
    room1_val = ''
    room2_val = ''
    room3_val = ''
    iNum = 3
    str_file_name = '/home/pi/_py/google_calendar/index.html'
    
    cl_id = 'skydisc.jp_3130303935323631313837@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room1_val = mod_GC.read_calendar_now(events, False)
    #print(room1_val)
    #mDataTypeChange_Ary(room1_val)
    
    cl_id = 'skydisc.jp_34313237303839303238@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room2_val = mod_GC.read_calendar_now(events, False)
    #print(room2_val)
    
    cl_id = 'skydisc.jp_3638353434303437393537@resource.calendar.google.com'
    events = mod_GC.set_Calendar_API(cl_id, iNum)
    room3_val = mod_GC.read_calendar_now(events, False)
    #print(room3_val)
    
    str_html_txt = room1_val + '\n**********\n' + room2_val + '\n**********\n' + room3_val
    mFileWrite_text(str_file_name, str_html_txt)
    
    mWebServerRun()