from django.shortcuts import render
from django.contrib import auth
import json
from django.views.decorators.clickjacking import xframe_options_exempt

from django.http import HttpResponseRedirect,HttpResponse,JsonResponse

from datetime import datetime
import csv
import os
import glob
import shutil
from shutil import copyfile
from pathlib import Path
import re

from random import choice

#from AccessoryManager.settings import BASE_DIR
from pathlib import Path


@xframe_options_exempt
def location_query(request):

    if request.method == 'POST':
        json_data = json.loads(request.body.decode())
        print('************************************************************************')
        print(json_data)
        print(type(json_data))
        print('************************************************************************')

        if ('type' in json_data != False):

            if ('content' in json_data != False):
                
                type = json_data.get('type')
                content = json_data.get('content')
                
                csv_file = type+"_"+datetime.now().astimezone().strftime("%Y%m%d%H%M%S")+"_"+content+'.csv'
                '''
                folder = os.environ.get("PAT_Location_Query",
                    os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System'))
                fullpath = os.path.join(folder, csv_file)

                folder_2 = os.environ.get("PAT_Location_Query_FB",
                    os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System/iMES_Feedback'))
                fullpath_2 = os.path.join(folder_2, csv_file)
                
                with open(fullpath, 'w', newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                    [type, content])



                with open(fullpath_2, 'w', newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                    [type, '2F'])
                '''

                context = {
                    "status": "OK",
                    "csv": csv_file,
                    "retry_interval": 2,
                    "retry_max_times": 5
                }
            else:
                context = {
                    "status": "FAILED",
                    "csv": "",
                    "error_message": "content is not in body"
                }

        else:
            context = {
                "status": "FAILED",
                "csv": "",
                "error_message": "type is not in body"
            }

    else:
        context = {
            "status": "FAILED",
            "csv": "",
            "error_message": "Request is not in POST"
        }

    
    
    return JsonResponse(context)


@xframe_options_exempt
def location_query_content(request,csv):
    '''
    folder = os.environ.get("PAT_Location_Query_FB",
        os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System/iMES_Feedback'))

    backup = os.environ.get("PAT_Location_Query_FB_BAK",
        os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System/iMES_Feedback/Backup'))
    '''
    csv_title = str(csv).split('_')[0]

    targets = []
    '''
    for file in glob.glob(folder + "/*.csv"):
        if csv_title in file:
            targets.append(file)
            print(file)
    '''
    res = {
        "status": "UNKNOWN",
        "content": ""
    }
    '''
    if len(targets) == 0:
        return JsonResponse(res)
    '''

    random_list = [0,1,2]

    if choice(random_list) == 0:
        return JsonResponse(res)

    '''
    targets.sort(reverse=True)

    try:
        with open(targets[0], newline='', encoding="cp950") as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                rc = row[3]
                eqp = row[0]
                if len(row) > 7:
                    error_message = ','.join(row[7:])  # row[-1]
                else:
                    error_message = ""
                break
    except Exception as e:
        error_message = str(e)
    '''

    if csv_title == 'LotNo':
        content = '2F_WH'
    else:
        content = 'P20221200012'

    targets = ["SUCCESS"]
    if "SUCCESS" in targets[0].upper():
        res["status"] = "OK"
        res["content"] = content

    elif "FAIL" in targets[0].upper():
        res["status"] = "FAILED"
        res["content"] = ""
        res["error_message"] = error_message

    #fn = os.path.basename(targets[0])

    #shutil.move(targets[0], os.path.join(backup, fn))

    return JsonResponse(res)


@xframe_options_exempt
def location_create(request):

    if request.method == 'POST':
        json_data = json.loads(request.body.decode())
        print('************************************************************************')
        print(json_data)
        print(type(json_data))
        print('************************************************************************')

        if ('LotNo' in json_data != False):

            if ('LocationNo' in json_data != False):
                
                if ('LoginID' in json_data != False):

                    LotNo = json_data.get('LotNo')
                    LocationNo = json_data.get('LocationNo')
                    LoginID = json_data.get('LoginID')
                    
                    csv_file = LotNo+"_"+datetime.now().astimezone().strftime("%Y%m%d%H%M%S")+"_"+LocationNo+'.csv'
                    
                    # folder = os.environ.get("PAT_Location_Create",
                    #     os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System'))
                    # fullpath = os.path.join(folder, csv_file)

                    # with open(fullpath, 'w', newline='', encoding="utf-8") as csvfile:
                    #     writer = csv.writer(csvfile)
                    #     writer.writerow(
                    #     [LotNo, LocationNo, LoginID, datetime.now().astimezone().strftime("%Y%m%d%H%M%S")])


                    context = {
                        "status": "OK",
                        "csv": csv_file,
                        "retry_interval": 2,
                        "retry_max_times": 5
                    }

                else:
                    context = {
                        "status": "FAILED",
                        "csv": "",
                        "error_message": "LoginID is not in body"
                    }

            else:
                context = {
                    "status": "FAILED",
                    "csv": "",
                    "error_message": "LocationNo is not in body"
                }

        else:
            context = {
                "status": "FAILED",
                "csv": "",
                "error_message": "LotNo is not in body"
            }

    else:
        context = {
            "status": "FAILED",
            "csv": "",
            "error_message": "Request is not in POST"
        }

    
    
    return JsonResponse(context)

@xframe_options_exempt
def location_create_content(request,csv):

    # folder = os.environ.get("PAT_Location_Create_FB",
    #                             os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System/iMES_Feedback'))

    # backup = os.environ.get("PAT_Location_Create_FB_BAK",
    #     os.path.join(BASE_DIR, 'web/WIP_Location_Manager_System/iMES_Feedback/Backup'))

    csv_title = str(csv).split('_')[0]

    targets = []
    # for file in glob.glob(folder + "/*.csv"):
    #     if csv_title in file:
    #         targets.append(file)
    #         print(file)

    res = {
        "status": "UNKNOWN",
        "content": ""
    }

    # if len(targets) == 0:
    #     return JsonResponse(res)

    random_list = [0,1,2]

    if choice(random_list) == 0:
        return JsonResponse(res)

    #targets.sort(reverse=True)

    # try:
    #     with open(targets[0], newline='', encoding="cp950") as csvfile:
    #         rows = csv.reader(csvfile)
    #         for row in rows:
    #             rc = row[3]
    #             eqp = row[0]
    #             if len(row) > 7:
    #                 error_message = ','.join(row[7:])  # row[-1]
    #             else:
    #                 error_message = ""
    #             break
    # except Exception as e:
    #     error_message = str(e)

    targets = ["SUCCESS"]
    content = 'SUCCESS'

    if "SUCCESS" in targets[0].upper():
        res["status"] = "OK"
        res["content"] = content

    elif "FAIL" in targets[0].upper():
        res["status"] = "FAILED"
        res["content"] = ""
        res["error_message"] = error_message

    # fn = os.path.basename(targets[0])

    # shutil.move(targets[0], os.path.join(backup, fn))

    return JsonResponse(res)