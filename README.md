<p align="center">
  <img src="./src/images/glass-of-water-fotor-20231025223633.png" width="120" alt="Yep, this is a MS Paint logo" /></a>
</p>

# Water Time Project

A simple project to remind you to drink water

### Requirements
**Python version**: 3.10.6 

**Windows version**: Windows 10 Home Single Language
> Not tested in another verisions of windows yet

**Libs**: _All libs required are in [requirements.txt](./requirements.txt) file, at project root_

### Usage
To use this project, use pythow command to keep it in backgroud

E.G.

```shell
wattertimeproject/src> pythonw main.py
wattertimeproject/src>
```

By default, a notification like the image below will be displayed on your Windows every 40 minutes to remind you to drink water

![plot](./src/images/exemple_notify.PNG)

### Configuration

#### First run
Before run for the first time, goto file [run.cmd](./run.cmd) and change watertimehome variable in section setauto to the absolute path where the code is save

```shell
@echo off

if NOT [%1] == [] goto setvar
if [%1] == [] goto setauto

:setvar
set watertimehome=%1
goto run

:setauto:
set watertimehome=./src  # <-- here E.G: C:\users\foo\bar\watertimeproject\src\
goto run

:run
echo %watertimehome%
cd %watertimehome%
pythonw main.py >> ./logs/logs


```

> Note: You can pass the location as parameter to script, just run `run.cmd C:\users\foo\bar\watertimeproject\src`

#### Main Configuration
All settings can be found in the [config.yaml](./src/config.yaml) file

Lets explain all the keys

| key | type | default value | description |
|-----|------|---------------|-------------|
|interval | int | 50 | Time between notifications |
| type_interval | str | minutes | Value type for range, accepted values are described in the note below |
| lang | str | PT-BR | Language for presenting messages. See more in the language item |
| message_duration | int | 10 | Duration of display message |
| icon_path | str | ./images/glass-of-watter.ico | Location of message icon |
| lang_path | str |  ./lang/messages.json | language configuration path |

> type_interval: The valid values are:
>  * seconds: S, SEC, SECONDS
>  * minutes: M, MIN, MINUTES,
>  * hours: H, HOUR, HOURS

#### Language
Language file is a json with three keys:

| key | type | description |
|-----|------|-------------|
| lang |str | Language name, This value should be used in the lang parameter |
| title | str | Title in display message |
| message | str | Message to show |

##### Creating a new language
In [json file](./src/lang/messages.json) create a new key using the definition above, like this

```json
{
    "lang": "IT-IT",
    "title": "L'acqua potabile fa bene",
    "message": "Bevi qualche sorso"
}

```

Add this json to language file

```json
[
    {
        "lang": "PT-BR", 
        "title": "Beba Àgua",
        "message": "Mais vale uma pedra no caminho do que duas no rim"
    },
    
    {
        "lang": "EN-US",
        "title": "Drink watter",
        "message": "A stone in the road is better than one in the kidney"
    },

    {
        "lang": "ES-ES",
        "title": "Tiempo de Agua",
        "message": "¿Quieres que tus riñones sigan funcionando, muchacho?"
    },

    {
        "lang": "IT-IT",
        "title": "L'acqua potabile fa bene",
        "message": "Bevi qualche sorso"
    }
]
```

### Start with Windows

You can start the script in Windows when you logon.

Just create a powershell script or use the [run.cmd](run.cmd) and add this to Windows Task Scheduler


### Change logs

V 0.0.1 - Create project


