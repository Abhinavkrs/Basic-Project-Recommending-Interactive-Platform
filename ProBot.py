from random import randint
from selenium import webdriver

print ('Hi! I am Probot.\nYour project assistant at Science Canvas.\nI will guide you through.\nAnd will help you select a project as per your interest.\n:) ')

name = raw_input('Can you please tell me your name : ')

greetings = ['Hi.','Hello.','Wassup.','Hey.']
emotions = ['Nice.','Cool.','Fine.','Yes.']

l = randint(0,len(greetings)-1) #Generating a random integer

print greetings[l] + ' ' + name + '.' #Greeting user

std = raw_input('Which class are you studying in?\n')

if (std == '11' or '12'):

    print emotions[randint(0,len(emotions)-1)]
    for i in range(0,3):
            platform = raw_input('Which platform do you want to work on.(Enter the number corresponding to the section)\n1. Arduino\n2. RaspberryPi\n3. Other\n')
            if (platform == '1' or platform == '2' or platform == '3'):
                break
            print 'Invalid Input'
              
    if (platform == '1'):

        for i in range(0,3):

            try:

                budget = int(input('Since you are doing a project on Arduino, your budget must be more than atleast 600.\nEnter your budget : '))
                if (type(budget == int and budget > 600)):

                    break
                print 'Invalid Input'
            except:

                print 'Invalid Input.'
        
        basic = ['\n1. Super Blink','2. Motion Detector','3. Sound Sensor','4. PIR sensor','5. Arduino Booombox']

        intermidiate = ['\n1. Display sensor data on screen','2. Send text file values to Arduino','3. Computer animation using photo-resistor','4. Arduino Beatbox','5. e-Paper Barcode']

        advanced = ['\n1. SONAR','2. Home security using Cayenne']    
        
        l_basic = {1:'http://arduinobasics.blogspot.com.au/2011/05/superblink.html',2:'http://arduinobasics.blogspot.com.au/2012/08/3-axis-accelerometer-motion-detector.html',3:'http://arduinobasics.blogspot.com.au/2013/05/sound-sensor.html',4:'http://arduinobasics.blogspot.com.au/2013/12/pir-sensor-part-2.html',5:'http://arduinobasics.blogspot.com.au/2015/03/arduino-boombox.html'}

        l_intermidiate = {1:'http://arduinobasics.blogspot.com.au/2011/06/arduino-uno-photocell-sensing-light.html',2:'http://arduinobasics.blogspot.com.au/2012/05/reading-from-text-file-and-sending-to.html',3:'http://arduinobasics.blogspot.com.au/2012/06/jumper-arduino-controlled-animation.html',4:'http://arduinobasics.blogspot.com.au/2015/04/arduino-beatbox.html',5:'http://arduinobasics.blogspot.com/2015/01/e-paper-barcode-39.html'}

        l_advanced = {1:'http://arduinobasics.blogspot.com.au/2013/01/sonar-project-tutorial.html',2:'http://arduinobasics.blogspot.com.au/2016/08/arduino-based-security-project-using.html'}
        
        for i in range(0,3):

            try:

                pl = int(input('Level of project you want to work on.(Enter the number corresponding to the level)\n1. Basic\n2. Intermidiate\n3. Advanced\n'))
                if (type(budget == int)):

                    break
                print 'Invalid Input'
            except:

                print 'Invalid Input.'
        if (pl == 1):

            for i in basic:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_basic[project])
        elif (pl == 2):

            for i in intermidiate:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_intermidiate[project])
        elif (pl == 3):

            for i in advanced:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_advanced[project])
        else:

            print 'Invalid Input'
            
            
            
            
    if (platform == '2'):

        for i in range(0,3):

            try:

                budget = int(input('Since you are doing a project on RaspberryPi, your budget must be more than atleast 4000.\nEnter your budget : '))
                if (type(budget == int) and budget > 4000):

                    break
                print 'Invalid Input'
            except:

                print 'Invalid Input.'
        camera = ['\n1. LED Mirror','2. Thermal Camera','3. Webcam Robot']

        l_camera = {1:'http://fullscreennl.github.io/led-mirror/',2:'https://hackaday.io/project/7176-polapi',3:'https://diyhacking.com/raspberry-pi-webcam-robot/'}
        
        robotics = ['\n1. Ball tracking robot','2. MeArm','3. Flying Hunter Bot']
        
        l_robotics = {1:'https://www.hackster.io/junejarohan/ball-tracking-robot-7a9865',2:'https://hackaday.io/project/181-mearm-your-robot',3:'https://www.youtube.com/watch?v=E9NdQTNOJOA'}
        
        wifi = ['\n1. Music Player','2. Drone disabler']
        
        l_wifi = {1:'https://pimylifeup.com/raspberry-pi-music-player/',2:'http://makezine.com/projects/build-wi-fi-drone-disabler-with-raspberry-pi/'}
        
        for i in range(0,3):

            try:

                pl = int(input('Module you want to work on.(Enter the number corresponding to the module)\n1. Camera\n2. Robotics\n3. Wifi\n'))
                if (type(budget == int)):

                    break
                print 'Invalid Input'
            except:

                print 'Invalid Input.'
        if (pl == 1):

            for i in camera:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_camera[project])
        elif (pl == 2):

            for i in robotics:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_robotics[project])
        elif (pl == 3):

            for i in wifi:

                print i
            project = int(input('Enter the project you want to work on. (Enter the number corresponding to the project) : '))
            driver = webdriver.Chrome()
            driver.get(l_wifi[project])
        else:

            print 'Invalid Input'
        
    if(platform == '3'):
    	
        print 'Contact:\nAbhinav Kumar\nMob No. - 9003752022\nEmail - abhinavkrs@gmail.com\nFacebook - facebook.com/abhinav.kumar.kmr'
    
           
        
    


# In[ ]:




# In[ ]:



