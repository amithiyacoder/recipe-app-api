# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jira-gts-mheducation.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("amit.pal@mheducation.com", "ATATT3xFfGF0NjUxFZW8zq7QZpWaI2BPU1_yQRaarF5LIsRTNJ56mJ6bi6uJUdYOZ44ElSE84oSVK76cOsnPlYvKingsYhtOzXhvxJrLSt63MLAp_NCRvpaPX53g3QDyrJzeXgWmI52sj68Np08qdhEn5CoNVSm03-UpZ9j-9_dTeDvWIhd0H1U=8C2A401C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "assignee": {
                    "accountId": "62b07e41b8e499e567e7f111",
                    "accountType": "atlassian",
                    "active": 'True',
                    "avatarUrls": {
                        "16x16": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "24x24": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "32x32": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "48x48": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png"
                    },
                    "displayName": "Sujit Kumar Gupta",
                    "emailAddress": "sujitkumar.gupta@mheducation.com",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/user?accountId=62b07e41b8e499e567e7f111",
                    "timeZone": "America/New_York"
                },
    
     
   
    
     "customfield_10036": {
                    "accountId": "62b07e41b8e499e567e7f111",
                    "accountType": "atlassian",
                    "active": 'True',
                    "avatarUrls": {
                        "16x16": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "24x24": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "32x32": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                        "48x48": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png"
                    },
                    "displayName": "Sujit Kumar Gupta",
                    "emailAddress": "sujitkumar.gupta@mheducation.com",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/user?accountId=62b07e41b8e499e567e7f111",
                    "timeZone": "America/New_York"
                },
                "customfield_10037": {
                    "child": {
                        "id": "10641",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10641",
                        "value": "CSOM"
                    },
                    "id": "10626",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10626",
                    "value": "OTC/FA Support"
                },
                "customfield_10038": {
                    "child": {
                        "id": "10460",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10460",
                        "value": "Oracle OTC-Configuration"
                    },
                    "id": "10314",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10314",
                    "value": "Oracle OTC"
                },
                "customfield_10039": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "As per our observations we are finding new category account combinations assigned to products recently added to FBA AMAZON (204) organization. \nSince these are new combinations they are not included under the cost group set up.\n\nThus, the cost manager in Production is failing due to the above-mentioned issue.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "customfield_10044": "https://mheducation.sharepoint.com/sites/eqa/mhe_processes/Wiki%20Pages/Standards%20Documents.aspx",
               

                 "customfield_10058": [
                    {
                        "accountId": "62b07e41b8e499e567e7f111",
                        "accountType": "atlassian",
                        "active": 'True',
                        "avatarUrls": {
                            "16x16": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                            "24x24": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                            "32x32": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png",
                            "48x48": "https://secure.gravatar.com/avatar/cdbdf8d72c6ef4be426c4f9bdf409903?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FSG-6.png"
                        },
                        "displayName": "Sujit Kumar Gupta",
                        "emailAddress": "sujitkumar.gupta@mheducation.com",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/user?accountId=62b07e41b8e499e567e7f111",
                        "timeZone": "America/New_York"
                    }
                ],
                "customfield_10059": {
                    "id": "10681",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10681",
                    "value": "Config"
                },
                "customfield_10062": {
                    "id": "10687",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10687",
                    "value": "Help Desk"
                },
                "customfield_10063": "RITM0729540",
                "customfield_10065": [
                    {
                        "id": "10689",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10689",
                        "value": "Cross-Divisional"
                    }
                ],
                "customfield_10066": {
                    "id": "10711",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10711",
                    "value": "All Locations"
                },
                "customfield_10068": "https://github.mheducation.com/GTS/OTC/blob/main/config_workbook/FIN/FIN_CATEGORY_ACCTS_US.xlsm",
                "customfield_10074": {
                    "id": "10714",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10714",
                    "value": "Issue Resolution"
                },
               
                "customfield_10088": {
                    "id": "10721",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10721",
                    "value": "No"
                },
                
                "customfield_10095": {
                    "id": "10732",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10732",
                    "value": "Configuration"
                },
                "customfield_10096": {
                    "id": "10796",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10796",
                    "value": "Oracle"
                },
                
                "customfield_10100": 9.0,
                "customfield_10101": 9.0,
                "customfield_10102": "2023-07-14",
                "customfield_10103": "2023-07-14",
                "customfield_10110": [
                    {
                        "groupId": "f514c25b-d2de-45f3-8d91-21ec51387fa2",
                        "name": "GTS-OTC_FA Support-CSOM Technical SC",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/group?groupId=f514c25b-d2de-45f3-8d91-21ec51387fa2"
                    }
                ],
               
               
                "customfield_10138": {
                    "id": "10917",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/10917",
                    "value": "OTC/FA Support - Finance"
                },
                "customfield_10141": {
                    "id": "11050",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/customFieldOption/11050",
                    "value": "Oracle OTC - Oracle OTC-Configuration"
                },
                
                
             
               
                
              
               
              
                
             
               
    "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "To Add cost group in Category Accounts for newly added product in FBA AMAZON (204) organization.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "fixVersions": [
                    {
                        "archived": 'False',
                        "description": "BAU activities",
                        "id": "10119",
                        "name": "GTS-Production Support",
                        "released": 'False',
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/version/10119"
                    }
                ],
                
                "issuetype": {
                    "avatarId": 10321,
                    "description": "",
                    "hierarchyLevel": 0,
                    "iconUrl": "https://jira-gts-mheducation.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10321?size=medium",
                    "id": "10010",
                    "name": "Release Management Code Request",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/issuetype/10010",
                    "subtask": 'False'
                },
              
              
                "priority": {
                    "iconUrl": "https://jira-gts-mheducation.atlassian.net/images/icons/priorities/minor.svg",
                    "id": "3",
                    "name": "Medium",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/priority/3"
                },
                
                "project": {
                    "avatarUrls": {
                        "16x16": "https://jira-gts-mheducation.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10408?size=xsmall",
                        "24x24": "https://jira-gts-mheducation.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10408?size=small",
                        "32x32": "https://jira-gts-mheducation.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10408?size=medium",
                        "48x48": "https://jira-gts-mheducation.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10408"
                    },
                    "id": "10011",
                    "key": "GTSOTC",
                    "name": "GTS-Order to Cash",
                    "projectCategory": {
                        "description": "",
                        "id": "10020",
                        "name": "GTS",
                        "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/projectCategory/10020"
                    },
                    "projectTypeKey": "software",
                    "self": "https://jira-gts-mheducation.atlassian.net/rest/api/3/project/10011",
                    "simplified": 'False'
                },
               
    
 "summary": "Testing the JIRA ccount configuration.",
               
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))