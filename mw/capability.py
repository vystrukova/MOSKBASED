import os


def capability_select(device_os):
    if device_os == 'android_code':
        capability = {"platformName": "Android",
                      "platformVersion": "11.0",
                      "automationName": "Appium",
                      "appPackage": "ru.docsystems.mont",
                      "appActivity": "ru.docsystems.mont.SplashActivity",
                      "autoGrantPermissions": "true",
                      "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                          '../mont_app/mont.apk')
                                             ),
                      "orientation": "PORTRAIT"
                      }
    else:
        raise ValueError("Incorrect device os type")
    return capability
