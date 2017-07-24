# Logitech Dualshock F310 Connected to Arduino through PI

## Pre-requisits

### Install Python-dev

    $sudo apt-get install python-dev

### Install Evdev

    $sudo pip install evdev

## Configurations

### Raspi-Config

    $sudo raspi-config

    Interfaceing Options -> Serial

        Login Shell -> OFF

        Hardware Serial -> ON

        ssh -> ON(Optional)

## Serial script

### Installation and Execution

    First the default event in line 57
    of myApp.py is '/dev/input/event3'.
    This may vary depending on the Pi.
    Please navigate to the folder
    /dev/input/ without the controler
    plugged in and run $ls to see what
    events exist.  Plug in the controller
    and run $ls again.  The new event will
    be the event for the controller.

    Replace '/dev/input/eventX' in line
    57 with whatever number should be at
    the end of event.  

    Copy myApp.py to desired folder and ensure it has
    propper permissions

        $chmod +x myApp.py

    To run:

        $./myApp.py

### Outputs

  | Button | Code | Value(Down/UP) |
  |:------:|:----:|:--------------:|
  | X      | 0    | 1/0            |
  | A      | 1    | 1/0            |
  | B      | 2    | 1/0            |
  | Y      | 3    | 1/0            |
  | TL     | 4    | 1/0            |
  | TR     | 5    | 1/0            |
  | BL     | 6    | 1/0            |
  | BR     | 7    | 1/0            |
  | BACK   | 8    | 1/0            |
  | START  | 9    | 1/0            |
  | LJSBTN | 10   | 1/0            |
  | RJSBTN | 11   | 1/0            |
  | D-UP   | 13   | 1/0            |
  | D-DOWN | 14   | 1/0            |
  | D-LEFT | 15   | 1/0            |
  | D-RIGHT| 16   | 1/0            |
  | RJSANLX| 17   | 0-255          |
  | RJSANLY| 18   | 0-255          |
  | LJSANLX| 19   | 0-255          |
  | LJSANLY| 20   | 0-255          |

###### Termination Strings

  | Code | Value |
  |:----:|:-----:|
  | 888  |  999  |

###### Example Buffer Contents
    {'1','8','8','8','8','2','0','8','9','9','9'}

    Code: 18, Value: 208

## Connection to Arduino

    Tx from Pi should be directly connected to Rx on
    the Arduino.

    Ground on the Pi can be connected directly to ground
    on the Arduino.

###### Rx from Pi to Tx from Arduino

    Rx from the Pi requires a voltage divider to keep
    from smoking your Pi (3.3 volts vs 5.0 volts).

    This is accomplished with two resistors a 3.3 kOhm
     and kOhm 1.6.

    Connect the Rx of the Pi to a single node where both
    resistors branch off.  Connect the output of the
    1.6kOhm resistor to Tx on the Arduino and the output
    of the 3.3 kOhm resistor to ground.

## Reading the serial data from the Arduino

    Baud rate is 9600

    In the setup() function open the connection with
    Serial.begin(9600);

    In your loop read in data using a buffer long enough
    to store a single command per the protocol described
    above and then parse the data as necessary.
    You can read serial input on the Arduino with the
    Serial.read() function which returns a Byte.  This
    should be placed in a conditional statement that
    checks "if(Serial.available() > 0) {...}".
