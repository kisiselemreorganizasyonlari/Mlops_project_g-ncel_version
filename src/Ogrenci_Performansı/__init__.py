import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s "

log_dir='logs'
log_filepath=os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format=logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('Ogrenci_Performansı')



def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Pythondaki Hata Scripti {file_name} dosyasından {line_number} satırından {str(error)} hatası gelmiştir."
    return error_message


