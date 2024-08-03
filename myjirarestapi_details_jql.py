import requests
import oracledb
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import tkinter as tk
from tkinter import ttk

all_df = pd.DataFrame()
final_list=[]
#Iterating over json element

def oracle_connection(df2):
  # Dictionary with key-value pairs
  dropdown_options_instance = {
      'OTCDEV9':'oa2exa1-6w8ww-scan.exa.dsiad.oraclevcn.com:1521/ebs_OTCDEV9',
      'OTCDEV1':'oa2exa1-6w8ww-scan.exa.dsiad.oraclevcn.com:1521/ebs_OTCDEV1',
      
  }

  lib_dir = {
    'Install client Oracle':"C:\\Oracle\\Oracle11gR2_64bit\\product\\11.2.0\\client_1\\bin"

  }



  def submit_action(df2):
      dsn = dropdown_var1.get()
      dsn_value = dropdown_options_instance.get(dsn,"No values found")
      instant_cleint_dir = dropdown_var2.get()
      instant_cleint_dir_val= lib_dir.get(instant_cleint_dir,"No values found")
      text_value = text_field.get()

      
      
      oracledb.init_oracle_client(lib_dir=r"C:\\Oracle\\Oracle11gR2_64bit\\product\\11.2.0\\client_1\\bin")

      con = oracledb.connect(user="apps" , password=text_value , dsn=dsn_value)

      print("Database version:" , con.version)
   
      # Convert DataFrame to list of tuples
      tuples_list = [tuple(row) for index, row in df2.iterrows()]
    
      print(tuples_list)
      cursor = con.cursor()
      cursor.setinputsizes(None, 20)
      cursor.executemany("""
        insert into jira_kickback_details (PARENTDescription2, ParentKey , Project2 , Project_Description , KICK_dESCRIPTION ,KickBackJIRA)
        values (:1, :2, :3 , :4 , :5,:6  )""", tuples_list)
       
      con.commit() 
      root.destroy()





  print('This is the list')
  # Create the main window with specific dimensions
  root = tk.Tk()
  root.title("Dropdown and Text Field Example")
  root.geometry("700x500")

  # set minimum window size value
  root.minsize(700, 500)
  
  # set maximum window size value
  root.maxsize(700, 500)

  # Create a frame to hold the widgets and center it
  frame = ttk.Frame(root, padding="10")
  frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

  # Configure the grid to center the frame
  root.grid_rowconfigure(0, weight=1)
  root.grid_columnconfigure(0, weight=1)

  # Create labels for prompts
  label1 = ttk.Label(frame, text="Oracle user name")
  label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

  label2 = ttk.Label(frame, text="Oracle instance details")
  label2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

  label3 = ttk.Label(frame, text="Oracle password")
  label3.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

  # Create the first dropdown
  dropdown_var1 = tk.StringVar()
  dropdown1 = ttk.Combobox(frame, textvariable=dropdown_var1)
  dropdown1['values'] = list(dropdown_options_instance.keys())
  dropdown1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)


  # Create the second dropdown
  dropdown_var2 = tk.StringVar()
  dropdown2 = ttk.Combobox(frame, textvariable=dropdown_var2)
  dropdown2['values'] =list(lib_dir.keys())
  dropdown2.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

  # Create the text field
  text_field = ttk.Entry(frame)
  text_field.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

  # Create the submit button
  submit_button = ttk.Button(frame, text="Submit", command=lambda: submit_action(df2))
  submit_button.grid(row=6, column=0, padx=5, pady=5)

  # Start the main event loop
  root.mainloop()




def iterateDictIssues(issue_list, listInner): 
  
    # Now,the details for each Issue, maybe 
    # directly accessible, or present further, 
    # in nested dictionary objects. 
    for key, values in issue_list.items(): 
  
        # If key is 'fields', get its value, 
        # to fetch the 'summary' of issue. 
        if(key == "fields"): 
  
            # Since type of object is Json str, 
            # convert to dictionary object. 
            fieldsDict = dict(values) 
  
            # The 'summary' field, we want, is  
            # present in, further,nested dictionary 
            # object. Hence,recursive call to  
            # function 'iterateDictIssues'. 
            iterateDictIssues(fieldsDict, listInner) 
  
        # If key is 'reporter',get its value, 
        # to fetch the 'reporter name' of issue. 
        elif ( key == "summary"):
            keyIssue_summary_parent = values 
            listInner.append(keyIssue_summary_parent) 

        elif ( key == "key"):
            keyIssue_summary_parent_key = values 
            listInner.append(keyIssue_summary_parent_key)     

       
        elif(key == 'key'): 
            keyIssue = values 
            listInner.append(keyIssue) 
  
        # Get the value of key "summary",and, 
        # append to temporary list object, once matched. 
        elif(key == 'parent'): 
            # Since type of object is Json str, 
            # convert to dictionary object. 
            fieldsparent = dict(values) 
            iterateDictIssues(fieldsparent, listInner) 

            

        elif (key == 'project'):
            field_project = dict(values)   
            iterateDictIssues(field_project, listInner) 


        elif ( key =='name') :
            keyIssue_project = values 
            listInner.append(keyIssue_project) 
   
def main():          
    #Determine the project details
    url_project = "https://jira-gts-mheducation.atlassian.net/rest/api/3/project"
      # we are trying to do basic auth details using the jira token#
    auth = HTTPBasicAuth("amit.pal@mheducation.com", "ATATT3xFfGF0NjUxFZW8zq7QZpWaI2BPU1_yQRaarF5LIsRTNJ56mJ6bi6uJUdYOZ44ElSE84oSVK76cOsnPlYvKingsYhtOzXhvxJrLSt63MLAp_NCRvpaPX53g3QDyrJzeXgWmI52sj68Np08qdhEn5CoNVSm03-UpZ9j-9_dTeDvWIhd0H1U=8C2A401C")

    headers = {
        "Accept": "application/json"
      }

    url_ticket = "https://jira-gts-mheducation.atlassian.net/rest/api/3/search"

    response = requests.request(
        "GET",
        url_project,
        headers=headers,
        
        auth=auth
      )

    data_project = response.text
    print('Amit'+data_project)

      # Parse the string into a list of dictionaries
    projects = json.loads(data_project)



    project_list=[]

    valid_project= ["GTSOTC"]


    for project in projects:
      if  project["key"] in valid_project:
        project_list.append(project["key"])


    #print(project_list)

        #Determine the issue list for kickbacks
    for i in project_list:

          project_inst =i
          
                   
          query2_kickback = {
          'jql': f'project = {project_inst}   AND issuetype in ("") AND created >= 2024-06-01 AND created <= 2024-06-30 ORDER BY Rank ASC' 

                  }
          
          

          response_kickback = requests.request(
          "GET",
          url_ticket ,
          headers=headers,
          params=query2_kickback,
          auth=auth
          )

          # Get all project issues,by using the 
        # json loads method. 
          projectIssues = json.dumps(json.loads(response_kickback.text), 
                                  sort_keys=True, 
                                  indent=4, 
                                  separators=(",", ": ")) 
          
          projects_details = json.loads(projectIssues)

          final_issue_list = [] 

        # Iterate through the API output and look for key issues by iterating ind cotionary

          for key, value in projects_details.items(): 
            
            if(key == "issues"): 
                totalIssues = len(value) 
                for each_issue in range (totalIssues ):
                    listInner=[]
                    iterateDictIssues(value[each_issue], listInner )
                    final_issue_list.append(listInner)



          
          dfIssues = pd.DataFrame(final_issue_list, columns=["Description", 
                                                        "ParentKey", 
                                                        "Project" , 
                                                        "Project Description",
                                                        "Description",
                                                        "KickBackJIRA#"])
          

          final_list.append(dfIssues)

    all_df =pd.concat(final_list , ignore_index=True)

    #print(all_df)

    query2_kickback = {
          'jql': f'project = {project_inst}   AND issuetype in ("Kickback Sub-task") AND created >= 2024-06-01 AND created <= 2024-06-30 ORDER BY Rank ASC' 

                  }
          
          

    response_kickback = requests.request(
          "GET",
          url_ticket ,
          headers=headers,
          params=query2_kickback,
          auth=auth
        )

          # Get all project issues,by using the 
        # json loads method. 
    projectIssues = json.dumps(json.loads(response_kickback.text), 
                                  sort_keys=True, 
                                  indent=4, 
                                  separators=(",", ": ")) 
          
    projects_details = json.loads(projectIssues)

    

    oracle_connection(all_df)



main()
