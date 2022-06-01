from ctypes.wintypes import SIZE
from datetime import datetime
import json
import os
import collections
import sys
from tkinter import *
from tkinter import font as tkFont
from turtle import up
from typing import Counter

root = Tk()

mont_ttl = tkFont.Font(family='Consolas', size=20, weight='bold')
mont = tkFont.Font(family='Consolas', size=11, weight='bold')

root.title('Shopping List GUI')
root.geometry("600x650")
root.configure(bg='#4d5055')


cfp = os.path.dirname(__file__)
cfpl = os.path.join(cfp,"Lists")
inpt_aprv = ['Y', 'Yes', 'Ye', 'Yea', 'Yeah', 'Yh']
inpt_dny = ['N', 'No', 'Na', 'Nope']
cwd = os.getcwd()

os.chdir(cfp)
if not os.path.exists('Lists'):
    os.makedirs('Lists')
elif os.path.exists('Lists'):
    pass

#side_bar.pack(expand=False, fill='both', side='left', anchor='nw')

mainarea = LabelFrame(root, bg='#4d5055', width=500, height=500)
mainarea.pack(expand=True, fill='both', side='right')


class ButtonDesignWithEntry:
    def __init__(self,master,text,command):
        
        #declare variable
        self.command = command
        self.text = text

        self.entry = Entry(master, 
            width=20, 
            bg='#242425', 
            fg='white', 
            borderwidth='5', 
            insertbackground='white',
            font=mont)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>',self.command)

        self.button = Button(master, 
            text=self.text, 
            bg='#242425', 
            fg='white', 
            borderwidth='2',
            command=self.command,
            width=20,
            font=mont)
        self.button.pack(pady=10)

class StandardButton:
    def __init__(self,master,text,command):
        
        #declare variable
        self.command = command
        self.text = text

        self.button = Button(master, 
            text=self.text, 
            bg='#242425', 
            fg='white', 
            borderwidth='2',
            command=self.command,
            width=20,
            font=mont)
        self.button.pack(pady=10)

class LabelDesign:
    def __init__(self,master,text='Blank'):

        self.text = text
        self.master = master

        self.basic_label = Label(mainarea, 
            bg='#4d5055', 
            fg='white',
            font=mont,
            justify='center', 
            text=text)
        self.basic_label.pack(pady='10')



#######################################################################################
def new():
    partial_reset()
    def create_a_new_file_fn():
        request_new_file_name_instructions_labl = LabelDesign(mainarea,'What would you like to call your list?')
        def continue_new_file():
            print('Triggered continue_new_file()')
            partial_reset()
            new_file_name = create_list_entry_field.entry.get().title().rstrip()           
            if new_file_name == "":
                full_reset()
                print('Cannot enter a blank file name')
            else:
                partial_reset()
                request_new_file_name_instructions_updated = LabelDesign(mainarea,f'List: {new_file_name}')
                print(f'Here is your new file name: {new_file_name}')
                print(os.path.join(cfpl, new_file_name + '.json'))
                new_file_name_path = os.path.join(cfpl, new_file_name + '.json')
                os.chdir(cfp)
                #If there is no directory named "lists" to save the new files then one will be created
                if not os.path.exists('Lists'):
                    os.makedirs('Lists')
                    print(cwd)
                elif os.path.exists('Lists'):
                    #If a user tries to create a file that already exists they will be asked to enter a unique name
                    if os.path.exists(new_file_name_path):
                        print('There is already a shopping list with that name, please enter a unique name.')
                        main_menu  
                    elif not os.path.exists(new_file_name_path):
                        print(f'Unable to find file "{new_file_name}"')
                        #If a file name with new_file_name does not yet exist, a new file will be created in the "Lists" dir  
                        def create_new_file():
                                with open(new_file_name_path, 'w') as j_file:
                                    print(f'Creating Shopping List: {new_file_name}')
                                    sl = "Shopping List"
                                    data = {f'{sl}':f''}
                                    j_obj = json.dumps(data, indent=4)
                                    j_file.write(j_obj)
                                    j_file.close()

                                    


                                #Once a new list has been created the user will be asked to add items to the newly created list
                                def add_new_items_fn():
                                    print('Triggered add_new_items_fn()')
                                    add_new_items_instructions_label = LabelDesign(mainarea,'Add items to your list:')
                                    new_lbl = LabelDesign(mainarea,'')
                                    def add_new_items_update_list():
                                        print('Triggered add_new_items_update_list()')
                                        new_entry_box_item = add_new_items_submit_new_item_btn.entry.get().title().replace(" ","-").rstrip()
                                        
                                        if new_entry_box_item == "":
                                            pass
                                        elif not new_entry_box_item == "":
                                            with open(new_file_name_path, 'r+') as j_file:
                                                data = json.load(j_file)
                                                temp = data[f'{sl}']
                                                
                                                
                                                
                                                def writing():
                                                    add_new_items_submit_new_item_btn.entry.delete(0,'end')

                                                    new_lst = {sl: f'{temp}'+" "+ new_entry_box_item}
                                                    j_dump = json.dumps(new_lst, indent=4)
                                                    j_file.seek(0)
                                                    j_file.truncate()
                                                    j_file.write(j_dump)
                                                    j_file.seek(0)
          
                                                    json_read = j_file.read()
                                                    json_data = json.loads(json_read)
                                                    json_data_key = [json_data['Shopping List']]
                                                    json_data_key_str = str(json_data_key).strip(")(]['")
                                                    json_data_key_str_split = json_data_key_str.split(" ")
                                                    
                                                    json_data_key_str_split_filter_none_type =  list(filter(None,json_data_key_str_split))
                                                    
                                                    result = []
                                                    for i in json_data_key_str_split_filter_none_type:
                                                        j = json_data_key_str_split_filter_none_type.count(i)
                                                        my_data = f'{j} x {i}'
                                                        result.append(my_data)
                                                    
                                                    unique = dict.fromkeys(result)

                                                    for ii in unique:
                                                        print(ii)

                                                    new_lbl.basic_label.config(text=ii)
                                 
                                               
                                                    j_file.close()

                                                if not new_entry_box_item in data['Shopping List']:
                                                    print(f'Added an item to the list {new_file_name}: "{new_entry_box_item}"')
                                                    print(f'At location {new_file_name_path}')
                                                    
                                                    writing()
                                                         

                                                elif new_entry_box_item in data['Shopping List']:
                                                    print(f'Added more "{new_entry_box_item}" to the list {new_file_name}')
                                                    print(f'At location {new_file_name_path}')
                                                    
                                                    writing()
                                                    
                                                    
                                                else:
                                                    print('FAIL')
                                    
                                    add_new_items_submit_new_item_btn = ButtonDesignWithEntry(mainarea,'Add item',add_new_items_update_list)
                                    main_menu.button.pack()                                
                                    #add_new_items_update_list()
                                
                                add_new_items_fn()
                        create_new_file()
        create_list_entry_field = ButtonDesignWithEntry(mainarea,'Create list',continue_new_file)
        main_menu.button.pack()
    create_a_new_file_fn()
####################################################################################### 
def update_list():
    print('Triggered update_list()')
    partial_reset()
    update_file_name_instructions = LabelDesign(mainarea,'Which list would you like to edit?')
    
    def update_file():
        print('Triggered update_file()')
        partial_reset()
        list_to_update = update_file_entry.entry.get().title().rstrip()
        print(f'Searching for {list_to_update}')      
        list_to_update_new_path = (os.path.join(cfpl, list_to_update + '.json'))
        
        
        
        
        if os.path.exists(list_to_update_new_path):      
            
            partial_reset()
            list_to_update_lbl = LabelDesign(mainarea,'Your file exists')
            list_to_update_lbl_add_items = LabelDesign(mainarea,'Add items to your list: ')  
           
           
           
           
           
           
           
            def add_new_items_fn():
                list_to_update_btn.button.pack_forget()
                list_to_update_btn.entry.pack_forget()
                print('Triggered add_new_items_fn()')
                def add_new_items_update_list():
                    print('Triggered add_new_items_update_list()')
                    new_entry_box_item = list_to_update_btn.entry.get().title().replace(" ","-").rstrip()
           
                    if new_entry_box_item == "":
                        pass
                    elif not new_entry_box_item == "":
                        new_entry_box_item_label = LabelDesign(mainarea,new_entry_box_item)
                        with open(list_to_update_new_path, 'r+') as j_file:
                            c = json.load(j_file)
                            def write_over():
                                x = 'Shopping List'
                                y = c[f'{x}']
                                new_lst = {x: f'{y}' +","+" " + new_entry_box_item}
                                j_dump = json.dumps(new_lst, indent=4)
                                j_file.seek(0)
                                j_file.truncate()
                                j_file.write(j_dump)
                                j_file.close()
                                z = str(y).strip(",[]'").replace(",","").replace("'","")
                                z_ = z.split(" ")
                                z_.pop(0)
                                k = list(dict.fromkeys(z_))               

                            if new_entry_box_item == "":
                                add_new_items_update_list()
                            elif not new_entry_box_item in c['Shopping List']:
                                print(f'Added an item to the list {list_to_update_new_path}: "{new_entry_box_item}"')
                                print(f'At location {list_to_update_new_path}')
                                write_over()    
                                add_new_items_fn()      
                            elif new_entry_box_item in c['Shopping List']:
                                print(f'Added MORE "{new_entry_box_item}" to the list')
                                print(f'At location {list_to_update_new_path}')
                                write_over()                 
                                add_new_items_fn()               
                            else:
                                print('FAIL')
                add_new_items_submit_new_item_btn = ButtonDesignWithEntry(mainarea,'Add item',add_new_items_update_list)
            list_to_update_btn = ButtonDesignWithEntry(mainarea,'Add item',add_new_items_fn)
        elif not os.path.exists(list_to_update_new_path):
            list_to_update_lbl = LabelDesign(mainarea,'Your file does NOT exist.')
        
        update_file_entry = ButtonDesignWithEntry(mainarea,'Search for list',update_file)
        main_menu.button.pack()     
    update_file_entry = ButtonDesignWithEntry(mainarea,'Search for list',update_file) 
    main_menu.button.pack()
#######################################################################################
def delete_file():
    partial_reset()
    delete_file_name_instructions = LabelDesign(mainarea,'Which list would you like to delete?')
    
    def delete_file_cont():
        partial_reset()       
        file_to_delete = delete_cont_btn.entry.get().title().rstrip()
        file_to_delete_path = (os.path.join(cfpl, file_to_delete + '.json'))
        if file_to_delete == "":
            file_to_delete = None
            full_reset()
        else:
            main_menu.button.pack_forget()
            if os.path.exists(file_to_delete_path):
                file_to_delete_lbl = LabelDesign(mainarea,f'Sucessfully deleted: {file_to_delete}')
                os.remove(file_to_delete_path)
                main_menu.button.pack()
            elif not os.path.exists(file_to_delete_path):
                file_to_delete_lbl = LabelDesign(mainarea,'Your file does NOT exist.')
                main_menu.button.pack()
            pass
    delete_cont_btn = ButtonDesignWithEntry(mainarea,'DELETE',delete_file_cont)
    main_menu.button.pack()  
    def delete_all():
        partial_reset()
        del_all_labl = LabelDesign(mainarea,'Are you sure you want to delete all your lists?')
        def del_confirm():
            for i in os.listdir(cfpl):
                file_to_del = os.path.join(cfpl,i)
                os.remove(file_to_del)
                print(f'Deleted {file_to_del}')
            full_reset()
        def del_deny():
            full_reset()
        del_confirm_btn = StandardButton(mainarea,'Confirm',del_confirm)
        del_deny_btn = StandardButton(mainarea,'Deny',del_deny)
    delete_file_name_instructions_btn = StandardButton(mainarea,'Delete all lists',delete_all)
    
    main_menu.button.pack()
####################################################################################### DELETE COMPLETED
def print_file():
    partial_reset()
    print_file_name_instructions = LabelDesign(mainarea,'Which list would you like to print?')
    def print_file_cont():
        file_to_print = print_file_name_btn.entry.get().title().rstrip()
        print(file_to_print)
        file_to_print_path = (os.path.join(cfpl, file_to_print + '.json'))
        print_file_name_btn.button.pack_forget()
        print_file_name_btn.entry.pack_forget()
        if file_to_print == "":
            print('File name cannot be ""')
            full_reset()
        else:
            main_menu.button.pack_forget()
            if os.path.exists(file_to_print_path):
                print('Trying to trigger print_file()')
                print(f'File path: {file_to_print_path}')
                print('Triggered print_file()')
                with open(file_to_print_path, 'r') as j_file:
                    c = json.load(j_file)
                    x = 'Shopping List'
                    y = c[f'{x}']
                    z = str(y).strip(",[]'").replace(",","").replace("'","")
                    z_ = z.split(" ")
                    z_.pop(0)               
                    k = list(dict.fromkeys(z_))
                    print_lbl_0 = LabelDesign(mainarea,f"Here's your list: {file_to_print}")
                    for ii in k:
                        iii = z_.count(ii)
                        print(f'You have got {iii} x {ii}')
                        print_lbl = LabelDesign(mainarea,f'{iii} x {ii}')
                    main_menu.button.pack()
                    print_file_name_instructions.basic_label.pack_forget()                                 
            elif not os.path.exists(file_to_print_path):
                file_to_print_lbl = LabelDesign(mainarea,f"There is no list called: {file_to_print}")
                main_menu.button.pack()
    print_file_name_btn = ButtonDesignWithEntry(mainarea,'Print list',print_file_cont)
    main_menu.button.pack()
####################################################################################### PRINT COMPLETED    
def partial_reset():
    for widget in mainarea.winfo_children():
        widget.pack_forget()
def full_reset():
    partial_reset()
    opn_pack()
ttl_lbl = LabelDesign(mainarea,'Shopping List')
new_btn = StandardButton(mainarea,'New',new)
update_btn = StandardButton(mainarea,'Update',update_list)
print_btn = StandardButton(mainarea,'Print',print_file)
delete_btn = StandardButton(mainarea,'Delete',delete_file)
main_menu = StandardButton(mainarea,'Main menu',full_reset)
main_menu.button.pack_forget()
def opn_pack():
    ttl_lbl = LabelDesign(mainarea,'Shopping List')
    new_btn = StandardButton(mainarea,'New',new)
    update_btn = StandardButton(mainarea,'Update',update_list)
    print_btn = StandardButton(mainarea,'Print',print_file)
    delete_btn = StandardButton(mainarea,'Delete',delete_file)
    main_menu = StandardButton(mainarea,'Main menu',full_reset)
    main_menu.button.pack_forget()
root.mainloop()
                                    




                                    