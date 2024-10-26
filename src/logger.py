import logging
import os  # Operating System İşletim sistemi üzerinden kayıtları alacak kütüphane
from datetime import \
    datetime  # Yapılan işlerin zamanlarını alabilmesi için zaman methodlarını kullanan kütüphane

LOG_FİLE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_FİLE) #os.getcwd() methodu istenilen dosya yolunu getirir logs adında klasör açar LOG_FİLE adında dosya adını klasöre ekler
os.makedirs(logs_path,exist_ok=True)

LOG_FİLE_PATH = os.path.join(logs_path,LOG_FİLE) #DOSYA YOLUNUN TAMAMINI BİR DEĞİŞKENE ATADIM

logging.basicConfig(
    filename=LOG_FİLE_PATH,
    format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

if __name__ == '__main__':
    logging.info('Logging Başlatıldı')