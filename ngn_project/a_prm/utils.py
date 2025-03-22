import subprocess
from django.db import connections


def built_in_list(_id):
    rows = []
    for item in _id.split('\n'):
        item = item.rstrip()
        if item == '' or item is None:
            continue

        if item.find(';') > -1:
            items = item.split(';')
            for new_item in items:
                rows.append(new_item)
        else:
            rows.append(item)
    return rows


def host_connection_check(host):
    # ===========================================================
    command = f"""ls"""
    ssh = subprocess.Popen(["ssh", "%s" % host, command],
                           shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    result = ssh.stdout.readlines()

    if not result:
        error = ssh.stderr.readlines()
        return False

    return True


# ==================================================================================

def bulk_run(instance, query, add_orders_bulk):
    cursor = connections[instance].cursor()
    cursor.prepare(query)
    cursor.executemany(query, add_orders_bulk)
