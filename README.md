# RpiShutdown

This project provides a way to shutdown and/or restart the Raspberry PI by a button connected to the GPIO pin.

Hardware connection
========================

Connect the button to your RPI GPIO3, as follows:


   button pin 1   <------------> RPI GPIO3  (pin5)
    
   button pin 2   <------------> RPI Ground (pin6)


Software configuration
========================

Grab the python script shutdown.py and copy it over to your RPI local folder, for example, at:

  /home/pi/python/shutdown.py

Modify the /etc/rc.local, by adding the following script line before "exit 0":

  sudo python /home/pi/python/shutdown.py

All set! Now restart your RPI ...

Thereafter, when your RPI starts up, anytime pressing the button, it will shutdown your RPI; and pressing the button again, it will awake up your RPI again.

Have fun!
