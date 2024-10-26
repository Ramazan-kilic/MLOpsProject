import sys  # System Os --> Bilgisayarın sistemi ile alakı işlemlemleri yapan kütüphanedir

from src.logger import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Pythondaki Hata Scripti {file_name} dosyasından {line_number} satırından {str(error)} hatası gelmiştir."
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #error_message özelliğini Exception sınıfından miras aldım
        self.error_message = error_message_detail(error_message, error_detail=error_detail)# kullanmaya aktif ederken yukarda tanımladığım fonksiyonu çağırarak güncelledim
    

    def __str__(self):
        return self.error_message
    

if __name__ == '__main__':
    print("Özel istisna modülü yüklendi.")
    