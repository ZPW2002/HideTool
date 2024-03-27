import sqlite3
import os
import traceback
from contextlib import closing
import socket

with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    s.bind(('', 0))
    port = s.getsockname()[1]

mask_dic_data = {
    '无': '',
    '无关联文件': '.{00021401-0000-0000-c000-000000000046}',
    '回收站': '.{645ff040-5081-101b-9f08-00aa002f954e}',
    '脱机文件夹': '.{AFDB1F70-2A4C-11d2-9039-00C04F8EEB3E}',
    '管理工具': '.{D20EA4E1-3957-11d2-A40B-0C5020524153}',
    '历史记录': '.{Ff393560-C2a7-11cf-Bff4-444553540000}',
    '缓存文件夹': '.{88c6c381-2e85-11d0-94de-444553540000}',
    '拨号网络': '.{992CFFA0-F557-101A-88EC-00DD010CCC48}',
    '网上邻居': '.{208D2C60-3AEA-1069-A2D7-08002B30309D}'
}


def to_dict(cursor):
    key = ['path', 'folder', 'hide', 'mask']
    tar = [dict(zip(key, item)) for item in cursor]
    return tar


def mask_dic(mask):
    return mask_dic_data[mask]


def os_hide(path, hide):
    cmd = f'attrib "{path}" +s +h' if hide == '是' else f'attrib "{path}" -s -h'
    res = os.popen(cmd).read().splitlines()
    return res


def os_mask(path, mask):
    path_new = path.split('.{')[0] + mask_dic(mask)
    if path == path_new:
        return
    try:
        os.rename(path, path_new)
    except:
        return traceback.format_exc()
    return


class SQLManager():
    def __init__(self):
        self.conn = sqlite3.connect('data/data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        has_tab = self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='data'"
        ).fetchall()

        if not has_tab:
            self.cursor.execute(
                'create table data(path varchar(100), folder varchar(50), hide varchar(10), mask varchar(50))'
            )
            self.conn.commit()

        self.path_dic = {}
        self.path_real()

    def path_real(self, path=None):
        temp = self.cursor.execute('select * from data')
        self.path_dic = {item[0].split('.{')[0]: item[0] for item in temp}
        # for item in self.path_dic.items():
        #     print(item)
        if path:
            return self.path_dic[path]
        return

    def is_exist(self, path):
        return path in self.path_dic

    def get_list(self, sql):
        return to_dict(self.cursor.execute(sql))

    def modify(self, sql, args=None, comm=True):
        if not (self.is_exist(args[0])) ^ (args[1] == 'add'):
            return False

        self.cursor.execute(sql)
        if comm:
            self.conn.commit()
            self.path_real()
        return True

    def commit_(self):
        self.conn.commit()
        self.path_real()

    def close(self):
        self.conn.close()
