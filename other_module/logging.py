import logging
print("start log")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.FileHandler("app.log", 'a', 'utf-8')])
                    
logging.getLogger().addHandler(logging.StreamHandler())
