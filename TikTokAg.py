import random
def UserAgent():
    device_types = {        
        "Samsung": ["Galaxy S23 Ultra", "Galaxy Z Fold 4", "Galaxy Note 20 Ultra"],
        "Google": ["Pixel 7 Pro", "Pixel 6a", "Pixel 5"],
        "OnePlus": ["10 Pro", "9", "8T"],
        "Xiaomi": ["12 Pro", "Mi 11", "Redmi Note 11 Pro"],
        "Huawei": ["P50 Pro", "Mate 50", "P40 Pro"],
        "Sony": ["Xperia 1 IV", "Xperia 10 IV", "Xperia 5 III"],
        "Oppo": ["Find X5 Pro", "Reno 7 Pro", "A96"],
        "Realme": ["GT 2 Pro", "9 Pro", "X7 Max"],
        "Nokia": ["X20", "G50", "8.3"]
    }
    
    brand = random.choice(list(device_types.keys()))
    device_type = random.choice(device_types[brand])
    
    agent = (
        f"com.zhiliaoapp.musically/2023105030 (Linux; U; Android 12; ar_YE;{device_type}; Build/{brand}{device_type}; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)"
    )
    
    return {
        'type': device_type,
        'brand': brand,
        'User-Agent': agent
    }



        