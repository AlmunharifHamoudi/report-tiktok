from binascii        import hexlify
from random          import randbytes
from uuid            import uuid4
from ttencrypt import ttencrypt
from json            import dumps
from requests        import request
def tt_encrypt(data) -> str:
  return ttencrypt().encrypt(dumps(data).replace(" ", ""))
def device_register() -> dict:
      openudid = hexlify(randbytes(8)).decode()
      cdid = str(uuid4())
      google_aid = str(uuid4())
      clientudid = str(uuid4())
      req_id = str(uuid4())
      url = "https://log-va.tiktokv.com/service/2/device_register/?ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=170404&version_name=17.4.4&device_platform=android&ab_version=17.4.4&ssmix=a&device_type=SM-G611M&device_brand=samsung&language=en&os_api=28&os_version=9&openudid=" + openudid + "&manifest_version_code=2021704040&resolution=720*1280&dpi=320&update_version_code=2021704040&_rticket=1653464286478&_rticket=1653464286894&storage_type=2&app_type=normal&sys_region=US&appTheme=light&pass-route=1&pass-region=1&timezone_name=Europe%252FBerlin&cpu_support64=false&host_abi=armeabi-v7a&app_language=en&ac2=wifi&uoo=1&op_region=US&timezone_offset=3600&build_number=17.4.4&locale=en&region=US&ts=1653464286&cdid=" + cdid
      
      payload = {"magic_tag":"ss_app_log","header":{"display_name":"TikTok","update_version_code":2021704040,"manifest_version_code":2021704040,"app_version_minor":"","aid":1233,"channel":"googleplay","package":"com.zhiliaoapp.musically","app_version":"17.4.4","version_code":170404,"sdk_version":"2.12.1-rc.5","sdk_target_version":29,"git_hash":"050d489d","os":"Android","os_version":"9","os_api":28,"device_model":"SM-G611M","device_brand":"samsung","device_manufacturer":"samsung","cpu_abi":"armeabi-v7a","release_build":"e1611c6_20200824","density_dpi":320,"display_density":"xhdpi","resolution":"1280x720","language":"en","timezone":1,"access":"wifi","not_request_sender":0,"mcc_mnc":"26203","rom":"G611MUBS6CTD1","rom_version":"PPR1.180610.011","cdid":cdid,"sig_hash":"e89b158e4bcf988ebd09eb83f5378e87","gaid_limited":0,"google_aid":google_aid,"openudid":openudid,"clientudid":clientudid,"region":"US","tz_name":"Europe\\/Berlin","tz_offset":7200,"oaid_may_support":False,"req_id":req_id,"apk_first_install_time":1653436407842,"is_system_app":0,"sdk_flavor":"global"},"_gen_time":1653464286461}
      
      headers = {
        "Host": "log-va.tiktokv.com",
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "passport-sdk-version": "17",
        "content-type": "application/octet-stream",
        "user-agent": "okhttp/3.10.0.1"
      }
      response = request("POST", url, headers=headers, data=bytes.fromhex(tt_encrypt(payload))).json()
      try:
       install_id = response["install_id_str"]
       device_id = response["device_id_str"]
       return {"install_id":install_id,"device_id":device_id,"openudid":openudid,'cdid':cdid}
      except:
       pass

 