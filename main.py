import PySimpleGUI as sg
from elevate import elevate
import write
import sys
import os

elevate()

path = os.getcwd()
chosenPath = path
sg.theme('DarkBrown4')
sg.set_global_icon('ASSINGMENTS.ico')

data = []
heading = ['Index','Name','Price','Quantity','Total','Link']
index = 0
tempStore = {}


layout = [
            [sg.Text("Amazon Estimation List \nDeveloped by Adwait Narayan Pradhan", relief=sg.RELIEF_RAISED, size = (99,0), justification='center',)],
            [sg.Table(values=data,headings = heading,justification='center',key = '-table-',
                    auto_size_columns=False,size=(90,15),hide_vertical_scroll=True,col_widths=(5,30,8,8,8,30),
                    header_background_color='brown',alternating_row_color='Yellow'),],
            [sg.Text('Name'),sg.Input(key='name', size=(34,0),do_not_clear=False),
            sg.Text('Price'),sg.Input(key='price', size=(8,0),do_not_clear=False),
            sg.Text('Quantity'),sg.Input(key='quantity', size=(4,0),do_not_clear=False),
            sg.Text('Link'),sg.Input(key='link', size=(34,0),do_not_clear=False),],
            [sg.Text("",size = (6,0)),
             sg.Button('Choose Location', size = (12,0),enable_events=True),
             sg.Text("",size = (4,0)),
            sg.Button('Generate Total', size = (12,0),enable_events=True),
            sg.Text("",size = (4,0)),       
            sg.Button('Update',enable_events=True),
            sg.Text("",size = (4,0)),       
            sg.Button('Write to File', size = (12,0),enable_events=True,disabled=True),
            sg.Text("",size = (4,0)),       
            sg.Button('Close', size = (12,0),enable_events=True)],
    
        ]

testWin = sg.Window('Amazon Estimation List',layout,keep_on_top=True)

sg.PopupAnnoying("Please be careful while entering the data, Duplicates are not checked and are directly written to the file.\nEverytime you click on the Write to file, New data pack is created and is written iinto the file,\nso ensure that before writting into the file you have entered all the dataor you can have multiple datapacks.",keep_on_top=True,grab_anywhere=False)

while True:
            
    event, values = testWin.read()   

    if event in (None, 'cancel','Close'):
        testWin.Close()
        sg.PopupAnnoying("Thank You for using my Application.",keep_on_top=True,auto_close=True,auto_close_duration=4)
        break

    elif event in ('Update'):
            if values['price'] != '' and values['name'] != '' and values['quantity'] != '' and values['link'] != '':
            
            try:
                index+=1
                dat1 =  [index,values['name'],values['price'],values['quantity'],str( int(values['quantity']) * int(values['price'])),values['link']]
                data.append(dat1)
                testWin['-table-'].update(values = data)
                write.ParseData(values)
                testWin['Write to File'].update(disabled = False)
            except ValueError:
                sg.PopupNoTitlebar('Problems with values of Price or Quantity',keep_on_top=True)
        else:
            
            sg.PopupNoTitlebar('Empty Feilds detected',button_type=None,keep_on_top=True)
            pass

    elif event in ('Generate Total'):
        total = write.Total()
        testWin['Update'].update(disabled = True)
        testWin['Generate Total'].update(disabled = True)
        testWin['Choose Location'].update(disabled = True)
        testWin['Write to File'].update(disabled = True)
        testWin['Close'].update(disabled = True)
        sg.popup_annoying(f"Your total expense will be {total}",icon=sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED,keep_on_top=True,)
        testWin['Update'].update(disabled = False)
        testWin['Generate Total'].update(disabled = False)
        testWin['Choose Location'].update(disabled = False)
        testWin['Write to File'].update(disabled = False)
        testWin['Close'].update(disabled = False)
            
    elif event in 'Choose Location':
        testWin['Update'].update(disabled = True)
        testWin['Generate Total'].update(disabled = True)
        testWin['Choose Location'].update(disabled = True)
        testWin['Write to File'].update(disabled = True)
        testWin['Close'].update(disabled = True)
        chosenPath = sg.PopupGetFolder("Please Browse to the location to save the file or continuw with the default path.",default_path=path,keep_on_top=True,)
        testWin['Update'].update(disabled = False)
        testWin['Generate Total'].update(disabled = False)
        testWin['Choose Location'].update(disabled = False)
        testWin['Write to File'].update(disabled = False)
        testWin['Close'].update(disabled = False)
            
    elif event in 'Write to File':
        testWin['Update'].update(disabled = True)
        testWin['Generate Total'].update(disabled = True)
        testWin['Choose Location'].update(disabled = True)
        testWin['Write to File'].update(disabled = True)
        testWin['Close'].update(disabled = True)
        status = write.WritetoCSV(path = chosenPath)
        sg.popup_annoying(f"Writing process sucessful.\nFile saved as 'Amazon Estimation list.csv' at {chosenPath}.\nOpen the file using Excel or any other application.",keep_on_top=True)
        testWin['Update'].update(disabled = False)
        testWin['Generate Total'].update(disabled = False)
        testWin['Choose Location'].update(disabled = False)
        testWin['Write to File'].update(disabled = False)
        testWin['Close'].update(disabled = False)
    
sys.exit(0)
