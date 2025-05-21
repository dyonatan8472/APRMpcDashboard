from django.shortcuts import render, redirect
from django.db import connections
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import (PrmDatErrMngr, DmsDealDtl, DmsActvDtl, DmsPrepAccUsg, PrmFlexReportsStatus,
                     DmsPrepAccUsg,
                     DmsRechEvtDtl,
                     DmsActvThreshold,
                     DmsDealerCommsn, 
                     )

import pandas as pd
import csv
from zipfile import BadZipFile
from .utils import built_in_list, bulk_run
import subprocess
import datetime as dt
import psutil
from psutil import NoSuchProcess, process_iter
import glob
import os

USER_NAME = os.environ['USER']


# =======================================
def run_rcyerr() -> (bool, str):
    # =======================================
    command = ["runjobs", "PRMERRCRECTR", "DAILY"]
    try:
        output = subprocess.run(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    except Exception as e:
        return False, str(e)

    return True, ''


# =======================================
def get_disk_usage():
    # =======================================
    command = ["df", "-k"]
    output = subprocess.run(command, universal_newlines=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out_list = output.stdout.split('\n')
    match = [x for x in out_list if '/dev/mapper/vg_misc-tsa' in x and '%' in x]
    match = match[0]
    loc = match.index('%')
    disk_usage = int(match[loc - 3:loc])

    return disk_usage


def delete_users(users):
    pass


# Create your views here.


# =======================================
def monitor_processing(request):
    # =======================================
    sql_monitor_query = """
   WITH ac_control AS(    
 SELECT 
        'ac_control_01' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_01
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
 SELECT 
        'ac_control_02' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_02
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
 SELECT 
        'ac_control_03' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_03
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
   SELECT 
        'ac_control_04' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_04
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
   SELECT 
        'ac_control_05' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_05
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
     SELECT 
        'ac_control_06' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_06
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        UNION ALL
 SELECT 
        'ac_control_07' AS ac_control, file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias, TO_CHAR(SUM(wr_rec_quantity),'999,999,999'), TO_CHAR(COUNT(1),'999,999,999'), MIN(TO_DATE(sys_creation_date,'YYYY/MM/DD HH24:MI:SS')), 
        MAX(TO_DATE(sys_creation_date, 'YYYY/MM/DD HH24:MI:SS'))
    FROM 
        ac_control_07
    WHERE
        file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' AND sys_creation_date >= TO_DATE('2020-12-01','yyyy-mm-dd')
    GROUP BY 
        file_status, SUBSTR(file_name, 1, 4), cur_pgm_name, cur_file_alias, nxt_pgm_name, 
        nxt_file_alias
        )
        SELECT * FROM ac_control
        ORDER BY 
            CASE
                WHEN file_status = 'AF' THEN 0 ELSE 1
                END, 
            1,3
    """

    cursor = connections['default'].cursor()
    cursor.execute(sql_monitor_query)
    process_report = cursor.fetchall()
    current_datetime = dt.datetime.now()

    context = {
        "title": "Processing Monitor",
        "process_report": process_report,
        'current_datetime': current_datetime,
    }

    return render(request, "a_prm/process_report.html", context)


# =======================================
def activity_count(request):
    # =======================================
    sql_control_query = """
    WITH ac_control AS 
    (
    SELECT 'ac_control_01_rcy' AS ac_contr,cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1), '999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity), '999,999,999') AS file_count
FROM ac_control_01 WHERE file_status IN('RD', 'IU') AND file_name LIKE '%RCY' AND file_name NOT LIKE '%DROP%'
 GROUP BY 'ac_control_01', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_01' AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1), '999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity), '999,999,999') AS file_count
    FROM ac_control_01 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_01', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_02'  AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity), '999,999,999') AS file_count
    FROM ac_control_02 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_02', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_03'  AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity), '999,999,999') AS file_count
    FROM ac_control_03 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_03', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_04'  AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity), '999,999,999') AS file_count
    FROM ac_control_04 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_04', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_05'  AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity),'999,999,999') AS file_count
    FROM ac_control_05 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_05', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_06'  AS ac_contr, cur_file_alias, nxt_file_alias,file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity),'999,999,999') AS file_count
    FROM ac_control_06 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_06', cur_file_alias, nxt_file_alias, file_status
    UNION ALL
    SELECT 'ac_control_07'  AS ac_contr, cur_file_alias, nxt_file_alias, file_status, TO_CHAR(COUNT(1),'999,999,999') AS record_count, TO_CHAR(SUM(wr_rec_quantity),'999,999,999') AS file_count
    FROM ac_control_07 WHERE file_status IN ('RD', 'IU', 'AF') AND cur_pgm_name != 'ICERR' AND nxt_pgm_name != 'ICREPDRP' GROUP BY 'ac_control_07', cur_file_alias, nxt_file_alias, file_status)
    SELECT ac_contr, cur_file_alias, nxt_file_alias, file_status, record_count, file_count FROM ac_control
        ORDER BY 
            CASE
                WHEN file_status = 'AF' THEN 0 ELSE 1
                END, 
            1,2,4
    """

    cursor = connections['default'].cursor()
    cursor.execute(sql_control_query)
    control_report = cursor.fetchall()
    current_datetime = dt.datetime.now()

    context = {
        "title": "Activity Count",
        "control_report": control_report,
        "current_datetime": current_datetime,
    }

    return render(request, "a_prm/activity_count.html", context)


# =======================================
def load_cib(request):
    # =======================================
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You are not logged in! And that was very sneaky!!!')
    #     return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_cib.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_cib.html')

    request_id = int(request_id)

    cib_file = request.FILES["cib_file"]
    try:
        cib = pd.read_csv(cib_file)

        cib.columns = ['deal_id', 'dealr_cib', 'dlr_addl_cib', 'dlr_sales_agr', 'ata_reward_card', 'discount',
                       'special_deal',
                       'tenant_cd']
        cib['deal_id'] = cib['deal_id'].str.replace(' ', '')

    except BadZipFile:
        messages.warning(request, 'Problem with the cib file. Please check!!')
        return render(request, 'a_prm/load_cib.html')
    except Exception as e:
        messages.warning(request, ('Problem with the cib file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_cib.html')

    update_list = [dict(zip(cib.iloc[i].index.values, cib.iloc[i].values)) for i in range(len(cib))]

    for item in update_list:
        item['request_id'] = request_id

    insert_query = """INSERT INTO aprmrefwork.dms_deal_comm
        (sys_creation_date, application_id, dl_service_code, deal_id, dealr_cib, dlr_addl_cib, dlr_sales_agr, ata_reward_card, discount, special_deal, tenant_cd, operator_id) 
        VALUES (sysdate, 'ciupld', 'IMP', :deal_id, :dealr_cib, :dlr_addl_cib, :dlr_sales_agr, :ata_reward_card, :discount, :special_deal, :tenant_cd, :request_id)"""

    try:
        bulk_run('default', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading cib onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_cib.html')

    messages.success(request, f'CIB Upload successfully! {len(cib)} CIB entries were inserted.')

    return render(request, 'a_prm/load_cib.html')


# =======================================
def load_rib(request):
    # =======================================
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You are not logged in! And that was very sneaky!!!')
    #     return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_rib.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_rib.html')

    request_id = int(request_id)

    rib_file = request.FILES["rib_file"]
    try:
        rib = pd.read_csv(rib_file)

        rib.columns = ['dealer_rib', 'dlr_addl_rib', 'dlr_sales_agr_rib', 'ata_reward_card_rib', 'discount_rib',
                       'deal_id', 'special_deal', 'tenant_cd']
        
        rib['deal_id'] = rib['deal_id'].str.replace(' ', '')

    except BadZipFile:
        messages.warning(request, 'Problem with the rib file. Please check!!')
        return render(request, 'a_prm/load_rib.html')
    except Exception as e:
        messages.warning(request, ('Problem with the rib file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_rib.html')

    update_list = [dict(zip(rib.iloc[i].index.values, rib.iloc[i].values)) for i in range(len(rib))]

    for item in update_list:
        item['request_id'] = request_id

    insert_query = """INSERT INTO aprmrefwork.dms_deal_comm_rib
        (sys_creation_date, application_id, dl_service_code, dealer_rib, dlr_addl_rib, dlr_sales_agr_rib, ata_reward_card_rib, discount_rib, deal_id, special_deal, tenant_cd, operator_id) 
        VALUES (sysdate, 'ciupld', 'IMP', :dealer_rib, :dlr_addl_rib, :dlr_sales_agr_rib, :ata_reward_card_rib, :discount_rib, :deal_id, :special_deal, :tenant_cd, :request_id)"""

    try:
        bulk_run('default', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading rib onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_rib.html')

    messages.success(request, f'RIB Upload successfully! {len(rib)} RIB entries were inserted.')

    return render(request, 'a_prm/load_rib.html')

# =======================================
def load_threshold(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_threshold.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_threshold.html')

    request_id = int(request_id)

    threshold_file = request.FILES["threshold_file"]
    try:
        threshold = pd.read_csv(threshold_file)

        threshold.columns = ['dealer_cd', 'threshold_amt', 'tenant_cd']

    except BadZipFile:
        messages.warning(request, 'Problem with the dealer file. Please check!!')
        return render(request, 'a_prm/load_threshold.html')
    except Exception as e:
        messages.warning(request, ('Problem with the dealer file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_threshold.html')

    update_list = [dict(zip(threshold.iloc[i].index.values, threshold.iloc[i].values)) for i in range(len(threshold))]

    for item in update_list:
        item['request_id'] = request_id

    insert_query = """INSERT INTO aprmrefwork.dms_actv_threshold
     (sys_creation_date, application_id, dl_service_code, dealer_cd, threshold_amt, tenant_cd, operator_id) 
     VALUES (sysdate, 'dlupld', 'IMP', :dealer_cd, :threshold_amt, :tenant_cd, :request_id)"""

    try:
        bulk_run('refwork', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading threshold onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_threshold.html')

    messages.success(request, f'Threshold Upload successfully! {len(threshold)} threshold were inserted.')

    return render(request, 'a_prm/load_threshold.html')


# =======================================
def load_dealer_commission(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_dealer_commission.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_dealer_commission.html')

    request_id = int(request_id)

    dealer_commission_file = request.FILES["dealer_commission_file"]
    try:
        commission_rates = pd.read_csv(dealer_commission_file)
        commission_rates = commission_rates.drop(commission_rates.columns[:2], axis=1) # Removing the first two redundant columns
        commission_rates.columns = ['effective_date', 'commsn_code', 'partner_profile_cd', 'dealer_cd', 'comm_effective_date', 'qual_param_1_val', 'qual_param_2_val', 'qual_param_3_val', 'qual_param_4_val', 
                                    'qual_param_5_val', 'qual_param_6_val', 'qual_param_7_val', 'qual_param_8_val', 'qual_param_9_val', 'qual_param_10_val', 'slab_order', 'step_tier_ind', 
                                    'group_cd', 'from_slab', 'to_slab', 'slab_val', 'tenant_cd']


    except BadZipFile:
        messages.warning(request, 'Problem with the commission rates file. Please check!!')
        return render(request, 'a_prm/load_dealer_commission.html')
    except Exception as e:
        messages.warning(request, ('Problem with the commission rates file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_dealer_commission.html')

    update_list = [dict(zip(commission_rates.iloc[i].index.values, commission_rates.iloc[i].values)) for i in range(len(commission_rates))]

    for item in update_list:
        item['request_id'] = request_id

    insert_query = """INSERT INTO dms_dealer_commsn
     (sys_creation_date, application_id, dl_service_code, effective_date, commsn_code, partner_profile_cd, dealer_cd, comm_effective_date, qual_param_1_val, qual_param_2_val, 
     qual_param_3_val, qual_param_4_val, qual_param_5_val, qual_param_6_val, qual_param_7_val, qual_param_8_val, qual_param_9_val, qual_param_10_val, slab_order, step_tier_ind, 
     group_cd, from_slab, to_slab, slab_val, tenant_cd, operator_id) 
     VALUES (sysdate, 'dlupld', 'IMP', TO_DATE(:effective_date, 'YYYY-MM-DD'), :commsn_code, :partner_profile_cd, :dealer_cd, TO_DATE(:comm_effective_date, 'YYYY-MM-DD'), :qual_param_1_val, :qual_param_2_val, :qual_param_3_val, 
     :qual_param_4_val, :qual_param_5_val, :qual_param_6_val, :qual_param_7_val, :qual_param_8_val, :qual_param_9_val, :qual_param_10_val, :slab_order, :step_tier_ind, 
     null, :from_slab, :to_slab, :slab_val, :tenant_cd, :request_id)"""

    try:
        bulk_run('refwork', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading commission rates onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_dealer_commission.html')

    messages.success(request, f'Commission rates Upload successfully! {len(commission_rates)} commission rates were inserted.')

    return render(request, 'a_prm/load_dealer_commission.html')

# =======================================
def load_dealers(request):
    # =======================================
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You are not logged in! And that was very sneaky!!!')
    #     return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_dealers.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_dealers.html')

    request_id = int(request_id)

    dealers_file = request.FILES["dealers_file"]
    try:
        dealers = pd.read_csv(dealers_file)

        dealers.columns = ['dealer_cd', 'deal_id', 'deal_type', 'status', 'account_status', 'effective_date',
                           'expiration_date', 'tenant_cd']

        dealers['deal_id'] = dealers['deal_id'].str.replace(' ', '')

    except BadZipFile:
        messages.warning(request, 'Problem with the dealer file. Please check!!')
        return render(request, 'a_prm/load_dealers.html')
    except Exception as e:
        messages.warning(request, ('Problem with the dealer file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_dealers.html')

    update_list = [dict(zip(dealers.iloc[i].index.values, dealers.iloc[i].values)) for i in range(len(dealers))]

    for item in update_list:
        item['request_id'] = request_id

    insert_query = """INSERT INTO aprmrefwork.dms_deal_map
     (sys_creation_date, application_id, dl_service_code, dealer_cd, deal_id, deal_type, status, account_status, effective_date,
    expiration_date, tenant_cd, operator_id) VALUES (sysdate, 'dlupld', 'IMP', :dealer_cd, :deal_id, :deal_type, :status, :account_status, TO_DATE(:effective_date, 'YYYY-MM-DD'),
    TO_DATE(:expiration_date, 'YYYY-MM-DD'), :tenant_cd, :request_id)"""

    select_query = """SELECT dealer_cd, deal_id, deal_type, status, account_status, effective_date, expiration_date, tenant_cd FROM aprmrefwork.dms_deal_map WHERE
        dealer_cd = :dealer_cd AND deal_id = :deal_id AND deal_type = :deal_type AND status = :status AND account_status = :account_status
    """
    try:
        bulk_run('default', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading dealers onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_dealers.html')

    messages.success(request, f'Dealers Upload successfully! {len(dealers)} dealers were inserted.')

    return render(request, 'a_prm/load_dealers.html')


# =======================================
def load_deals(request):
    # =======================================
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You are not logged in! And that was very sneaky!!!')
    #     return render(request, 'index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/load_deals.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/load_deals.html')

    request_id = int(request_id)

    deals_file = request.FILES["deals_file"]
    try:
        deals = pd.read_csv(deals_file, converters={'DMS_DEAL_DTL.OFFER_CODE': str})
        deals.columns = ['deal_id', 'offer_code', 'service_type', 'deal_start_date', 'deal_type', 'contract_period',
                         'customer_cib', 'component_cost', 'deal_end_date', 'tenant_cd']
        
        deals['deal_id'] = deals['deal_id'].str.replace(' ', '')
        deals['offer_code'] = deals['offer_code'].str.replace(' ', '')

    except BadZipFile:
        messages.warning(request, 'Problem with the deals file. Please check!!')
        return render(request, 'a_prm/load_deals.html')
    except Exception as e:
        messages.warning(request, ('Problem with the deals file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_deals.html')

    update_list = [dict(zip(deals.iloc[i].index.values, deals.iloc[i].values)) for i in range(len(deals))]

    for item in update_list:
        item['request_id'] = request_id
        item['contract_period'] = str(item['contract_period'])

    insert_query = """INSERT INTO aprmrefwork.dms_deal_dtl
     (deal_id, offer_code, service_type, deal_start_date, deal_type, sys_creation_date, operator_id, dl_service_code, 
     contract_period, customer_cib, component_cost, deal_end_date, tenant_cd) 
     VALUES (:deal_id, :offer_code, :service_type, TO_DATE(:deal_start_date, 'YYYY-MM-DD'), :deal_type, sysdate, 
     :request_id, 'IMP', :contract_period, :customer_cib, :component_cost, 
     TO_DATE(:deal_end_date, 'YYYY-MM-DD'), :tenant_cd)"""

    try:
        bulk_run('refwork', insert_query, update_list)

    except Exception as e:
        messages.warning(request, ('Problem with loading dealers onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/load_deals.html')

    messages.success(request, f'Dealers Upload successfully! {len(deals)} deals were inserted.')

    return render(request, 'a_prm/load_deals.html')


# =======================================
def update_dealers(request):
    # =======================================
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You are not logged in! And that was very sneaky!!!')
    #     return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/update_dealers.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/update_dealers.html')

    request_id = int(request_id)

    dealers_file = request.FILES["dealers_file"]

    try:
        df = pd.read_excel(dealers_file)
    except BadZipFile:
        messages.warning(request, 'Problem with the dealer file. Please check!!')
        return render(request, 'a_prm/update_dealers.html')
    except Exception as e:
        messages.warning(request, ('Problem with the dealer file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/update_dealers.html')

    # Converting all column names to upper. This is due to Vincent's inconsistency.

    df['REQUEST_ID'] = int(request_id)

    df.columns = map(str.upper, df.columns)  # All column names to upper

    # update_dms_dealer = """UPDATE dms_actv_dtl SET sys_update_date = sysdate,  dealer_code = :dealer_code,
    #     comm_mdcode = :comm_mdcode, comm_sdcode = :comm_sdcode,
    #     comm_rocode = :comm_rocode, operator_id = :request_id
    #     WHERE edr_id = :edr_id"""

    try:
        update_params = df[['EDR_ID', 'UPDATED_DEALER_CODE', 'UPDATED_COMM_MDCODE',
                            'UPDATED_COMM_SDCODE', 'UPDATED_COMM_ROCODE', 'REQUEST_ID']].values.tolist()
    except KeyError:
        messages.success(request, 'Incorrect column names. Please check the file!')
        return render(request, 'a_prm/update_dealers.html')

    try:
        for edr_id, dealer_code, comm_mdcode, comm_sdcode, comm_rocode, request_id in update_params:
            DmsActvDtl.objects.filter(edr_id=edr_id).update(
                sys_update_date=timezone.now(),
                dealer_code=dealer_code,
                comm_mdcode=comm_mdcode,
                comm_sdcode=comm_sdcode,
                comm_rocode=comm_rocode,
                operator_id=request_id,
                application_id='dlrupd',
            )
        messages.success(request, f'Dealers Update Completed successfully! \n{len(df)} entries were updated.')
    except Exception as e:
        messages.warning(request, ('Problem with loading dealers onto database. Please check the following: ' + str(e)))

    return render(request, 'a_prm/update_dealers.html')


# =======================================
def update_rech_event_dealers(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/update_rech_event_dealers.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/update_rech_event_dealers.html')

    request_id = int(request_id)

    rech_events_file = request.FILES["rech_events_file"]

    try:
        df = pd.read_excel(rech_events_file, converters={'MSISDN': str, 'RECH_UNIQUE_NO': str})
    except BadZipFile:
        messages.warning(request, 'Problem with the rech events file. Please check!!')
        return render(request, 'a_prm/update_rech_event_dealers.html')
    except Exception as e:
        messages.warning(request, ('Problem with the rech events file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/update_rech_event_dealers.html')

    # Converting all column names to upper.

    df['REQUEST_ID'] = int(request_id)

    df.columns = map(str.upper, df.columns)  # All column names to upper

    try:
        update_params = df[['MSISDN', 'UPDATED_DEALER_CD', 'RECH_UNIQUE_NO', 'REQUEST_ID']].values.tolist()
    except KeyError:
        messages.success(request, 'Incorrect column names. Please check the file!')
        return render(request, 'a_prm/update_rech_event_dealers.html')

    try:
        for msisdn, dealer_cd, rech_unique_no, request_id in update_params:
            DmsRechEvtDtl.objects.filter(msisdn=msisdn, rech_unique_no=rech_unique_no).update(
                sys_update_date=timezone.now(),
                dealer_cd=dealer_cd,
                operator_id=request_id,
                application_id='evupld',
            )
        messages.success(request,
                         f'Dealers rech events update Completed successfully! \n{len(df)} entries were updated.')
    except Exception as e:
        messages.warning(request, (
                'Problem with loading rech events updates onto database. Please check the following: ' + str(e)))

    return render(request, 'a_prm/update_rech_event_dealers.html')


# =======================================
def purge_dm73_by_msisdn(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in!  And that was very sneaky!!!')
        return redirect('index.html')
    print('In purge_dm73_by_msisdn')
    if "GET" == request.method:
        return render(request, 'a_prm/purge_dm73_by_msisdn.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/purge_dm73_by_msisdn.html')

    request_id = int(request_id)

    errors_file = request.FILES["errors_file"]

    try:
        df = pd.read_excel(errors_file, converters={'MSISDN': str})

    except BadZipFile as e:
        return render(request, 'a_prm/purge_dm73_by_msisdn.html',
                      {'error_message': "Problem with the purge file. Please check the following: " + str(e)})
    except Exception as e:
        return render(request, 'a_prm/purge_dm73_by_msisdn.html',
                      {'error_message': "problem with the purge file. Please check the following: " + str(e)})

    df['OPERATOR_ID'] = int(request_id)

    update_for_purge = """UPDATE prm_dat_err_mngr SET operator_id = :operator_id, sys_update_date = sysdate, rec_handle_ind = 'X', 
                            next_process_ind = 'E' WHERE TRIM(originating_id) = :msisdn AND dominant_err_cd = 'DM73'"""

    try:
        update_params = df[['MSISDN', 'OPERATOR_ID']].values.tolist()
    except KeyError:
        messages.success(request, 'MSISDN column not found. Please check the document!')
        return render(request, 'a_prm/purge_dm73_by_msisdn.html')

    params_list = [{'msisdn': msisdn, 'operator_id': operator_id} for msisdn, operator_id in update_params]

    try:
        bulk_run('default', update_for_purge, params_list)
    except Exception as e:
        messages.success(request, ('Problem with loading errors list onto database. Please check!!' + e))
        return render(request, 'a_prm/purge_dm73_by_msisdn.html')

    command = ["runjobs", "PRMERRCRECTR", "DAILY"]
    try:
        output = subprocess.run(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    except Exception as e:
        messages.success(request, ('There was a problem with the PRMERRCRECTR job run! ' + e))
        return render(request, 'a_prm/purge_dm73_by_msisdn.html')

    if output.returncode == 0:
        messages.success(request, f"{len(df)} entries were purged successfully!")
    else:
        messages.success(request, 'There was a problem with the PRMERRCRECTR job run!')

    return render(request, 'a_prm/purge_dm73_by_msisdn.html')


# =======================================
def purge_errors(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in!  And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/purge_errors.html', {})

    request_id = request.POST.get("request_id").strip()

    if not request_id.isdecimal():
        messages.warning(request, 'Please supply a numeric value for request number!')
        return render(request, 'a_prm/purge_errors.html')

    request_id = int(request_id)

    errors_file = request.FILES["errors_file"]

    try:
        df = pd.read_excel(errors_file)

    except BadZipFile as e:
        return render(request, 'a_prm/purge_errors.html',
                      {'error_message': "problem with the purge file. Please check the following: " + str(e)})
    except Exception as e:
        return render(request, 'a_prm/purge_errors.html',
                      {'error_message': "problem with the purge file. Please check the following: " + str(e)})

    df['OPERATOR_ID'] = int(request_id)

    df.columns = map(str.upper, df.columns)  # All column names to upper

    update_for_purge = """UPDATE prm_dat_err_mngr SET operator_id = :operator_id, sys_update_date = sysdate, rec_handle_ind = 'X',
                            next_process_ind = 'E' WHERE edr_id = :edr_id AND dominant_err_cd = :dominant_err_cd"""

    try:
        update_params = df[['EDR_ID', 'DOMINANT_ERR_CD', 'OPERATOR_ID']].values.tolist()
    except KeyError:
        messages.success(request, 'EDR_ID, DOMINANT_ERR_CD or OPERATOR_ID column not found. Please check the file!')
        return render(request, 'a_prm/purge_errors.html')

    params_list = [{'edr_id': edr_id, 'dominant_err_cd': dominant_err_cd, 'operator_id': operator_id} for
                   edr_id, dominant_err_cd, operator_id in update_params]

    try:
        bulk_run('default', update_for_purge, params_list)
    except Exception as e:
        messages.success(request, ('Problem with loading errors list onto database. Please check!! ' + str(e)))
        return render(request, 'a_prm/purge_errors.html')

    command = ["runjobs", "PRMERRCRECTR", "DAILY"]
    try:
        output = subprocess.run(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    except Exception as e:
        messages.success(request, ('There was a problem with the PRMERRCRECTR job run! ' + str(e)))
        return render(request, 'a_prm/purge_errors.html')

    if output.returncode == 0:
        messages.success(request, f"{len(df)} entries were purged successfully!")
    else:
        messages.success(request, 'There was a problem with the PRMERRCRECTR job run!')

    return render(request, 'a_prm/purge_errors.html')


# =======================================
def dms_detail_report(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/dms_detail_report.html', {})

    id_number = request.POST.get("id_number").strip()

    # To remove duplicates
    rows = built_in_list(id_number)

    model_class = DmsDealDtl

    field_names = ['deal_id', 'offer_code', 'service_type', 'deal_start_date', 'deal_type',
                   'sys_creation_date', 'contract_period', 'customer_cib',
                   'component_cost', 'deal_end_date', 'tenant_cd']

    response = HttpResponse(content_type='text/csv')

    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response['Content-Disposition'] = f'attachment; filename="dms_detail_report_{current_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for obj in model_class.objects.filter(deal_id__in=rows):
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


# =======================================
def actv_detail_report(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/actv_detail_report.html', {})

    id_number = request.POST.get("id_number").strip()

    rows = built_in_list(id_number)

    model_class = DmsActvDtl

    meta = model_class._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')

    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response['Content-Disposition'] = f'attachment; filename="actv_detail_report_{current_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for obj in model_class.objects.filter(msisdn__in=rows):
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


# =======================================
def prus_detail_report(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/prus_detail_report.html', {})

    id_number = request.POST.get("id_number").strip()

    rows = built_in_list(id_number)

    model_class = DmsPrepAccUsg

    meta = model_class._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')

    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response['Content-Disposition'] = f'attachment; filename="prus_detail_report_{current_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for obj in model_class.objects.filter(msisdn__in=rows):
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


# =======================================
def usage_report(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/usage_report.html', {})

    id_number = request.POST.get("id_number").strip()

    rows = built_in_list(id_number)

    model_class = DmsPrepAccUsg

    meta = model_class._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')

    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response['Content-Disposition'] = f'attachment; filename="usage_report_{current_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for obj in model_class.objects.filter(msisdn__in=rows):
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


# =======================================
def dm69_update(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/dm69_update.html', {})

    dm69_file = request.FILES["dm69_file"]

    try:
        df = pd.read_excel(dm69_file, converters={'ORIGINATIN': str, 'SESSION_ID': str})

    except BadZipFile:
        return render(request, 'a_prm/dm69_update.html', {'upload_errors': "Problem with the dm69 file. Please check!"})
    except Exception as e:
        return render(request, 'a_prm/dm69_update.html',
                      {'upload_errors': "Problem with the dm69 file. Please check the following: " + str(e)})

    df.columns = map(str.upper, df.columns)

    update_dms_all = """UPDATE dms_actv_dtl SET sys_update_date = sysdate, ser_type = :ser_type, 
        offer_code = :offer_code, deal_id = :deal_id WHERE msisdn = :msisdn AND sim_seq_num = :sim_seq_num"""

    # update_dms_all = """UPDATE dms_actv_dtl SET sys_update_date = sysdate, ser_type = :ser_type, offer_code = :offer_code, deal_id = :deal_id 
    # WHERE msisdn = :msisdn AND trans_type = 'W' AND sim_seq_num = :sim_seq_num AND TO_CHAR(effective_date, 'YYYY-MM-DD HH24:MI:SS') = :effective_date"""
    # The above was commented out on 29-mar-2021

    # update_dms_no_offer = """UPDATE dms_actv_dtl_dummy SET sys_update_date = sysdate, ser_type = :ser_type, deal_id = :deal_id 
    # WHERE msisdn = :msisdn AND trans_type = 'W' AND sim_seq_num = :sim_seq_num AND TO_CHAR(effective_date, 'YYYY-MM-DD HH24:MI:SS') = :effective_date"""

    update_err_mngr = """UPDATE prm_dat_err_mngr SET sys_update_date = sysdate, rec_handle_ind = 'R', 
                    next_process_ind = 'E' WHERE edr_id = :edr_id"""

    update_params = []
    edr_id_list = []
    rejects_list = []

    for _, excel_row in df.iterrows():
        msisdn = excel_row['ORIGINATIN']
        sim_seq_num = excel_row['SESSION_ID']
        effective_date = excel_row['EVENT_START_DATETIME']
        edr_id = excel_row['EDR_ID']
        comments = excel_row['COMMENTS']

        ser_type = comments[51:54]
        if len(comments) == 136:
            offer_code = comments[71:76]
            deal_id = comments[89:99]
        elif len(comments) == 131:
            deal_id = comments[89:94]
            offer_code = comments[71:76]
        elif len(comments) == 123:
            offer_code = deal_id = comments[81:86]
        else:
            rejects_list.append(excel_row)
            continue

        edr_id_list.append({'edr_id': edr_id})

        update_params.append(
            {'msisdn': msisdn, 'sim_seq_num': sim_seq_num, 'ser_type': ser_type, 'offer_code': offer_code,
             'deal_id': deal_id, 'effective_date': effective_date})

    try:
        bulk_run('default', update_dms_all, update_params)

        bulk_run('default', update_err_mngr, edr_id_list)
    except Exception as e:
        return render(request, 'a_prm/dm69_update.html',
                      {'error_message': "Problem with loading errors list onto database. Please check!  " + str(e)})

    context = {
        'message': "Update Completed",
        'rejects_list': rejects_list
    }
    return render(request, 'a_prm/dm69_update.html', context)


# =======================================
def dm40_update(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/dm40_update.html', {})

    dm40_file = request.FILES["dm40_file"]

    try:
        df = pd.read_excel(dm40_file)

    except BadZipFile:
        return render(request, 'a_prm/dm40_update.html', {'upload_errors': "Problem with the dm40 file. Please check!"})
    except Exception as e:
        return render(request, 'a_prm/dm40_update.html',
                      {'upload_errors': "Problem with the dm40 file. Please check the following: " + str(e)})

    df.columns = map(str.upper, df.columns)

    try:
        update_params = df[['UPDATED_ACCOUNT_CD', 'EDR_ID']].values.tolist()
    except KeyError:
        messages.success(request, 'Incorrect column names. Please check the file!')
        return render(request, 'a_prm/dm40_update.html')

    try:
        for account_cd, edr_id in update_params:
            PrmDatErrMngr.objects.filter(edr_id=edr_id).update(
                sys_update_date=timezone.now(),
                rec_handle_ind='R',
                next_process_ind='E',
                account_cd=account_cd,
            )
    except Exception as e:
        return render(request, 'a_prm/dm40_update.html',
                      {'error_message': "Problem with loading errors list onto database. Please check!  " + str(e)})

    context = {
        'message': "Update Completed",
        # 'rejects_list': rejects_list
    }
    return render(request, 'a_prm/dm40_update.html', context)


# =======================================
def agent_details(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/agent_details.html', {})

    id_number = request.POST.get("id_number").strip()
    rows = built_in_list(id_number)

    id_numbers = "('{0}')".format("','".join(map(str, rows)))

    query = f"""SELECT usr.sys_creation_date creation_date, map.agent_id agent_id , map.account_cd account_cd, info.org_name account_org, usr.first_name name, 
    usr.last_name last_name, map.sub_dealer_id, info1.org_name sub_dealer_org, map.retail_outlet_id, info2.org_name retail_outlet_org
    FROM dms_ro_agent_map_v map 
    LEFT JOIN prm_users usr ON usr.user_cd = map.account_cd
    LEFT JOIN dms_acc_addl_info info ON info.account_cd = map.account_cd
    LEFT JOIN dms_acc_addl_info info1 ON info1.account_cd = map.sub_dealer_id
    LEFT JOIN dms_acc_addl_info info2 ON info2.account_cd = map.retail_outlet_id
    WHERE agent_id IN {id_numbers}"""

    cursor = connections['default'].cursor()

    cursor.execute(query)
    output = cursor.fetchall()

    context = {
        "title": "Agent details",
        "agent_details": output
    }
    return render(request, "a_prm/agent_details.html", context)


# =======================================
def msisdn_details(request):
    # =======================================
    if "GET" == request.method:
        return render(request, 'a_prm/msisdn_details.html', {})

    msisdn = request.POST.get("msisdn").strip()

    full_content = request.POST.get('full_content', False)

    query = f"""SELECT edr_id, msisdn, old_msisdn, order_action_id, trans_type,  effective_date, expiration_date, sys_creation_date, sim_seq_num, ser_type, 
                offer_code, deal_id, dealer_code, comm_mdcode, comm_sdcode, comm_rocode
                 FROM dms_actv_dtl WHERE msisdn = '{msisdn}' 
                AND order_action_Id != 'BULKCEASE90' 
                ORDER BY TO_NUMBER(order_action_id) DESC, expiration_date desc, edr_id DESC"""

    cursor = connections['default'].cursor()

    cursor.execute(query)
    msisdn_output = cursor.fetchall()

    if full_content:
        err_query = f"""SELECT edr_id, iecd event_type, get_adu_value(adu, '0095') order_action_id, qual_param_2_val trans_type, TRIM(future_12) new_msisdn, 
        session_id sim_seq_num, future_11 new_sim_seq_num, dominant_err_cd, event_start_datetime, future_1, qual_param_1_val ser_type, qual_param_3_val offer_code, qual_param_4_val deal_id
        FROM prm_dat_err_mngr WHERE TRIM(originating_id) = '{msisdn}'"""

        cursor.execute(err_query)
        err_output = cursor.fetchall()
    else:
        err_output = None

    context = {
        "title": "MSISDN details",
        "msisdn": msisdn,
        "msisdn_details": msisdn_output,
        "err_details": err_output,

    }
    return render(request, "a_prm/msisdn_details.html", context)


# =======================================
def delete_dealer(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/delete_dealer.html', {})

    delete_queries = [
        "DELETE FROM aprmrefwork.prm_accounts WHERE account_cd = :1",
        "DELETE FROM aprmrefwait.prm_accounts WHERE account_cd = :1",
        "DELETE FROM aprmrefwork.prm_acc_business_dtls WHERE account_cd = :1",
        "DELETE FROM aprmrefwait.prm_acc_business_dtls WHERE account_cd = :1",
        "DELETE FROM aprmrefwait.prm_users WHERE user_cd = :1",
        "DELETE FROM aprmrefwork.prm_users WHERE user_cd = :1",
        "DELETE FROM aprmrefwork.prm_acc_financial_dtls WHERE account_cd = :1",
        "DELETE FROM aprmrefwait.prm_acc_financial_dtls WHERE account_cd = :1",
        "DELETE FROM aprmrefwork.prm_acc_contact_dtls WHERE account_cd = :1",
        "DELETE FROM aprmrefwait.prm_acc_contact_dtls WHERE account_cd = :1"
    ]

    id_number = request.POST.get("id_number").strip()
    rows = built_in_list(id_number)

    id_numbers = "('{0}')".format("','".join(map(str, rows)))

    get_dealer_from_sec_user = f"""SELECT user_id FROM sec_user WHERE user_id IN {id_numbers}"""

    cursor = connections['default'].cursor()

    cursor.execute(get_dealer_from_sec_user)
    agents_in_sec_user = cursor.fetchall()

    if agents_in_sec_user:
        agents_in_sec_user = [item[0] for item in agents_in_sec_user]
        agents_in_sec_user = tuple(agents_in_sec_user)
        context = {
            'title': 'Agents still in sec_user',
            'agents_in_sec_user': agents_in_sec_user
        }
    else:

        context = {

        }
    return render(request, 'a_prm/delete_dealer.html', context)


# =======================================
def aprm_error_count(request):
    # =======================================
    # current_bill_date = dt.datetime.today().strftime("01-%b-%Y")

    get_total_errors = """SELECT a.dominant_err_cd ,b.err_desc ,
            DECODE(a.phy_file_id, 999999999,'TELKOM/RECON' , 999999998, 'TELKOM/RECON', 999999997, 'TELKOM/RECON', 
            999999996,'TELKOM/RECON', 999999995, 'TELKOM/RECON', 999999994, 'TELKOM/RECON', 999999991, 'AMDOCS', 
            999999990,'TELKOM', 999999993, 'AMDOCS', c.error_target) error_target,
            DECODE(a.phy_file_id, 999999999, 'MSISDN CEASED BEFORE EVENT START_TIME', 999999998, 
            'CEASE ORDER NOT FOUND ON OMS_APRM_RECON', 999999997, 'MSISDN does not exist on DMS_ACTV_DTL', 999999996, 
            'DM12 Related', 999999995,'Missing transactions', 999999994, 
            'RECORD START TIME BEFORE THE MIN EFFECTIVE_DATE IN DMS_ACTV_DTL', 999999991, 
            'Missing Offer code or Deal ID', 999999990, 'Telkom Dependent', 999999993, 'DM12 Related', 'N/A') comments, 
            TO_CHAR(COUNT(1),'999,999,999') 
            FROM prm_dat_err_mngr a, ic_error_codes b, error_targets c
            WHERE a.dominant_err_cd = b.error_code
            AND a.dominant_err_cd = c.error_code
            group by a.DOMINANT_ERR_CD ,b.ERR_DESC ,
            DECODE(a.phy_file_id, 999999999, 'TELKOM/RECON', 999999998,'TELKOM/RECON', 999999997, 'TELKOM/RECON', 
            999999996, 'TELKOM/RECON', 
            999999995, 'TELKOM/RECON', 999999994, 'TELKOM/RECON', 999999991, 'AMDOCS', 999999990, 'TELKOM', 999999993, 
            'AMDOCS', c.error_target),
            DECODE(a.phy_file_id, 999999999,'MSISDN CEASED BEFORE EVENT START_TIME', 999999998, 
            'CEASE ORDER NOT FOUND ON OMS_APRM_RECON',
            999999997,'MSISDN does not exist on DMS_ACTV_DTL', 999999996,'DM12 Related', 999999995, 
            'Missing transactions',
            999999994,'RECORD START TIME BEFORE THE MIN EFFECTIVE_DATE IN DMS_ACTV_DTL', 999999991, 
            'Missing Offer code or Deal ID',
            999999990,'Telkom Dependent', 999999993,'DM12 Related', 'N/A') ORDER BY 5 DESC"""

    get_older_errors = """SELECT a.dominant_err_cd, b.err_desc, 
        DECODE(A.PHY_FILE_ID, 999999999,'TELKOM/RECON', 999999998, 'TELKOM/RECON', 999999997, 'TELKOM/RECON', 999999996,
        'TELKOM/RECON',
        999999995,'TELKOM/RECON', 999999994,'TELKOM/RECON', 999999991, 'AMDOCS', 999999990, 'TELKOM',
        999999993,'AMDOCS', c.error_target) error_target, DECODE(a.phy_file_id,
        999999999,'MSISDN CEASED BEFORE EVENT START_TIME' ,
        999999998,'CEASE ORDER NOT FOUND ON OMS_APRM_RECON',
        999999997,'MSISDN does not exist on DMS_ACTV_DTL',
        999999996,'DM12 Related',
        999999995,'Missing transactions',
        999999994,'RECORD START TIME BEFORE THE MIN EFFECTIVE_DATE IN DMS_ACTV_DTL',
        999999991,'Missing Offer code or Deal ID',
        999999990,'Telkom Dependent',
        999999993,'DM12 Related',
        'N/A') comments ,TO_CHAR(COUNT(1),'999,999,999')
        FROM prm_dat_err_mngr a , ic_error_codes b , error_targets C
        WHERE a.dominant_err_cd = b.error_code
        AND a.dominant_err_cd = c.error_code
        AND a.event_start_datetime < (SELECT TRUNC(LAST_DAY(logical_date)) -60 FROM logical_date WHERE expiration_date IS NULL AND logical_date_type = 'B')
        GROUP BY a.dominant_err_cd ,b.err_desc ,
        DECODE(a.phy_file_id, 999999999, 'TELKOM/RECON' , 999999998, 'TELKOM/RECON', 999999997, 'TELKOM/RECON', 
        999999996, 'TELKOM/RECON',
        999999995,'TELKOM/RECON', 999999994, 'TELKOM/RECON', 999999991, 'AMDOCS', 999999990, 'TELKOM', 999999993, 
        'AMDOCS', C.ERROR_TARGET),
        DECODE(a.phy_file_id,
        999999999,'MSISDN CEASED BEFORE EVENT START_TIME' ,
        999999998,'CEASE ORDER NOT FOUND ON OMS_APRM_RECON',
        999999997,'MSISDN does not exist on DMS_ACTV_DTL',
        999999996,'DM12 Related',
        999999995,'Missing transactions',
        999999994,'RECORD START TIME BEFORE THE MIN EFFECTIVE_DATE IN DMS_ACTV_DTL',
        999999991,'Missing Offer code or Deal ID',
        999999990,'Telkom Dependent',
        999999993,'DM12 Related',
        'N/A')
        ORDER BY 5 DESC"""

    cursor = connections['default'].cursor()
    cursor.execute(get_total_errors)
    total_errors = cursor.fetchall()
    cursor.execute(get_older_errors)
    older_errors = cursor.fetchall()

    context = {
        "title": "Error Count Report",
        "total_errors": total_errors,
        "older_errors": older_errors,
    }

    return render(request, "a_prm/aprm_error_count.html", context)


# =======================================
def detail_error_report(request):
    # =======================================
    model_class = PrmDatErrMngr

    meta = model_class._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response['Content-Disposition'] = f'attachment; filename="detail_error_report_{current_date}.csv"'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in model_class.objects.all():
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


# =======================================
def recycle_errors(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    command = ["runjobs", "PRMERRCRECTR", "DAILY"]
    try:
        output = subprocess.run(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        # raise Exception("Problem with command for runjobs", e)
        messages.success(request, 'Problem with runjobs. Please check!')

        # return render(request, 'a_prm/recycle_errors.html', {'error_message': "Problem with runjobs. Please check! " + str(e)})
        return render(request, 'a_prm/recycle_errors.html')

    if output.returncode == 0:
        messages.success(request, 'PRMERRCRECTR job run terminated successfully!')
    else:
        messages.success(request, 'There was a a problem with the PRMERRCRECTR job run!')

    return render(request, 'a_prm/recycle_errors.html')


# --------------------------
def get_processes():
    # --------------------------

    while True:
        try:
            process_list = [proc for proc in psutil.process_iter(attrs=("name", "create_time")) if
                            proc.username() == USER_NAME]
        except psutil.NoSuchProcess:
            continue
        break

    process_dicts = [{"pid": proc.pid, "create_time": proc.create_time()} for proc in process_list]

    return process_dicts


# =======================================
def daemon_status(request):
    # =======================================

    DAEMONS = [
        ('LISTINER', 'gutl_classes', 'gutl_classes', 'grep'),
        ('EVENT_MANAGER_DEF', 'icsmpgum', 'icsmpgum', 'ICUSGMGR'),
        ('EVENT_MANAGER_1', 'icsmpgum', 'ICUSGMGR1', 'grep'),
        ('EVENT_MANAGER_2', 'icsmpgum', 'ICUSGMGR2', 'grep'),
        ('EVENT_MANAGER_3', 'icsmpgum', 'ICUSGMGR3', 'grep'),
        ('EVENT_MANAGER_4', 'icsmpgum', 'ICUSGMGR4', 'grep'),
        ('EVENT_MANAGER_5', 'icsmpgum', 'ICUSGMGR5', 'grep'),
        ('EVENT_MANAGER_6', 'icsmpgum', 'ICUSGMGR6', 'grep'),
        ('EVENT_MANAGER_7', 'icsmpgum', 'ICUSGMGR7', 'grep'),
        ('RATER_DEF', 'ICRATER', 'ICRTDEF', 'grep'),
        ('RATER_1', 'ICRT001', 'ICRT001', 'grep'),
        ('RATER_2', 'ICRT002', 'ICRT002', 'grep'),
        ('RATER_3', 'ICRT003', 'ICRT003', 'grep'),
        ('RATER_4', 'ICRT004', 'ICRT004', 'grep'),
        ('RATER_5', 'ICRT005', 'ICRT005', 'grep'),
        ('RATER_6', 'ICRT006', 'ICRT006', 'grep'),
        ('RATER_7', 'ICRT007', 'ICRT007', 'grep'),
        ('UPLOAD_RATED_USAGE_DEF', 'prm_upload_rated_usg', 'prm_upload_rated_usg', 'UPRTUSAGE'),
        ('UPLOAD_RATED_USAGE_1', 'UPRTUSAGE1', 'UPRTUSAGE1', 'grep'),
        ('UPLOAD_RATED_USAGE_2', 'UPRTUSAGE2', 'UPRTUSAGE2', 'grep'),
        ('UPLOAD_RATED_USAGE_3', 'UPRTUSAGE3', 'UPRTUSAGE3', 'grep'),
        ('UPLOAD_RATED_USAGE_4', 'UPRTUSAGE4', 'UPRTUSAGE4', 'grep'),
        ('UPLOAD_RATED_USAGE_5', 'UPRTUSAGE5', 'UPRTUSAGE5', 'grep'),
        ('UPLOAD_RATED_USAGE_6', 'UPRTUSAGE6', 'UPRTUSAGE6', 'grep'),
        ('UPLOAD_RATED_USAGE_7', 'UPRTUSAGE7', 'UPRTUSAGE7', 'grep'),
    ]

    number_of_fins = len(glob.glob('/users/tsa/prdprm1/var/tsa/LSN/input1/*.FIN'))
    disk_usage = get_disk_usage()

    processes = get_processes()

    daemon_status_list = []

    for daemon, job, i_process, rec in DAEMONS:

        command = f'ps -fu {USER_NAME} | grep -e {job} | grep {i_process} |grep -v {rec} | grep -v grep'
        try:
            process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        except subprocess.CalledProcessError:
            daemon_state = None
        else:
            daemon_state = process.stdout.strip()

        if daemon_state:
            _, pid, *_ = daemon_state.split()
            for process_time in processes:
                if process_time.get('pid') == int(pid):
                    row = (
                        daemon,
                        dt.datetime.fromtimestamp(process_time.get('create_time')).strftime("%H:%M:%S %d-%m-%Y"),
                        'Up')
        else:
            row = (daemon, '', 'Down')

        daemon_status_list.append(row)

        current_datetime = dt.datetime.now()

    context = {
        "daemon_status": daemon_status_list,
        "disk_usage": disk_usage,
        "number_of_fins": number_of_fins,
        "current_datetime": current_datetime,
    }

    return render(request, "a_prm/daemon_status.html", context)


# =======================================
def dm48_missing_deals(request):
    # =======================================
    query = """SELECT DISTINCT future_1 dealer_cd, qual_param_4_val deal_id, dtl.offer_code, dtl.service_type, dtl.deal_start_date, dtl.deal_end_date FROM prm_dat_err_mngr err
                JOIN dms_deal_dtl dtl ON qual_param_4_val = dtl.deal_id
                WHERE dominant_err_cd IN ('DM48')
                AND NOT EXISTS (SELECT 1 FROM dms_deal_map WHERE future_1 = dealer_cd AND qual_param_4_val = deal_id AND expiration_date > TRUNC(sysdate))
                ORDER BY 1,2,3"""

    # cursor = connections['aprm'].cursor()
    conn = connections

    df = pd.read_sql_query(query, conn)
    # cursor.execute(query)
    # rows = cursor.fetchall()

    heading = ['DEALER_CD', 'DEAL_ID', 'OFFER_CODE', 'SERVICE_TYPE', 'DEAL_START_DATE', 'DEAL_END_DATE']

    df['DEAL_ID'].astype(str)
    df['OFFER_CODE'].astype(str)

    response = HttpResponse(content_type='text/csv')
    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response[
        'Content-Disposition'] = f'attachment; filename="dm48_missing_deals_{current_date}.csv"'

    # writer = csv.writer(response, lineterminator='\n', delimiter=',')
    # writer.writerow(heading)
    # for row in rows:
    #     writer.writerow(row)
    # response.write(','.join(heading) + '\n')
    # for row in rows:
    #     response.write(','.join(map(str, row)) + '\n')
    # cursor.close()

    df.to_csv(response, index=False)
    return response


# =======================================
def missing_offers_ids(request):
    # =======================================
    query = """SELECT edr_id, TRIM(originating_id) MSISDN, dominant_err_cd AS ERROR_CODE, 
        qual_param_2_val AS TRANSACTION_TYPE, 
        session_id, future_11 AS new_sim_seq_num, future_12 AS new_msisdn, qual_param_3_val AS offer_code, 
    qual_param_4_val AS deal_id, event_start_datetime, 
    SUBSTR(adu, LENGTH(adu)- (TO_NUMBER(SUBSTR(adu, INSTR(adu,'95|')+3,3))), 
    TO_NUMBER(SUBSTR(adu, INSTR(adu, '95|') + 3, 3))) AS order_action_id
    FROM prm_dat_err_mngr WHERE iecd IN ('ACTV', 'MSIS', 'SISW') AND phy_file_id = 999999991
    """
    cursor = connections['default'].cursor()

    cursor.execute(query)
    output = cursor.fetchall()

    heading = ['EDR_ID', 'MSISDN', 'ERROR_CODE', 'TRANSACTION_TYPE',
               'SESSION_ID', 'NEW_SIM_SEQ_NUM', 'NEW_MSISDN', 'OFFER_CODE', 'DEAL_ID', 'EVENT_START_DATETIME',
               'ORDER_ACTION_ID']

    response = HttpResponse(content_type='text/csv')
    current_date = dt.datetime.today().strftime("%Y%m%d_%H%M")

    response[
        'Content-Disposition'] = f'attachment; filename="missing_Offer_codes_deal_ids_{current_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(heading)

    for line in output:
        writer.writerow(line)

    return response


# =======================================
def dm27_update(request):
    # =======================================
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in! And that was very sneaky!!!')
        return redirect('index.html')

    if "GET" == request.method:
        return render(request, 'a_prm/dm27_update.html', {})

    dm27_file = request.FILES["dm27_file"]

    try:
        df = pd.read_excel(dm27_file)

    except BadZipFile:
        messages.error(request, 'Problem with the file. Please check!')
        return render(request, 'a_prm/dm27_update.html')
    except Exception as e:
        messages.error(request, ('Problem with the file. Please check the following: ' + str(e)))
        return render(request, 'a_prm/dm27_update.html')

    df.columns = map(str.upper, df.columns)

    update_dm27 = """UPDATE prm_dat_err_mngr SET sys_update_date = sysdate , rec_handle_ind = 'R', next_process_ind = 'E', 
    qual_param_4_val = :deal_id, qual_param_3_val = :offer_code WHERE edr_id = :edr_id"""

    edr_id_list = []
    # rejects_list = []
    try:
        for _, excel_row in df.iterrows():
            edr_id = excel_row['EDR_ID']
            offer_code = excel_row['OFFER_CODE']
            deal_id = excel_row['DEAL_ID']

            edr_id_list.append({'deal_id': deal_id, 'offer_code': offer_code, 'edr_id': edr_id})
    except KeyError:
        messages.error(request,
                       'Problem with key value. Please use the following keys: [edr_id, offer_code, deal_id]')
        return render(request, 'a_prm/dm27_update.html')

    try:
        bulk_run('default', update_dm27, edr_id_list)

    except Exception as e:
        messages.error(request,
                       ('Problem with loading errors list onto database. Please check the following: ' + str(e)))
        return render(request, 'a_prm/dm27_update.html')

    context = {
        'message': "Update Completed",
    }

    messages.success(request, 'Update Completed Successfully')

    return render(request, 'a_prm/dm27_update.html')


# =======================================
def report_server_jobs(request):
    # =======================================

    model_class = PrmFlexReportsStatus

    qs = model_class.objects.filter(job_status__in=['RD', 'IU']).order_by('job_rec')
    context = {
        'title': "Report Server Jobs",
        'job_server_report': qs,
    }
    return render(request, "a_prm/report_server_jobs.html", context)
