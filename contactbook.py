import PySimpleGUI as sg
import csv

sg.theme('DarkAmber')
sg.set_options(font='Arial 14')

layout = [
    [sg.Text('Contact Book', size=(30, 1), justification='center', font='Arial 20', relief=sg.RELIEF_RIDGE)],
    [sg.Text('Enter First Name'), sg.InputText(key='-fname-', size=(40, 1))],
    [sg.Text('Enter Last Name'), sg.InputText(key='-lname-', size=(40, 1))],
    [sg.Text('Enter Phone Number'), sg.InputText(key='-phone-', size=(40, 1))],
    [sg.Text('Enter Email'), sg.InputText(key='-email-', size=(40, 1))],
    [sg.Text('Enter Address'), sg.InputText(key='-address-', size=(40, 1))],
    [sg.Button('Save'), sg.Button('Cancel')],
    [sg.HorizontalSeparator()],
    [sg.Text('Search by First Name'), sg.InputText(key='-searchText-', size=(30, 1)), sg.Button('Search')],
    [sg.Button('Update'), sg.Button('Delete')],
    [sg.Text('', key='-searchOutput-', size=(60, 5), relief=sg.RELIEF_SUNKEN, font='Arial 12')],
]

window = sg.Window('Contact Book', layout, icon='favicon.ico', size=(500, 600), element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    fname = values['-fname-']
    lname = values['-lname-']
    phone = values['-phone-']
    email = values['-email-']
    address = values['-address-']
    searchText = values['-searchText-']
    
    if event == 'Save':
        if fname and phone:  # Basic validation
            with open('contacts.csv', 'a', newline='') as w:
                cw = csv.writer(w)
                cw.writerow([fname, lname, phone, email, address])
            window['-fname-'].update('')
            window['-lname-'].update('')
            window['-phone-'].update('')
            window['-email-'].update('')
            window['-address-'].update('')
            window['-searchOutput-'].update('Contact saved successfully!', text_color='green')
        else:
            window['-searchOutput-'].update('First Name and Phone Number are required.', text_color='red')
    
    if event == 'Search':
        found = False
        with open('contacts.csv', 'r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i[0].lower() == searchText.lower():  # Case-insensitive search
                    window['-searchOutput-'].update(
                        f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {i[3]}\nAddress: {i[4]}"
                    )
                    found = True
                    break
            if not found:
                window['-searchOutput-'].update("No contact found.", text_color='red')
    
    if event == 'Update':
        updated = False
        with open('contacts.csv', 'r') as r:
            contacts = list(csv.reader(r))
        with open('contacts.csv', 'w', newline='') as w:
            cw = csv.writer(w)
            for i in contacts:
                if i[0].lower() == searchText.lower():
                    updated_contact = [
                        fname if fname else i[0],
                        lname if lname else i[1],
                        phone if phone else i[2],
                        email if email else i[3],
                        address if address else i[4]
                    ]
                    cw.writerow(updated_contact)
                    updated = True
                else:
                    cw.writerow(i)
        if updated:
            window['-searchOutput-'].update("Contact updated successfully!", text_color='green')
        else:
            window['-searchOutput-'].update("No contact found.", text_color='red')
    
    if event == 'Delete':
        deleted = False
        with open('contacts.csv', 'r') as r:
            contacts = list(csv.reader(r))
        with open('contacts.csv', 'w', newline='') as w:
            cw = csv.writer(w)
            for i in contacts:
                if i[0].lower() == searchText.lower():
                    deleted = True
                else:
                    cw.writerow(i)
        if deleted:
            window['-searchOutput-'].update("Contact deleted successfully!", text_color='green')
        else:
            window['-searchOutput-'].update("No contact found to delete.", text_color='red')

window.close()
