import logging as lg;
lg.basicConfig(level=lg.INFO,format='%(asctime)s | %(levelname)s | %(message)s');
# write_Handler = lg.StreamHandler();
# write_Handler.setLevel(lg.INFO);
# error_Handler = lg.FileHandler('error.log');
# error_Handler.setLevel(lg.ERROR);
# # exception_Handler = lg.FileHandler('exception.log')
# # critical_Handler = lg.FileHandler('critical.log')
# # warning_Handler = lg.FileHandler('warning.log')
# # info_Handler = lg.FileHandler('info.log')
# we_format = lg.Formatter('%(name)s | %(asctime)s | %(levelname)s | %(message)s');
# write_Handler.setFormatter(we_format)
# console_log = lg.getLogger(__name__);
# logObj = lg.getLogger(__name__)
# logObj.addHandler(error_Handler)

# console_log.addHandler(write_Handler);
# error_Handler.setFormatter(we_format)

# logger = logObj;
# view_log = console_log;

# class loggin :
#     def __init__(self,lg) :
        
#         self.write_Handler = lg.StreamHandler();
# 		self.we_format = lg.Formatter('%(name)s | %(asctime)s | %(levelname)s | %(message)s');
#   		self.error_Handler = lg.FileHandler('error.log')
#     def writingInConsole(self):
# 		self.write_Handler.setLevel(lg.INFO);
		
#     def writingInFile(self):
        	
#   		self.error_Handler.setLevel(lg.ERROR);



class loggin:
    def __init__(self) :
        print(lg)
        self.write_Handler = lg.StreamHandler();
        self.write_Handler.setLevel(lg.INFO);
        self.error_Handler = lg.FileHandler('error.log');
        self.error_Handler.setLevel(lg.ERROR);
        self.we_format = lg.Formatter('%(name)s | %(asctime)s | %(levelname)s | %(message)s');
        self.console_log = lg.getLogger(__name__);
        self.logObj = lg.getLogger(__name__);
        self.write_Handler.setFormatter(self.we_format);
        self.error_Handler.setFormatter(self.we_format);
        self.logObj.addHandler(self.error_Handler);
        self.console_log.addHandler(self.write_Handler)
    def writingInfile(self) :
        return self.logObj;
    def writeInConsolo(self) :
        return self.console_log;


# mainObj = loggin();
# logger = mainObj.writingInfile();
# view_log = mainObj.writeInConsolo();

        